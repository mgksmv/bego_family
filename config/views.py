from itertools import chain

from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from regulations.models import Reglament, Penalty, Bonus
from bego.models import History, Mission, OrgStructure


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


@login_required
def search(request):
    reglaments = None

    if 'keyword' in request.GET:
        query = request.GET.get('keyword')
        if query:
            reglaments = Reglament.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'reglaments_search': reglaments})


class SearchListView(LoginRequiredMixin, ListView):
    template_name = 'search.html'
    paginate_by = 20

    def get_queryset(self):
        reglaments = None
        history = None
        mission = None
        org_structure = None
        penalty = None
        bonus = None

        if 'keyword' in self.request.GET and self.request.GET.get('keyword'):
            query = self.request.GET.get('keyword')
            if query:
                reglaments = Reglament.objects.filter(name__icontains=query)
                history = History.objects.filter(name__icontains=query)
                mission = Mission.objects.filter(name__icontains=query)
                org_structure = OrgStructure.objects.filter(name__icontains=query)
                penalty = Penalty.objects.filter(name__icontains=query)
                bonus = Bonus.objects.filter(name__icontains=query)

            object_list = list(chain(
                reglaments, history, mission, org_structure, penalty, bonus
            ))
            return object_list
        return None

    def get_context_data(self, **kwargs):
        if self.get_queryset():
            context = super().get_context_data(**kwargs)

            paginator = Paginator(self.get_queryset(), self.paginate_by)
            page = self.request.GET.get('page')

            try:
                object_list_paginated = paginator.page(page)
            except PageNotAnInteger:
                object_list_paginated = paginator.page(1)
            except EmptyPage:
                object_list_paginated = paginator.page(paginator.num_pages)

            print(object_list_paginated.has_next())

            context['object_list'] = object_list_paginated
            return context
