from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.newsp, name='news'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('newsdate/<int:year>', views.newsdate, name='newsdate'),
    path('addUser/', views.addUser, name='addUser'),
    path('signup/', views.register, name='register'),
    path('modalform/', views.modalform, name='modalform'),
    path('addmodalform/', views.addModalForm, name='form'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login', views.login, name='login2'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/register', views.register, name='modalform'),
    path('addlogin', views.addModallogin, name='modallogin')


]

