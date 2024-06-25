from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, Group, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import createGroupForm

def header(request): 
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'header.html', context)
def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        username = request.POST.get('username').lower()
        bio = request.POST.get('bio')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        picture = request.FILES.get('avatar')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already taken')
        elif password1 != password2:
            messages.error(request, "Passwords doesn't matched")
        else:
            user = User.objects.create(username=username, email=email, password=password1)
            profile = UserProfile.objects.create(user=user, bio=bio, picture=picture)

            login(request, user)
            return redirect('fields')



    context = {}
    return render(request, 'base/registration.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('fields')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(email=email)
            if user.password == password: 
                login(request, user)
                return redirect("fields")
            
            else:
                messages.error(request, 'Invalid Password') 
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')    
    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

login_required(login_url="login")
def profile(request):
    context = {}
    return render(request, 'base/profile.html', context)

login_required(login_url="login")
def Editprofile(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        bio = request.POST.get('bio')
        picture = request.FILES.get('avatar')

        user = request.user

        user.username = username
        user.userprofile.bio = bio
        user.userprofile.picture = picture

        user.save()
        user.userprofile.save()

        return redirect('fields')
    context = {}
    return render(request, 'base/editprofile.html', context)

def createGroup(request):
    context = {}
    return render(request, 'base/createGroup.html', context)

def deleteGroup(request):
    context = {}
    return render(request, 'base/deleteGroup.html', context)

def updateGroup(request):
    context = {}
    return render(request, 'base/updateGroup.html', context)

def field(request):
    groups = Group.objects.all()
    context = {"groups":groups}
    return render(request, 'base/field.html', context)

def groupPage(request, pk):
    groups = Group.objects.all()
    group = Group.objects.get(id=pk)
    messages = group.message_set.all()
    participants = group.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            sender = request.user,
            group=group,
            content=request.POST.get('body')
        )
    context = {'groups': groups, 'group':group, 'messages':messages, 'participants':participants}
    return render(request, 'base/group.html', context)

def updateMessage(request):
    context = {}
    return render(request, 'base/updateMessage.html', context)

def deleteMessage(request):
    context = {}
    return render(request, 'base/deleteMessage.html', context)

def add_joiners(request, pk):
    group = Group.objects.get(id=pk)
    group.joiners.add(request.user)
    return redirect("fields")
def add_participant(request, groupId, userId):
    group = Group.objects.get(id=groupId)
    user = User.objects.get(id=userId)
    if request.user == Group.admin:
        group.participants.add(user)
        return redirect("group")
    else:
        return redirect("fields")
def createGroup(request):
    form = createGroupForm()
    if request.method == "POST":
        form = createGroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fields")
    context = {'form':form}
    return render(request, 'base/createGroup.html', context)
