from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def index_view(request):
    return render_to_response('index.html')#, context_instance=RequestContext(request))

def types_view(request, type=''):
	return render_to_response('shop.html')#, context_instance=RequestContext(request))

def brands_view(request, brand=''):
	return render_to_response('shop.html')#, context_instance=RequestContext(request))

def accessories_view(request, accessory=''):
	return render_to_response('shop.html')#, context_instance=RequestContext(request))

def details_view(request, product):
	return render_to_response('details.html')#, context_instance=RequestContext(request))

def shoppingcart_view(request):
	return render_to_response('shoppingcart.html')#, context_instance=RequestContext(request))

def shipping_view(request):
	return render_to_response('shipping.html')#, context_instance=RequestContext(request))

def contact_view(request):
	return render_to_response('contact.html')#, context_instance=RequestContext(request))