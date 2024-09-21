from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('home/', include('home.urls')),
    # path('__debug__/', include('debug_toolbar.urls')), # 開発環境のみ
]



