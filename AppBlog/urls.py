from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="inicio"),
    path("about/", about,  name="about"),
    path("pages/", BlogsListView.as_view(),  name="pages"),
    path("create_blog/", BlogsCreateView.as_view(), name="create_blogs"),
    path('detail/<int:pk>', BlogsDetailView.as_view(), name="detail"),
    path('comentario/<int:pk>', ComentarioPagina.as_view(), name="comentario"),
    path("update/<int:pk>", BlogsUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", BlogsDeleteView.as_view(), name="delete"),
    path('accounts/login/', login_request, name='login'),
    path('accounts/register/', register_request, name='register'),
    path('accounts/profile/', UsuarioEdicion.as_view(), name='profile'),
    path('accounts/change_password/', CambioPassword.as_view(), name='change_password'),
    path('accounts/success/', password_exitoso, name='success'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/index.html'), name='logout'),
]

handler404 = 'AppBlog.views.handler404t'