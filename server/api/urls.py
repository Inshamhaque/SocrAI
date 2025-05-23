from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'profile', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
]