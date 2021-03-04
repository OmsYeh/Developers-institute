from django.shortcuts import render
from .forms import ResourceForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
# Create your views here.


def home(request):
    return render(request, 'base.html')


class ResourceCreationView(CreateView):
    template_name = 'planner/resources.html'
    form_class = ResourceForm
    success_url = reverse_lazy("resources")

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.author = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


def list_view(request):
    return render(request, 'components/resources.html')


def resource_creation(request):
    return render(request, 'components/resource_creation.html')


def guest_list(request):
    return render(request, 'components/guests.html')


def location_picker(request):
    return render(request, 'components/location.html')


def theme_picker(request):
    return render(request, 'components/theme.html')