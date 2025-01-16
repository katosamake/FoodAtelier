from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('home/', include('home.urls')),
    # path('__debug__/', include('debug_toolbar.urls')), # 開発環境のみ
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



