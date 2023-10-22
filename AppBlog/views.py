from django.shortcuts import render
from django.template import RequestContext

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from AppBlog.forms import *
from AppBlog.models import *

class BlogsDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "AppBlog/blog_detail.html"

class BlogsListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "AppBlog/blogs.html"

class BlogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = "/"
    fields = ["title", "subtitle", "body","image"]

class BlogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "/"
class BlogsCreateView(LoginRequiredMixin, CreateView):

    model = Blog
    template_name = "AppBlog/create_blogs.html"
    fields = ["title", "subtitle", "body","image"]

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
class UsuarioEdicion(UpdateView):
    form_class = Profile
    template_name= 'AppBlog/profile.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    
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
def about(request):
    return render(request, "AppBlog/about.html")
class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppBlog/comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppBlog/change_password.html'
    success_url = reverse_lazy('success')

def password_exitoso(request):
    return render(request, 'AppBlog/password_success.html', {})

def handler404t(request, *args, **argv):
    response = render('404.html')
    response.status_code = 404
    return response