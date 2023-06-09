from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication

from .serialazer import CategorySerializer
from .services import format_ctg, paginated_ctg
from umravaxajapp.models import Category
from base.helper import BearerToken


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk=None):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} IDsidagi categoriya yo'q!")
        return root

    def delete(self, requests, pk, *args, **kwargs):
        ctg = Category.objects.filter(pk=pk).first()
        if not ctg:
            result = {"ErrOr": "Bunday category mavjud emas!"}

        else:
            ctg.delete()
            result = {"Success": "Category o'chirib tashlandi!"}

        return Response(result)

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            ctg = Category.objects.filter(pk=pk).first()
            if not ctg:
                result = {"ERROR": "Bunday categoriya mavjud emas!"}
            else:
                result = format_ctg(ctg)
        else:
            result = paginated_ctg(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_ctg(result))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serialazer = self.get_serializer(data=data, partial=True, instance=root)
        serialazer.is_valid(raise_exception=True)
        result = serialazer.save()

        return Response(format_ctg(result))
