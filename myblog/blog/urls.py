from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from blog.views import *

app_name = '[blog]'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$',get_blogs,name='get_blogs'),
    url(r'^detail/(\d+)/$',get_details,name='blog_get_detail'),
    path(r'delete/',DeleteBlogView.as_view(),name='blogdelte'),
]
