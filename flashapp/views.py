from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
from .forms import SignUpForm, AddDeckForm
from .models import Deck
from django.contrib.auth import logout

def homepage(request):
    decks = Deck.objects.filter(user_id=request.user.id)
    return render(request, 'homepage.html', {"decks": decks})

def add_deck(request):
    if request.method == 'POST':
        form = AddDeckForm(request.POST)
        if form.is_valid():
            deck = Deck(title=form.cleaned_data.get('title'),
                        user=request.user)
            deck.save()
            return redirect('homepage')
        else:
            return render(request, 'add-deck.html', {'form': form})
    else:
        form = AddDeckForm()
        return render(request, 'add-deck.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("handling signup")
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.profile_photo = form.cleaned_data.get('profile_photo')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print("signed up")
            return redirect('homepage')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
