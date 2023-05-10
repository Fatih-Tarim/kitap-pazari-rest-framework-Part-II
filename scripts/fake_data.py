import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')
# os.environ["DJANGO_SETTINGS_MODULE"] = "kitap_pazari.settings"

import django
django.setup()
## Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız lazım
## SIRALAMA ÇOK ÖNEMLİ

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
        email = email
    )
    user.set_password('testing321..')
    user.save()

for i in range(1,20):
    set_user()