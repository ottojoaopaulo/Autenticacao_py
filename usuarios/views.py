from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def cadastro (request):
    if request.method == "GET":  
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse ('ja existe um usuario com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()


        return HttpResponse('Usuario cadastrado com sucesso')

def login (request):
    return render(request, 'login.html')
