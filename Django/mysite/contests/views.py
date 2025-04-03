from django.shortcuts import render, redirect, get_object_or_404
from .form import ContestForm
from django.contrib.auth.decorators import login_required
from .models import Contest, ContestForm
from .form import ContestForm
from .form import AdminContestForm, UserContestSignupForm 
from django.utils import timezone


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the contest page!")

def create_contest(request):
    if request.method == 'POST':
        form = AdminContestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdminContestForm()

    return render(request, 'contests/create_contest.html', {'form': form})

def contest_list(request):
    latest_contest_list = Contest.objects.all()
    latest_contest_list = Contest.objects.order_by('-pub_date')  # <- good default
    return render(request, 'contests/contest_list.html', {
        'latest_contest_list': latest_contest_list,
    } )

#@login_required
def contest_signup(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)

    if request.method == 'POST':
        form = UserContestSignupForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.contest = contest
            signup.pub_date = timezone.now()
            signup.save()
            return redirect('thank_you')
    else:
        form = UserContestSignupForm()

    return render(request, 'contests/contest_signup.html', {
        'form': form,
        'contest': contest
    })

def thank_you(request):
    return render(request, 'contests/thank_you.html')