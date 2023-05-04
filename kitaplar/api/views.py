from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from kitaplar.api.serializers import KitapSerializers, YorumSerializers
from kitaplar.models import Kitap

class KitapListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers

    #Listele
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Yarat
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)