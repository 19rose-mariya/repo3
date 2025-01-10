from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # For URL-friendly category names

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # Correct pluralization in admin

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Allow blank descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Product belongs to a category
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True) # Stock Keeping Unit
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True) #Product visibility
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # Order products by creation date (newest first)
        verbose_name_plural = "Products"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_thumbnail = models.BooleanField(default=False) #Designate one image as thumbnail

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name_plural = "Product Images"
