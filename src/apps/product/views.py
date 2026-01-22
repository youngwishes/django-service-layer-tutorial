from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from apps.product.serializers import BuyProductSerializer


class BuyProductService(views.APIView):
    def post(self, request: Request) -> Response:
        serializer = BuyProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data={"message": "Api is working now"})
