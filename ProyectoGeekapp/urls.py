from django.urls import path
from . import views
from .views import HomeView



urlpatterns = [
    path('', HomeView.as_view(),name="home"),

    path('search/', views.filterchats, name="search"),

    path('register/',views.signup,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.log_out,name="logout"),
    path('createSala/',views.createSala,name="createSala"),
    path('createComentario/',views.createComentario,name="createComentario"),
    path('UpdateComentario/<str:pk>', views.UpdateComentario, name="UpdateComentario"),
    path('BorrarComentario/<str:pk>', views.BorrarComentario, name="BorrarComentario"),




]