import os
import django
import random
from planner.models import *
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Event_planner.settings')

django.setup()

fakegen = Faker()


def add_entry():
    e = ResourceList.objects.get_or_create(title=random.choice("title"))[0]
    e.save()
    return e
