
from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name="home"),
path('add.html',views.add,name="add"),
path('sub.html',views.sub,name="sub"),
path('divide.html',views.divide,name="divide"),
path('multiply.html',views.multiply,name="multiply"),
]
