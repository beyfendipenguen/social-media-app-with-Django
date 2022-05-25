from django.urls import path
from .views import (
    MyProfileData,
    MyProfileView
)

app_name = 'profiles'

urlpatterns = [
    path('my-profile', MyProfileView.as_view(), name='my-profile-view').
    path('my-profile-json', MyProfileData.as_view(), name='my-profile-json')
]
