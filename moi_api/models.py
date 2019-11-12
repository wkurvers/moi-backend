from django.db import models

class favorite(models.Model):
    favorite_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.favorite_name
