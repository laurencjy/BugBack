"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from database.views import UserViewSet,BugViewSet, RoleViewSet, LoginViewSet, RegisterViewSet, LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'users', UserViewSet, basename='user')
router.register(r'bugs', BugViewSet, basename='bug')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/login', LoginViewSet, basename='login')


urlpatterns = [
    path('', include(router.urls)),
	path("main", include("database.urls")),

]

