import imp
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.registration,name='index'),
    path('qrcode/',views.qr_code,name='qrcode'),
    path('',views.homepage,name='homepage'),
    path('userlist/',views.fun_image,name='userlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns + staticfiles_urlpatterns()