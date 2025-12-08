from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "status": False,
            "message": "Validation Error",
            "errors": response.data
        }, status=response.status_code)

    return Response({
        "status": False,
        "message": "Internal Server Error",
        "errors": str(exc)
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
