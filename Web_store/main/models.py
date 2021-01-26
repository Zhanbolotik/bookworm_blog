from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=100)
    name = models.CharField(max_length= 100)
    def __str__(self):
        return f'{self.name} genre'

class Review(models.Model):
    title = models.CharField(max_length= 150)
    author = models.CharField(max_length= 50, default= 'people')
    description = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='reviews')
    written = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bk_review', kwargs={'pk': self.pk})

    @property
    def get_image(self):
        return  self.images.first()



class Image(models.Model):
    image = models.ImageField(upload_to='books')
    review = models.ForeignKey(Review, on_delete= models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url