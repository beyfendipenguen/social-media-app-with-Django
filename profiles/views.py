from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Profile
from django.views.generic import TemplateView, View
# Create your views here.

class MyProfileView(TemplateView):
    template_name = "profiles/my_profile.html"

class MyProfileData(View):
    def get(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        qs = profile.get_proposals_for_following()
        profiles_to_follow_list = []
        for p in qs:
            profile_item = {
                'id': p.id,
                'user': p.user.username,
                'avatar': p.avatar.url
            }
            profiles_to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': profiles_to_follow_list})       