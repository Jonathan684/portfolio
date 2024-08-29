# file_exists.py
from django import template
from django.conf import settings
import os

register = template.Library()

@register.filter
def file_exists(filepath):
    full_path = os.path.join(settings.STATIC_ROOT, filepath)
    return os.path.exists(full_path)
