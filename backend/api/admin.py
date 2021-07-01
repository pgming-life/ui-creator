from django.contrib import admin
from .models import BaseModel

# ベースモデルをadminに登録
admin.site.register(BaseModel)
