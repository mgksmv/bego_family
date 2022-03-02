from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = 'inner_life/gallery/gallery.html'


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery
    template_name = 'inner_life/gallery/gallery_detail.html'
