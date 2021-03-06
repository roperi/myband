from django.test import TestCase
from django.core.urlresolvers import reverse

from .factories import GigFactory, UpcomingGigFactory, PastGigFactory


class GigTestCase(TestCase):

    def setUp(self):
        self.draft_gigs = GigFactory.create_batch(5)
        self.upcoming_gigs = UpcomingGigFactory.create_batch(5)
        self.past_gigs = PastGigFactory.create_batch(5)

    def test_list_returns_published_gigs(self):
        published_gigs = set(self.upcoming_gigs + self.past_gigs)

        response = self.client.get(reverse('gig_list'))
        gig_list = response.context['gig_list']

        self.assertEqual(set(gig_list), published_gigs)

    def test_list_uses_template(self):
        response = self.client.get(reverse('gig_list'))
        self.assertTemplateUsed(response, 'shows/gig_list.html')
