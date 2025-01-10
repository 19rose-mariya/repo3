
from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")  # Title of the section
    content = models.TextField()  # Main content of the "About Us" section
    image = models.ImageField(upload_to='about_images/', blank=True, null=True) #Optional image
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"