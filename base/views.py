from django.shortcuts import render, redirect
from .models import Room
from .form import RoomForm
# Create your views here.


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
