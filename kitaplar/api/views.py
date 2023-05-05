from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from kitaplar.api.serializers import KitapSerializers, YorumSerializers
from kitaplar.models import Kitap



class KitapListCreateApiView(generics.ListCreateAPIView):

    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers

class KitapDetailAPIView(generics.RetrieveAPIView):

    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers




# class KitapListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #Listele
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     #Yarat
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)