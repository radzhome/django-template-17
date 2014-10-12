from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, patterns
from django.contrib import admin
from django.template.response import TemplateResponse

admin.autodiscover()


urlpatterns = patterns('',
    (r'', include('home.urls')),
    (r'^cmsadmin/', include(admin.site.urls)),
    # (r'^foo-app/', include('foo_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', TemplateResponse, {'template': '404.html'}))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
