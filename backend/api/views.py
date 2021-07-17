from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from .models import BaseModel, BaseSerializer

# Vue application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class MessageViewSet(viewsets.ModelViewSet):
    queryset = BaseModel.objects.all()
    serializer_class = BaseSerializer
    