# coding=utf-8
from __future__ import unicode_literals
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView


def home_page(request, * args, **kwargs):
    """View function for our home page."""
    foo = 'garbanzo beans'
    return render(request, 'home.html', context={'foo': foo})


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        foo = 'garbanzo beans'
        return {'foo': foo}
