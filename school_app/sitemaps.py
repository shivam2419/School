from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['index', 'about', 'Gallery', 'contact']  # These must match name='' in urls.py

    def location(self, item):
        return reverse(item)
