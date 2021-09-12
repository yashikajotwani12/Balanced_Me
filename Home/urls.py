from django.urls import path
from Home import views
app_name = 'Home'


urlpatterns =[
    path('',views.index,name='home'),
    path('personal',views.personal,name="personal"),
    path('productivity',views.personal,name="productivity"),
    
]