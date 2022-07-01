from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=80)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
