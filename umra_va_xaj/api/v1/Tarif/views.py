from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serialazer import TarifSerializer
from .services import format_tarif, paginated_tarif
from umravaxajapp.models import SubCategory
from base.helper import BearerToken


class TarifView(GenericAPIView):
    serializer_class = TarifSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk=None):
        try:
            root = SubCategory.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} tarif yo'q!")
        return root

    def delete(self, requests, pk, *args, **kwargs):
        tarif = SubCategory.objects.filter(pk=pk).first()
        if not tarif:
            result = {"ErrOr": "Bunday tarif mavjud emas!"}

        else:
            tarif.delete()
            result = {"Success": "Tarif o'chirib tashlandi!"}

        return Response(result)

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            tarif = SubCategory.objects.filter(pk=pk).first()
            if not tarif:
                result = {"ERROR": "Bunday tarif mavjud emas!"}
            else:
                result = format_tarif(tarif)
        else:
            result = paginated_tarif(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_tarif(result))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serialazer = self.get_serializer(data=data, partial=True, instance=root)
        serialazer.is_valid(raise_exception=True)
        result = serialazer.save()

        return Response(format_tarif(result))
