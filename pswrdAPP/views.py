from django.shortcuts import render
import random


def home(request):
    return render(request, 'generatorapp/Home.html')


def contacts(request):
    return render(request, 'generatorapp/contacts.html')


def password(request):
    """PASSWORD GENERATION START"""
    length = int(request.GET.get('length', 12))

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    if request.GET.get('specials'):
        character.extend(list('!@#$%^&*_+'))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(character)
    """PASSWORD GENERATION END"""

    return render(request, 'generatorapp/password.html', {'password': thepassword})
