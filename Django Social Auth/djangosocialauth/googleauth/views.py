from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User

# Create your views here.
def app_home(request):
    return render(request, 'login.html')

def google_login(request):
    current_user = request.user
    if(current_user):
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

    # var="Google Login Redirect Here, Bilal"
    # return HttpResponse(str(var))

# Create your views here.
def simple_signup(request):
  return render(request, 'signup.html')

def emailvarification(request):
	if request.is_ajax() and request.method == "POST":
		email = request.POST.get('email')
		return HttpResponse(json.dumps({'email': email}), content_type="application/json")
	else:
		return render_to_response('signup.html', locals())

def dictionary(request):
    print(request.GET.get('nameofinputfield', 'if notfounddefaulttext'))
    mydata=request.GET.get('nameofinputfield', 'if notfounddefaulttext')
    myname={'name':'Bilal', 'last_name':'Hameed'}
    return render(request, 'home.html' , myname)