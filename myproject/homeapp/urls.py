from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('sec/',views.sec,name="next"),
    path('third/',views.third,name='third')
    
]
