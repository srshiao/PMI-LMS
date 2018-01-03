from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import logout
from clockin.config import *


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/clockin/')

#@login_required
def adminhome(request):
	#if not request.user.is_superuser:
	#	return HttpResponseRedirect('/home/')
	context = {
		'period' : PERIOD
	}
	return render(request, 'timesheet/admin_home.html', context)
