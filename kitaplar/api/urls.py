from django.urls import path
from kitaplar.api import views as api_view

urlpatterns = [
    path("kitaplar/", api_view.KitapListCreateApiView.as_view(), name="kitap-listesi")
]
