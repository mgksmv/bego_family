from django.urls import path

from .views import GalleryListView, GalleryDetailView

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', GalleryDetailView.as_view(), name='gallery_detail'),
]
