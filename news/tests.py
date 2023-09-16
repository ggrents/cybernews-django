from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, reverse_lazy, resolve
from news import views
from users.views import *


class TestUrls(TestCase):
    def test_news_mainpage(self):
        url = reverse('main-page')
        self.assertEquals(resolve(url).func.view_class, views.show_article)

    def test_news_article_detail(self):
        article_id = 23
        url = reverse('full-article', args=[article_id])
        self.assertEquals(resolve(url).func, views.article_detail)

    def test_news_catonly_c(self):
        slug = 'cs'
        url = reverse('category-only', args=[slug])
        self.assertEquals(resolve(url).func, views.show_only_category)

    def test_news_catonly_d(self):
        slug = 'dota'
        url = reverse('category-only', args=[slug])
        self.assertEquals(resolve(url).func, views.show_only_category)

    def test_news_add_article(self):
        url = reverse('addart')
        self.assertEquals(resolve(url).func, views.addart)

    def test_news_show_by_tag(self):
        url = reverse('tag_search', args=['secret'])
        self.assertEquals(resolve(url).func, views.show_article_byTags)
        client = Client()
        resp = client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_news_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, views.Search)

    def test_user_profile(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, views.UserProfile)


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_news_main_page(self):
        url = reverse('main-page')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_news_add_article(self):
        url = reverse('addart')
        client = Client()
        resp = client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'addart.html')

    def test_news_search(self):
        url = reverse('search')
        client = Client()
        resp = client.get(url)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'search.html')
