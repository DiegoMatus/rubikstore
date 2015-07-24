from django.conf.urls import patterns, url, include

#Used to remove redundancy from URLconfs where a single pattern prefix is used repeatedly (Require from . import views)
#url(r'^checkout/', include([
#	 		url(r'^cart/$', 			views.shoppingcart_view,	name='shoppingcart'),
#			url(r'^shipping/$', 		views.shipping_view, 		name='shipping'),
#])),


urlpatterns = patterns('apps.shop.views',
                       url(r'^$', 								'index_view', 			name='index'),
                       url(r'^types/$', 						'types_view', 			name='types'),
                       url(r'^types/(?P<type>\w+)/$', 			'types_view',			name='types'),
                       url(r'^brands/$', 						'brands_view',		 	name='brands'),
                       url(r'^brands/(?P<brand>\w+)/$', 		'brands_view', 			name='brands'),
                       url(r'^accessories/$',					'accessories_view', 	name='accessories'),
                       url(r'^accessories/(?P<accessory>\w+)/$','accessories_view',		name='accessories'),
                       url(r'^details/(?P<product>\w+)/$', 		'details_view',		 	name='details'),
                       url(r'^checkout/cart/$', 				'shoppingcart_view',	name='shoppingcart'),
                       url(r'^checkout/shipping/$',				'shipping_view', 		name='shipping'),
                       url(r'^contact/$',						'contact_view', 		name='contact'),
                       )