from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='news/',default='news/default.jpg')
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    # tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return "{} - {}".format(self.title,self.id)

    def is_published_date(self):
        if timezone.now() >= self.published_date:
            return True
        else:
            return False

class Meta:
    ordering = ('-created_date',)
    