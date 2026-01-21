from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name