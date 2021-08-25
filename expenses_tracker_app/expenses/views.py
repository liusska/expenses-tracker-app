from django.shortcuts import render, redirect
from expenses_tracker_app.expenses.forms import ExpenseForm
from expenses_tracker_app.expenses.forms import CreateExpenseForm
from expenses_tracker_app.expenses.forms import EditExpenseForm
from expenses_tracker_app.expenses.forms import DeleteExpenseForm
from expenses_tracker_app.expenses.models import Expense
from expenses_tracker_app.core.profile_utils import get_profile


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)

    context = {
        'expenses': expenses,
        'budget': budget,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == "POST":
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,

    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,

    }
    return render(request, 'expense-delete.html', context)

