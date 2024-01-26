from django.urls import path
from . import views

from myapp.views.index import IndexView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('hello/<name>/<id>', views.pathview, name='pathview'),
    # path('showform/', views.showform, name='showform'),
    # path('getform/', views.getform, name='getform'),
    # path("drinks/<str:drink_name>", views.drinks, name="drink_name"),
    # path('menu', views.menu, name='menu'),
    # path('about', views.about, name='about'),
    path('index', IndexView.as_view(), name='index'),
]
