from django.urls import path

from . import views

urlpatterns = [
    path('mamago/', views.mamago),
    path('translated/', views.translated),
    path('static_example/', views.static_example),
    path('template_language/', views.template_language),
    path('hello/<str:name>/<int:age>', views.hello),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('index/', views.index),
]