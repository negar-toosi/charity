from django.contrib.syndication.views import Feed
from django.urls import reverse
from news.models import News

class LatestEntriesFeed(Feed):
    title = "newest news"
    link = "/rss/feed"
    description = "best news ever"

    def items(self):
        return News.objects.filter(status=True) 

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]