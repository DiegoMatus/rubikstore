from django.conf.urls import patterns, url

urlpatterns = patterns('apps.shop.views',
                       url(r'^$', 							'index_view', 			name='index'),
                       url(r'^(?P<filter>\w+)/', 			'shop_view', 			name='shop'),
                       url(r'^details/(?P<product>\w+)/', 	'single_product_view', 	name='single_product'),
                       url(r'^shoppingcart/', 				'cart_view', 			name='cart'),
                       url(r'^checkout/', 					'checkout_view', 		name='checkout'),
                       )
