from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serialazer import ContactSerializer
from .services import format_contact, paginated_contact
from umravaxajapp.models import Contact
from base.helper import BearerToken


class ContactView(GenericAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk=None):
        try:
            root = Contact.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} contact yo'q!")
        return root

    def delete(self, requests, pk, *args, **kwargs):
        contact = Contact.objects.filter(pk=pk).first()
        if not contact:
            result = {"ErrOr": "Bunday contact mavjud emas!"}

        else:
            contact.delete()
            result = {"Success": "Contact o'chirib tashlandi!"}

        return Response(result)

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            contact = Contact.objects.filter(pk=pk).first()
            if not contact:
                result = {"ERROR": "Bunday contact mavjud emas!"}
            else:
                result = format_contact(contact)
        else:
            result = paginated_contact(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_contact(result))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serialazer = self.get_serializer(data=data, partial=True, instance=root)
        serialazer.is_valid(raise_exception=True)
        result = serialazer.save()

        return Response(format_contact(result))
