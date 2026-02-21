from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from apps.product.permissions import CustomerRequired
from apps.product.serializers import BuyProductSerializer
from config.container import container

class BuyProductView(views.APIView):
    permission_classes = (CustomerRequired,)

    def post(self, request: Request) -> Response:
        serializer = BuyProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = container.resolve("BuyProductService", data=serializer.validated_data)
        service(customer=request.user.customer) # вызываем __call__
        return Response(data={"message": "ok"})