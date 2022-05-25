from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    avatar = models.ImageField(_("avatar"), upload_to='avatars', height_field=None, width_field=None, max_length=None,default='avatar.png')  
    background = models.ImageField(_("background"), upload_to='backgrounds', height_field=None, width_field=None, max_length=None,default='background.png')
    following = models.ManyToManyField(User,related_name='following',blank=True, verbose_name=_("following"))
    created = models.DateField(_("created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
