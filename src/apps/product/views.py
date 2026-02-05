from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from apps.product.permissions import CustomerRequired
from apps.product.serializers import BuyProductSerializer
from apps.product.services import BuyProductService
from apps.product.services.dtos import BuyProductIn


class BuyProductView(views.APIView):
    permission_classes = (CustomerRequired,)

    def post(self, request: Request) -> Response:
        serializer = BuyProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        BuyProductService(
            product_in=BuyProductIn(
                **serializer.validated_data,
            ),
        )(customer=request.user.customer)
        return Response(data={"message": "ok"})