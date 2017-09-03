# this code is all pulled from the decorators part of the django-annoying extension

from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.db.models import signals as signalmodule
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

try: import json
except ImportError: import simplejson as json

__all__ = ['template', 'ajax']

try:
    from functools import wraps
except ImportError:
    def wraps(wrapped, assigned=('__module__', '__name__', '__doc__'),
              updated=('__dict__',)):
        def inner(wrapper):
            for attr in assigned:
                setattr(wrapper, attr, getattr(wrapped, attr))
            for attr in updated:
                getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
            return wrapper
        return inner


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """

    def __init__(self, data):
        super(JsonResponse, self).__init__(content=json.dumps(data, default=lambda o: o.__dict__),
                                           mimetype='application/json',
                                           )
        self['Access-Control-Allow-Origin'] = "*"
        self['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'


def template(template=None):
    """
    Decorator for Django views that sends returned dict to render_to_response function.

    Template name can be decorator parameter or TEMPLATE item in returned dictionary.
    RequestContext always added as context instance.
    If view doesn't return dict then decorator simply returns output.

    Parameters:
     - template: template name to use

    Examples:
    # 1. Template name in decorator parameters

    @template('template.html')
    def foo(request):
        bar = Bar.object.all()
        return {'bar': bar}

    # equals to
    def foo(request):
        bar = Bar.object.all()
        return render_to_response('template.html',
                                  {'bar': bar},
                                  context_instance=RequestContext(request))


    # 2. Template name as TEMPLATE item value in return dictionary

    @template()
    def foo(request, category):
        template_name = '%s.html' % category
        return {'bar': bar, 'TEMPLATE': template_name}

    #equals to
    def foo(request, category):
        template_name = '%s.html' % category
        return render_to_response(template_name,
                                  {'bar': bar},
                                  context_instance=RequestContext(request))

    """

    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            tmpl = output.pop('TEMPLATE', template)

            response = render(request, tmpl, output)

            # response = render_to_response(tmpl, output, context_instance=RequestContext(request))
            response['X-FRAME-OPTIONS'] = 'DENY'
            return response

        return wrapper

    return renderer


def ajax(func):
    """
    If view returned serializable dict, returns JsonResponse with this dict as content.

    example:

        @ajax
        def my_view(request):
            news = News.objects.all()
            news_titles = [entry.title for entry in news]
            return {'news_titles': news_titles}
    """

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, dict):
            return JsonResponse(response)
        else:
            return response

    return wrapper

