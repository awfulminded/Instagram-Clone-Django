from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Api methods
    path('signin_user', signin_user),
    path('signup_user', signup_user),
    path('update_pic', update_pic),

    # Auth urls
    path('signin', signin_view, name='signin_url'),
    path('signup', signup_view, name='signup_url'),

    # Website urls
    path('home', home_view, name='home_url'),
    path('<user_page>', profile_page, name='profile_url'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
