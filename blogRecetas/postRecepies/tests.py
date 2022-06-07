from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class TestRecepies(TestCase):
    def test_str(self):
        post = Post(title='My first post', author=User(username='test', email='test@test.com'))
        self.assertEqual(str(post), 'My first post - test')

    def test_get_absolute_url(self):
        post = Post(title='My first post')
        self.assertIsNotNone(post.get_absolute_url())

    def test_get_absolute_url_is_not_none(self):
        post = Post(title='My first post')
        self.assertIsNotNone(post.get_absolute_url())
    
