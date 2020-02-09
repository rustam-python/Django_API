from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

# Add API URLs
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    # we don't want to add the prefix to this URL - just add all URLs from the router URLs.
    path('', include(router.urls))
]
