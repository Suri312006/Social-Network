# -*- coding: utf-8 -*-

import django
import os
import sys
from datetime import timedelta
from django.utils import timezone
from collections import Counter

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..' ))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'wey_backend.settings')
django.setup()


from post.models import Post, Trend

for trend in Trend.objects.all():
    trend.delete()

def extract_hashtags(text, trends):
    for word in text.split():
        if word[0] == '#':
            trends.append(word[1:])

    return trends


this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
twenty_four_hours_before = this_hour - timedelta(hours = 24)

posts = Post.objects.filter(created_at__gte=(twenty_four_hours_before))
trends = []


for post in posts:
    extract_hashtags(post.body, trends)

for trend in Counter(trends).most_common(10):
    Trend.objects.create(hashtag=trend[0], occurrences=trend[1])


for trend in Trend.objects.all():
    print(trend.hashtag)