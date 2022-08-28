import os
from django.contrib.auth import get_user_model

UserModel = get_user_model()

if not UserModel.objects.filter(username=os.getenv('DJANGO_SUPER_USER')).exists():
    user=UserModel.objects.create_user(os.getenv('DJANGO_SUPER_USER'), password=os.getenv('DJANGO_SUPER_USER_PASS'))
    user.is_superuser=True
    user.is_staff=True
    user.save()
