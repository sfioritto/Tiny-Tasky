from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext 
from webapp.forms import ListForm, TaskForm
from webapp.lists.models import List
from app.model import lists


@login_required
def show_lists(request):
    account = request.user.get_profile()
    
    return render_to_response('lists/lists.html', {
            'lists' : account.list_set.all()
            }, context_instance=RequestContext(request))


@login_required
def show_list(request, name):

    account = request.user.get_profile()
    lst = lists.get_list(name, account)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            lst.add_task(text)
            return HttpResponseRedirect(reverse('webapp.lists.views.show_list', args=[name]))
        else:
            return render_to_response('lists/list.html', {
                    'form' : form,
                    'lst' : lst,
                    }, context_instance = RequestContext(request))
    else:
        return render_to_response('lists/list.html', {
                'form' : TaskForm(),
                'lst' : lst,
                }, context_instance = RequestContext(request))


@login_required
def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['listname']
            account = request.user.get_profile()
            lists.create(name, account)
            return HttpResponseRedirect(reverse('webapp.lists.views.show_list', args=[name]))
        else:
            return render_to_response('lists/create.html', {
                    'form' : form,
                    }, context_instance = RequestContext(request))
    else:
        return render_to_response('lists/create.html', {
                'form' : ListForm(),
                }, context_instance = RequestContext(request))

    
