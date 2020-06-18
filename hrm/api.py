from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class UserList(APIView):

    def get(self, request):
        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get(self, request, employee_id):
        try:
            model = Users.objects.get(id=employee_id)
        except Users.DoesNotExist:
            return Response(f'User With {employee_id} Not Found Is Not Found In Database', status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(model)
        return Response(serializer.data)

    def put(self, request, employee_id):
        try:
            model = Users.objects.get(id=employee_id)
        except Users.DoesNotExist:
            return Response(f'User With {employee_id} Not Found Is Not Found In Database', status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)