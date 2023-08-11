from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from users.models import NewUser


class Agent(models.Model):
    name = models.CharField(max_length=100)
    agent_pic = models.ImageField(upload_to='agent_pics')
    bio = models.TextField(blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(_('Image'), blank=True, upload_to='property_images/')
    house_address = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    amount = models.IntegerField(blank=True)
    status = models.TextField(blank=True, null=True)
    beds = models.IntegerField(blank=True)
    baths = models.IntegerField(blank=True)
    garages = models.IntegerField(blank=True)
    area = models.CharField(blank=True, max_length=100)
    description = models.TextField(max_length=1000)
    agents = models.ManyToManyField(Agent, related_name='properties')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    post_image = models.ImageField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    short_content = models.TextField(blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.short_content:
            self.short_content = self.content[:200] + '...'  # Generate shortened content
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
