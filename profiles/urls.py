from django.urls import path
from .views import (
    MyProfileData,
    MyProfileView
)

app_name = 'profiles'

urlpatterns = [
    path('my-profiles', MyProfileView.as_view(), name='my-profile-view'),
    path('my-profiles-json/', MyProfileData.as_view(), name='my-profile-view')
]
