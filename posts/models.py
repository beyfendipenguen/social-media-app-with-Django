from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    picture = models.ImageField(_("picture"),blank=True, upload_to="images", height_field=None, width_field=None, max_length=None)
    body = models.TextField(_("body"))
    liked = models.ManyToManyField(User, verbose_name=_("liked"), default=None, blank=True)
    author = models.ForeignKey(Profile,related_name="posts", verbose_name=_("author"), on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

    def get_liked(self):
        return self.liked.all()
    
    @property
    def like_count(self):
        return self.liked.all().count()