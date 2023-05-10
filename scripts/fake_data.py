import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')
# os.environ["DJANGO_SETTINGS_MODULE"] = "kitap_pazari.settings"

import django
django.setup()

import requests

from django.contrib.auth.models import User

from faker import Faker

def set_user():
    fake = Faker(['en_US'])

    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = f"{first_name.lower()}_{last_name.lower()}"
    email = f"{user_name}@{fake.domain_name()}"
    print(first_name, last_name, user_name, email)

    user_check = User.objects.filter(username=user_name)
    while user_check.exist():
        user_name = user_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username=user_name)

    user = User(
        username = user_name,
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50)
    )
    user.set_password('testing321..')
    user.save()

# for i in range(1,20):
#     set_user()

from pprint import pprint
from kitaplar.api.serializers import KitapSerializers

def kitap_ekle(konu):
    fake = Faker(['en_US'])

    #İstek
    url = "https://openlibrary.org/search.json"
    payload = {'q':konu}
    response = requests.get(url, params=payload)
    #Kontrol
    if response.status_code != 200:
        print("Hatalı İstek Yapıldı: ", response.status_code)
        return 
    jsn = response.json()
    #İhtiyaç olan veri
    kitaplar = jsn.get('docs')
    for kitap in kitaplar:
        kitap_adi = kitap.get('title')
        data = dict(
            isim = kitap_adi,
            yazar = kitap.get('author_name')[0],
            aciklama = kitap.get('author_facet')[0],
            yayin_tarihi = fake.date_time_between_dates()
        )
        #Serializer'a Kaydet
        serializer = KitapSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Kitap Kaydedildi: ",kitap_adi)
        else:
            continue
        



