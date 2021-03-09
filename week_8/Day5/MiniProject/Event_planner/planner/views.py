from django.shortcuts import render
from .forms import ResourceForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from planner.models import *
# Create your views here.

shopList = [
    {
        'item': 'banana',
        'description': 'for smoothies'
    },
    {
        'item': 'red solo cups',
        'description': 'for beerpong'
    }
]


def home(request):
    title = 'Event planner - Home'
    return render(request, 'base.html')


# class ResourceCreateView(CreateView):
#     template_name = 'components/creation.html'
#     form_class = ResourceForm
#     success_url = reverse_lazy("new-entry")
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.author = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())


def list_view(request):
    context = {
        'ShoppingList': shopList,
        'title': 'Shopping List'
    }
    return render(request, 'components/resources.html', context)


def resource_creation(request):
    return render(request, 'components/creation.html')


def guest_list(request):
    return render(request, 'components/guests.html', {'title': 'Guests'})


def location_picker(request):
    return render(request, 'components/location.html', {'title': 'Locations'})


def theme_picker(request):
    return render(request, 'components/theme.html', {'title': 'Themes'})