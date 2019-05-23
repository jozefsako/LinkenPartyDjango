from django.test import TestCase
from .models import Events

class TestCase(TestCase):

    def setUp(self):
        self.author = User.objects.create(
          username='author@test.com',
          email='author@test.com',
          user_type=User.AUTHOR
        )
        self.publisher = User.objects.create(
          username='publisher@test.com',
          email='publisher@test.com',
          user_type=User.AUTHOR
        )

    def test_get_authors(self):
      self.assertEqual(User.get_authors(), 1)

    def test_can_write_books(self):
      self.assertTrue(self.author.can_write_books())
      self.assertFalse(self.publisher.can_write_books())




class EventsTestCase(TestCase):

    def setUp(self):
        self.event1 = Events.objects.create(
            id_user=2,
            creation_date="2019-06-02T00=00=00Z",
            address_event="Rue Antoine Dansaert 6, 1000",
            size_hosting=40,
            state_event="Confirmed",
            description_event="Anniversaire de Dj Khalid - hosted by Loury Jacob",
            type_event="party",
            version_number=0,
            name_event="DJ KHALID EVENT",
            theme_event="RAP-FR",
            email='author@test.com',
        )

    def test_get_id_user(self):
      self.assertEqual(Events.get_id_user(), 2)

    def test_can_write_books(self):
      self.assertTrue(self.author.can_write_books())
      self.assertFalse(self.publisher.can_write_books())
