from django.urls import path
from . import views
from .views import HomeView



urlpatterns = [
    #path('', views.home,name="home"),
    path('home/', HomeView.as_view(),name="home"),
    #path('about/',views.contact),
    path('register/',views.signup,name="register"),
    path('login/',views.login_page,name="login"),
    path('createSala/',views.createSala,name="createSala"),
    path('createComentario/',views.createComentario,name="createComentario"),
    path('UpdateComentario/<str:pk>', views.UpdateComentario, name="UpdateComentario"),
    path('BorrarComentario/<str:pk>', views.BorrarComentario, name="BorrarComentario"),




]