from django.shortcuts import render, redirect, reverse
from models import Task, User
from django.contrib import messages
import time, re

Date_regex = re.compile(r'^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$')

# Functions here will delegate to the correct method based on the HTTP verb

def user(request):
    if request.method == "POST":
        return create(request)
    # Else it's a GET, send to index method to return HTML
    return index(request)

def users_w_id(request, id):
    if request.method == "POST":
        return update(request, id)
    return show(request, id)

# *************************************************************************

# GET /users
def index(request):
    # Retrieve all Tasks to display in template
    Tasks = Task.objects.all().order_by('time')
    user = User.objects.get(id=request.session['user'])
    date_now = time.strftime("%Y-%m-%d")

    context = {
        "tasks" : Tasks, "date_now" : date_now
    }
    return render(request, "appointment_app/index.html", context)

# POST /users
def create(request):
    if not Date_regex.match(request.POST['date']):
        messages.error(request, 'Fix your date')
        return redirect('/task')
    user = User.objects.get(id=request.session['user'])
    Task.objects.create(created_by=user, date=request.POST['date'], time=request.POST['time'], task=request.POST['task'])
    return redirect(reverse('task:user'))

# GET /users/new
def new(request):
    return render(request, 'appointment_app/new.html')

# GET /users/<id>
def show(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'appointment_app/show.html', { 'Task' : Task })


# POST /task/<id>
def update(request, id):
    task = Task.objects.get(id=id)
    task.task = request.POST['task']
    task.date = request.POST['date']
    task.time = request.POST['time']
    task.status = request.POST['status']
    task.save()
    return redirect('/task')

# GET /users/<id>/edit
def edit(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'appointment_app/edit.html', { 'Task' : task })

# POST /users/<id>/destroy
def destroy(request, id):
    Task.objects.get(id=id).delete()
    return redirect('/task')
