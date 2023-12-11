from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<name>/<id>', views.pathview, name='pathview'),
    path('showform/', views.showform, name='showform'),
]
