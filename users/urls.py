from django.contrib import admin
from django.urls import path
from users.Views.registration import registration

person_patterns = [
   path('signUp/', registration)
    
    
]