from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.registerPage, name = "register"),
	path('login/', views.loginPage, name = "login"),  
	path('logout/', views.logoutUser, name = "logout"),
    path('aboutus/', views.aboutus, name = "aboutus"),
    path('contact/', views.contact, name = "contact"),
    path('blog/', views.blog, name = "blog"),
    path('temp2/', views.temp2, name = "temp2"),
    path('temp3/', views.temp3, name = "temp3"),
    path('index/', views.index, name = "index"),
    path('cv/', views.cv, name = "cv"),
]
