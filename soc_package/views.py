from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SocPackage


class SocPackageDetailView(LoginRequiredMixin, DetailView):
    model = SocPackage
    template_name = 'detailview_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.image_set.all()
        context['videos'] = self.object.video_set.all()
        context['pdfs'] = self.object.pdf_set.all()
        return context
