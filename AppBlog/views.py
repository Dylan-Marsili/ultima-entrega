from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class BlogsDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "AppBlog/blog_detail.html"

class BlogsListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "AppBlog/blogs.html"

class BlogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = "/"
    fields = ['nombre', 'apellido', 'email']

class BlogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "/"
class BlogsCreateView(LoginRequiredMixin, CreateView):

    model = Blog
    template_name = "AppBlog/create_blogs.html"
    fields = ["title", "subtitle", "body", "date","image"]

    success_url = reverse_lazy("pages")
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(request,username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppBlog/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppBlog/login.html", {"mensaje":"Datos incorrectos", 'form': form})
           
        else:

            return render(request, "AppBlog/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppBlog/login.html", {"form": form})

def register_request(request):
    if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  email = form.cleaned_data['email']
                  description = form.cleaned_data['description']
                  link = form.cleaned_data['link']
                  password1 = form.cleaned_data['password1']
                  
                  form.save()
                  return render(request,"AppBlog/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else: 
        form = UserRegisterForm()     

    return render(request,"AppBlog/register.html" ,  {"form":form})


def index(request):
    return render(request, "AppBlog/index.html")
@login_required
def profile(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        
        form = Profile(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            if info['password1'] != info['password2']:
                datos = {
                    'username': usuario.username,
                    'email': usuario.email
                }
                
                form = Profile(initial=datos)
            
            else:
                usuario.email = info['email']
                usuario.username = info['username']
                usuario.set_password(info['password1'])
                usuario.link = info['link']
                usuario.description = info['description']
                usuario.image = info['image']

                
            usuario.save()
            
            return render(request, 'AppBlog/index.html')
    else:
        form = Profile(initial={'email': usuario.email, 'username': usuario.username, 'link': usuario.link, 'description': usuario.description, 'image': usuario.image})
        
    return render(request, "AppBlog/edit.html", {"form": form})