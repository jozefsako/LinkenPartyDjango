from django.test import TestCase
# from django.urls import reverse
# from .models import Post

# Create your tests here.


class PostTests(TestCase):

    # def setUp(self):
    #     Post.objects.create(text='just a test')

    # def test_post_list_view(self):
    #     response = self.client.get(reverse('posts'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'just a test')
    #     self.assertTemplateUsed(response, 'posts.html')

    def hello(name):
        return 'Hello ' + 'name'

    def test_hello():
        assert hello('name') == 'Hello name'