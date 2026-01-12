from django.contrib import sitemaps
from django.urls import reverse

class TiendaViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['tienda',]

    def location(self, item):
        return reverse(item)
