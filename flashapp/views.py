from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
from .forms import SignUpForm, AddDeckForm, AddCardForm
from .models import Deck, Card
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url=('signup/'))
def homepage(request):
    decks = Deck.objects.filter(user_id=request.user.id)
    return render(request, 'homepage.html', {"decks": decks})

def deck(request, deck):
    current_deck = Deck.objects.get(id=deck)
    cards = Card.objects.filter(deck_id=deck)
    return render(request, 'deck.html', {"deck": current_deck, "cards": cards})

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

def add_card(request, deck):
    if request.method == 'POST':
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = Card(title=form.cleaned_data.get('title'),
                        notes=form.cleaned_data.get('notes'),
                        deck=Deck.objects.get(id=deck))
            card.save()
            return redirect('deck', deck=int(deck))
        else:
            return render(request, 'add-card.html', {'form': form})
    else:
        form = AddCardForm()
        return render(request, 'add-card.html', {'form': form})

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


def delete_view(request, card):
    current_card=Card.objects.get(id=card)
    deck=current_card.deck
    current_card.delete()
    return redirect('deck', deck=deck.id)

def edit_card(request, card):
    page_title = "Edit Card"
    editting_card = Card.objects.get(id=card)

    if request.method == 'POST':
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = Card.objects.get(id=card)
            card.title=form.cleaned_data.get('title')
            card.notes=form.cleaned_data.get('notes')
            card.date_updated = timezone.now()
            card.save()
            return redirect('deck', deck=card.deck.id)
        else:
            return render(request, 'add-card.html', {'form': form, "page_title": page_title})
    else:
        form = AddCardForm(initial={'title': editting_card.title, 'notes': editting_card.notes})
        return render(request, 'add-card.html', {'form': form, "page_title": page_title})

def search (request):
    if 'card' in request.GET  and request.GET['card']:
        search_term=request.GET.get('card')
        cards=Card.objects.filter(title__icontains=search_term)
        return render(request, 'search.html', {'search_term': search_term,'cards': cards})
    else:
        message='No results'
        return render(request, 'search.html', {'message':message})

        