from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


from . import views

urlpatterns = [
    # ex: /credits/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^account_id/(?P<pk>[0-9]+)/$', views.AccountDetailURL.as_view(), name="account_details2" ),
    url(r'^account-details/$', views.account_details, name='account_details'),
    url(r'^user-trade/$', views.user_trade, name='user-trade'),
    url(r'^user-grant/$', views.user_grant, name='user-grant'),

]

urlpatterns += staticfiles_urlpatterns()
