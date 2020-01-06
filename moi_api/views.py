from rest_framework import permissions, status
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .models import User_SearchProfile
from .serializer import CreateUserSerializer

class CreateUserSearchProfileAPIView(CreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	#permission_classes = [permissions.AllowAny] #DEBUGGING ONLY

	def validateData(self,data):
		bags = data.get('bags',None)
		lawForms = data.get('lawForms', None)
		location = data.get('location', None)
		startYear = data.get('startYear', None)
		themes = data.get('themes', None)
		types = data.get('types', None)
		workers = data.get('workers', None)
		if( type(bags) != list or
			type(lawForms) != list or
			type(startYear) != list or
			type(themes) != list or
			type(workers) != list):
			return False
		return True

	def create(self, request, *args, **kwargs):
		if(self.validateData(request.data)):
			try:
				sp = User_SearchProfile(
					user=request.user,
					scheme_names = request.data.get('themes'),
					location_distance = request.data.get('location')['distance'],
					location_position_lat = request.data.get('location')['position']['lat'],
					location_position_lng = request.data.get('location')['position']['lng'],
					type_names = request.data.get('types'),
					min_workers = request.data.get('workers')[0],
					max_workers = request.data.get('workers')[1],
					min_start_year = request.data.get('startYear')[0],
					max_start_year = request.data.get('startYear')[1],
					lawform_names = request.data.get('lawForms'),
					BAG_names = request.data.get('bags')
				)
				sp.save()
				return Response(
					{'searchProfileId': sp.id},
					status=status.HTTP_201_CREATED,
				)
			except User.DoesNotExist:
				return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
		else:
			return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class CreateUserAPIView(CreateAPIView):
	serializer_class = CreateUserSerializer
	permission_classes = [permissions.AllowAny]

	def create(self, request, *args, **kwargs):
		if(	request.data.get('username',None) == None or 
			request.data.get('email',None) == None or
			request.data.get('password',None) == None):
			return Response(status.HTTP_406_NOT_ACCEPTABLE)
		serializer = self.get_serializer(data=request.data)
		try:
			user = User.objects.get(username=request.data.get('username',None))
			return Response(status=status.HTTP_409_CONFLICT)
		except User.DoesNotExist:
			if(serializer.is_valid()):
				self.perform_create(serializer)
				headers = self.get_success_headers(serializer.data)
				return Response(
					{**serializer.data},
					status=status.HTTP_201_CREATED,
					headers=headers
				)
			else:
				return Response(status=status.HTTP_406_NOT_ACCEPTABLE)