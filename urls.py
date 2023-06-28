from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.predict,name='perd_diabetes'),
    path("",include("registration.urls")),
]