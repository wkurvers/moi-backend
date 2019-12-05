from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class favorite(models.Model):
    favorite_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.favorite_name


class User_SearchProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	scheme_names = ArrayField(models.CharField(max_length=100),default=list)
	location_distance = models.IntegerField(default=1)
	location_position_lat = models.DecimalField(max_digits=25, decimal_places=20, default=0)
	location_position_lng = models.DecimalField(max_digits=25, decimal_places=20, default=0)
	type_names = ArrayField(models.CharField(max_length=100), default=list)
	min_workers = models.IntegerField(default=0)
	max_workers = models.IntegerField(default=0)
	min_start_year = models.CharField(max_length=4, default="1900")
	max_start_year = models.CharField(max_length=4, default="1900")
	lawform_names = ArrayField(models.CharField(max_length=100),default=list)
	BAG_names = ArrayField(models.CharField(max_length=100),default = list)
	def __str__(self):
		return "searchprofile " + str(self.pk) + " for " + self.user.username