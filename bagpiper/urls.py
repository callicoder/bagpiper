"""bagpiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers
from bagpiper.views import IndexView
from users.views import UserViewSet, LoginView, LogoutView
from coupons.views import CouponViewSet
from referral import views

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'coupons', CouponViewSet)
users_router = routers.NestedSimpleRouter(
    router, r'users', lookup='user'
)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(users_router.urls)),
    url(r'^api/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/referral/(?P<pk>[0-9A-Z]+)/verify/$', views.verify_referral),
	url('^.*$', IndexView.as_view(), name='index'),
]
