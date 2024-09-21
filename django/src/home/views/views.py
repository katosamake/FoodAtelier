from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = "home/index.html"

class RecordView(TemplateView):
    template_name = "home/record/record.html"

class DesideView(TemplateView):
    template_name = "home/deside/deside.html"

class WatchView(TemplateView):
    template_name = "home/watch/watch.html"