from django.shortcuts import render, redirect
from .forms import RegisterForm, ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'expenses': expenses})

@login_required
def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.user = request.user
        expense.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Add Expense'})

@login_required
def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.user != expense.user:
        return redirect('dashboard')
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Expense'})

@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.user == expense.user:
        expense.delete()
    return redirect('dashboard')
