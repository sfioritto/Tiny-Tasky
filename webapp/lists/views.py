from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext 
from webapp.forms import ListForm
from app.model import lists


@login_required
def show_lists(request):
    return render_to_response('lists/lists.html',
                              context_instance=RequestContext(request))


@login_required
def show_list(request, key):
    return render_to_response('lists/list.html',
                              context_instance=RequestContext(request))


@login_required
def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['listname']
            print request.user
            account = request.user.get_profile()
            lists.create(name, account.id)
            return HttpResponseRedirect(reverse('webapp.lists.views.show_list', args=[name]))
        else:
            return render_to_response('lists/create.html', {
                    'form' : form,
                    }, context_instance = RequestContext(request))
    else:
        return render_to_response('lists/create.html', {
                'form' : ListForm(),
                }, context_instance = RequestContext(request))

    


