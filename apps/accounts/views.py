from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def account_view(request):
    return render_to_response('account.html', context=RequestContext(request))

def login_view(request):
	return render_to_response('login.html', context=RequestContext(request))

def register_view(request):
	return render_to_response('register.html', context=RequestContext(request))

def logout_view(request):
	return render_to_response('logout.html', context=RequestContext(request))

def wishlist_view(request):
	return render_to_response('wishlist.html', context=RequestContext(request))

def orders_view(request):
	return render_to_response('orders.html', context=RequestContext(request))

def edit_view(request):
	return render_to_response('edit.html', context=RequestContext(request))

def credit_cards_view(request):
	return render_to_response('credit_cards.html', context=RequestContext(request))

def forgot_password_view(request):
	return render_to_response('forgot_password.html', context=RequestContext(request))