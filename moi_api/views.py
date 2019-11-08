from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from .serializer import CreateUserSerializer

class CreateUserAPIView(CreateAPIView):
	serializer_class = CreateUserSerializer
	permission_classes = [permissions.AllowAny]

	def create(self, request, *args, **kwargs):
		if(	request.data.get('username',None) == None or 
			request.data.get('email',None) == None or
			request.data.get('password',None) == None):
			return Response(status.HTTP_406_NOT_ACCEPTABLE)
		serializer = self.get_serializer(data=request.data)
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
		
		