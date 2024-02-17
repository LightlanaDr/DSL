from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['cart_detail', 'category_products', 'gallery', 'delivery']

    def location(self, item):
        return reverse(item)