from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post-images')
    allowed_comment = models.BooleanField(default=False)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='likes')
    saves = models.ManyToManyField(CustomUser, blank=True, related_name='saves')
    slug = models.SlugField()

    def number_of_likes(self):
        return self.likes.count()

    def number_of_save(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) + ' + ' + str(self.created) + str(self.author)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'


# Notes
class Note(models.Model):
    title = models.CharField(max_length=255)
    note = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'Notes'
        ordering = ('-created',)

    def __str__(self):
        return self.title
