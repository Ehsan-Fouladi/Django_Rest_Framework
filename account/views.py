from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterAPISerializers, UserSerializers
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class RegisterAPI(APIView):
    serializer_class = RegisterAPISerializers

    def post(self, request):
        ser_register_data = RegisterAPISerializers(data=request.POST)
        if ser_register_data.is_valid():
            ser_register_data.create(ser_register_data.validated_data)
            return Response(ser_register_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_register_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request):
        srz_data = UserSerializers(instance=self.queryset, many=True)
        return Response(data=srz_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserSerializers(instance=user)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({"permissions": "Not user"})
        srz_data = UserSerializers(
            instance=user, data=request.POST, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({"permissions": "Not user"})
        user.delete()
        # user.is_active = True
        # user.save()
        return Response({'message': "user delete sussesfull"})
