import pytyrant
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


@login_required
def lists(request):
    pass


@login_required
def list(request, key):
    pass


