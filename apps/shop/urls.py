from django.conf.urls import patterns, url

urlpatterns = patterns('apps.shop.views',
                       url(r'^$', 'index_view', name='index'),
                       )
