

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap
from .views import robots_txt, pageNotFound

sitemaps = {'products': StaticSitemap, }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cart/', include('cart.urls')),
    path('catalog/', include('catalog.urls')),
    path('gallery/', include('gallery.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
