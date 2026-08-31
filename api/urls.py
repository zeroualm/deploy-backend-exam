from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('task', TaskViewSet, basename='task')

urlpatterns = router.urls
