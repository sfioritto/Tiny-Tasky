import pytyrant
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


def lists(request):
    return render_to_response('lists/lists.txt',
                              context_instance=RequestContext(request))


@login_required
def list(request, key):
    return render_to_response('lists/list.txt',
                              context_instance=RequestContext(request))



