from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from itertools import chain
import random
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    avatar = models.ImageField(_("avatar"), upload_to='avatars', height_field=None, width_field=None, max_length=None,default='avatar.png')  
    background = models.ImageField(_("background"), upload_to='backgrounds', height_field=None, width_field=None, max_length=None,default='background.png')
    following = models.ManyToManyField(User,related_name='following',blank=True, verbose_name=_("following"))
    bio = models.TextField(_("bio"),default="no bio..")
    created = models.DateField(_("created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def get_my_posts(self):
        return self.posts.all()

    @property
    def num_posts(self):
        return self.posts.all().count()
    
    def get_following(self):
        return self.following.all()
    
    def get_following_users(self):
        following_list = [p for p in self.get_following()]
        return following_list

    def get_my_and_following_posts(self):
        users = self.get_following_users()
        posts = []
        qs = None
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.posts.all()
            posts.append(p_posts)
        my_posts = self.posts.all()
        posts.append(my_posts)
        if len(posts) > 0:
            #this is important operation
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
        return qs
    
    def get_proposals_for_following(self):
        profiles = Profile.objects.all().exclude(user=self.user)
        followers_list = self.get_following_users()
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

    @property
    def following_count(self):
        return self.get_following().count()

    def get_followers(self):
        qs = Profile.objects.all()
        followers_list = []
        for profile in qs:
            if self.user in profile.get_following():
                followers_list.append(profile)
        return followers_list

    @property
    def followers_count(self):
        return len(self.get_followers())