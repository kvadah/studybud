from django.shortcuts import render, redirect
from .models import Room, Topic
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from .form import RoomForm
from django.contrib import messages
# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exsist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'wrong username or password ')

    context = {}
    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.all()
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q))
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'home.html', context)


def room(request, pk):

    room = Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, "room.html", context)


def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/create_room.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/create_room.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    else:
        print("couldn't delete")
    return render(request, 'base/delete.html', {'obj': room})
