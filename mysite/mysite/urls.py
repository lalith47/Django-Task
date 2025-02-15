"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from Profile import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as v
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Django API')

urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Django API')),
    path('swagger-docs/', schema_view),
    path('api-token-auth/',v.obtain_auth_token,name='api-token-auth'),
    url(r'^profile/$', views.UserData.as_view()),
    url(r'^profile/(?P<email_id>[\w\@\-\.]+)$', views.UserDetails.as_view()),
    url(r'^otherprofile/(?P<email_id>[\w\@\-\.]+)$', views.OtherUserDetails.as_view()),
    url(r'^listotherprofile/$', views.ListOtherUserDetails.as_view()),
    url(r'^addfriend/(?P<email_id>[\w\@\-\.]+)$$', views.AddFriend.as_view()),
    url(r'^removefriend/(?P<email_id>[\w\@\-\.]+)$$', views.RemoveFriend.as_view()),
    url(r'^registeruser/$', views.RegisterUser.as_view()),
    # path('profile/<int:pk>/', views.user_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
