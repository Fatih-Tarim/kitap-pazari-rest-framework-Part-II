from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from kitaplar.api.permissions import IsAdminUserOrReadOnly

from kitaplar.api.serializers import KitapSerializers, YorumSerializers
from kitaplar.models import Kitap, Yorum



class KitapListCreateApiView(generics.ListCreateAPIView):

    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers
    permission_classes = [IsAdminUserOrReadOnly]

class KitapDetailAPIView(generics.RetrieveAPIView):

    queryset = Kitap.objects.all()
    serializer_class = KitapSerializers
    permission_classes = [permissions.IsAdminUser]

class YorumCreateAPIView(generics.CreateAPIView, ListModelMixin):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        # path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)

class YorumDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializers
    permission_classes = [permissions.IsAuthenticated]

    












# class KitapListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializers

#     #Listele
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     #Yarat
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)