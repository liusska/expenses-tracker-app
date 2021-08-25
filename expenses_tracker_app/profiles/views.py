from django.shortcuts import render, redirect
from expenses_tracker_app.expenses.models import Expense
from expenses_tracker_app.profiles.models import Profile
from expenses_tracker_app.profiles.forms import ProfileForm
from expenses_tracker_app.core.profile_utils import get_profile


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request, pk):
    profile = get_profile()
    form = ProfileForm(instance=profile)
    if form.is_valid():
        profile.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request, pk):
    profile = get_profile()
    expenses = Expense.objects.all()
    if request.method == "POST":
        profile.delete()
        expenses.delete()
        return redirect('home')
    context = {
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context)


