from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.model import lists
from webapp.forms import AccountForm

#Django hack to let us put emails in the username field in the login form
AuthenticationForm.base_fields['username'].max_length = 75 

def create(request):
    
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            #don't put email in django user object, already
            #stored in the account object.
            user = User.objects.create_user(username, '', password)
            user.save()
            acc = lists.create_account(email)

            acc.user = user
            acc.save()
            
            user = authenticate(username=user.username, password=password)
            login(request, user)

            return HttpResponseRedirect(reverse('webapp.lists.views.lists'))
        else:
            return render_to_response('account/create-user.html', {
                    'form' : form,
                    }, context_instance = RequestContext(request))
    else:

        return render_to_response('account/create-user.html', {
                'form' : AccountForm(),
                }, context_instance = RequestContext(request))




