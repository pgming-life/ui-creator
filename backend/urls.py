from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.views import index_view, MessageViewSet

# ルーター設定
router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

# URLパターン
urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),             # PROCESS
    path('workspace/', index_view, name='index'),   # WORKSPACE
    path('profile/', index_view, name='index'),     # PROFILE

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]
