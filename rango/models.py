from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=128, unique=True)
  views = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  slug = models.SlugField(unique=True)# warning cannot add this unique attribute til after the database is created and populated as this unique constraint would have been violated

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)
  
  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name


class Page(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    
    class Meta:
      verbose_name_plural = 'Page'

    def __str__(self):
        return self.title
