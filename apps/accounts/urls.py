from django.conf.urls import patterns, url

urlpatterns = patterns('apps.accounts.views',
                       url(r'^$', 					'account_view', 		name="account"),
                       url(r'^login/$', 			'login_view', 			name="login"),
                       url(r'^register/$', 			'register_view', 		name="register"),
                       url(r'^logout/$', 			'logout_view', 			name="logout"),
                       url(r'^wishlist/$', 			'wishlist_view', 		name="wishlist"),
                       url(r'^orders/$', 			'orders_view', 			name="orders"),
                       url(r'^edit/$', 				'edit_view', 			name="edit"),
                       url(r'^credit_cards/$', 		'credit_cards_view', 	name="credit_cards"),
                       url(r'^forgot_password/$', 	'forgot_password_view', name="forgot_password"),
                       )