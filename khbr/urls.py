from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analytics.urls')),
    path('events/', include('event.urls')),
    path('videooverviews/', include('videooverview.urls')),
    path('raitings/', include('raitings.urls')),
    #path('user/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'analytics.views.not_found_view'
handler500 = 'analytics.views.error_view'
handler403 = 'analytics.views.permission_denied_view'
handler400 = 'analytics.views.bad_request_view'