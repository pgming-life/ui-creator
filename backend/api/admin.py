from django.contrib import admin
from .models import BaseModel

# register the BaseModel with admin
admin.site.register(BaseModel)
