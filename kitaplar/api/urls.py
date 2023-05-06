from django.urls import path
from kitaplar.api import views as api_view

urlpatterns = [
    path("kitaplar/", api_view.KitapListCreateApiView.as_view(), name="kitap-listesi"),
    path("kitaplar/<int:pk>", api_view.KitapDetailAPIView.as_view(), name="kitap-bilgileri"),
    path("kitaplar/<int:kitap_pk>/yorum_yap", api_view.YorumCreateAPIView.as_view(), name="yorum-yap"),
    path("yorumlar/<int:pk>", api_view.YorumDetailAPIView().as_view(), name="yorumlar")
]
