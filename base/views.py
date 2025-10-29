from django.shortcuts import render, redirect
from .models import Room
from .form import RoomForm
# Create your views here.

rooms = [
    {'id': 1, 'name': "Web Design"},
    {'id': 2, 'name': "Artificial Inteligence"},
    {'id': 3, 'name': "Django Development"}

]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


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
