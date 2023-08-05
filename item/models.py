from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    #strings representation of the model richtig ausgeben
    class Meta:
        # Sortierung nach Name
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        # Name des Objekts zurückgeben in der Liste
        return self.name
    
    
class Item(models.Model):
    #settings.py muss angepasst werden wegen den bildern
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        # Name des Objekts zurückgeben in der Liste
        return self.name