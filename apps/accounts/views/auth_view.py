from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.helpers.response import success_response,error_response
from ..services import register_user
from ..serializers import RegisterSerializer ,LoginSerializer

import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        try:
            logger.info("Registration started")
            serializer = RegisterSerializer(data=request.data)
            if not serializer.is_valid():
                logger.warning(
                    "Registration validation failed: %s",
                    serializer.errors
                )
                first_error = next(iter(serializer.errors.values()))[0]
                return error_response(first_error, "Validation Error")

            user = register_user(serializer.validated_data)
            refresh = RefreshToken.for_user(user)

            logger.info("User registered successfully: %s", user.email)

            return success_response({
                "status": True,
                "message": "Registration successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            })
        except Exception as e:
            logger.exception("Unexpected error during registration")
            return error_response("error", e)


class LoginView(APIView):

    def post(self, request):
        try:
            logger.info("Login request received")

            serializer = LoginSerializer(data=request.data)

            if not serializer.is_valid():
                first_error = next(iter(serializer.errors.values()))[0]
                logger.warning("Login failed: %s", first_error)
                return error_response("Validation Error", first_error)

            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)

            logger.info("User logged in successfully: %s", user.email)

            return success_response({
                "message":"Login successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            })
        except Exception as e:
            logger.exception("Unexpected error during Login")
            return error_response("error", e)

