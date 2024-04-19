from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import OrdenForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "home.html")

def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html", {
            "form": UserCreationForm
        })
    else:
        req = request.POST
        if req['password1'] == req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError as ie:
                return render(request, "registro.html", {
                    "form": UserCreationForm,
                    "msg": "Ese usuario ya existe, favor de elegir otro nombre de usuario"
                })
            except Exception as e:
                return render(request, "registro.html", {
                    "form": UserCreationForm,
                    "msg": f"Se ha presentado el siguiente error {e}"
                })
        else:
            return render(request, "registro.html", {
                "form": UserCreationForm,
                "msg": "Favor de verificar que las contraseñas coincidan"
            })

def iniciarsesion(request):
    if request.method == "GET":
        return render(request, "login.html", {
            "form": AuthenticationForm(),
            "msg": None
        })
    elif request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {
                "form": form,
                "msg": "El usuario o la contraseña son incorrectas"
            })


def cerrarsesion(request):
    logout(request)
    return redirect("/")
