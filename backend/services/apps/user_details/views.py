# Django
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Libraries
from user_details.exceptions import UserNotFound
from user_details.repositories.django_repository import DjangoUserRepository
from user_details.services import UserServices


class CreateUserView(APIView):
    user_repository = DjangoUserRepository()
    user_services = UserServices(user_repository)

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.EmailField()
        phone_number = serializers.CharField()
        dob = serializers.DateField()
        address = serializers.CharField()
        username = serializers.CharField()
        password = serializers.CharField()
        is_admin = serializers.BooleanField(required=False, default=False)

    class OutputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()

    def post(self, request):
        input_data = self.InputSerializer(data=request.data)
        input_data.is_valid(raise_exception=True)

        user = self.user_services.create_user(**input_data.validated_data)
        output_data = self.OutputSerializer(user).data

        return Response(output_data, status=status.HTTP_201_CREATED)


class GetUserView(APIView):
    user_repository = DjangoUserRepository()
    user_services = UserServices(user_repository)

    class OutputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.EmailField()
        phone_number = serializers.CharField()
        dob = serializers.DateField()
        address = serializers.CharField()
        username = serializers.CharField()
        is_admin = serializers.BooleanField()

    def get(self, request, id):
        try:
            user = self.user_services.get_user(id=id)
        except UserNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        output_data = self.OutputSerializer(user).data

        return Response(output_data)
