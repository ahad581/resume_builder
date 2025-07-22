from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('profile/', views.profile_view, name='account_profile'),
]