from django.contrib.sitemaps import Sitemap
from news.models import News

class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return News.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date