import logging

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from wger.core.tests.base_testcase import WorkoutManagerTestCase

logger = logging.getLogger(__name__)


class TestDeactivateUserTestCase(WorkoutManagerTestCase):
    """
    Test deactivate and activate user account
    """

    def test_deactivate_user(self, fail=False):
        """
        Helper function to test activate and deactivate the user
        :param fail:
        :return:
        """
        self.user_login()
        user = User.objects.get(username=self.current_user)
        response = self.client.get(reverse('core:user:deactivate', kwargs=dict(pk=user.id)))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(user.is_active) if fail else self.assertTrue(user.is_active)

        # Test activate user
        response = self.client.get(reverse('core:user:activate', kwargs=dict(pk=user.id)))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(user.is_active) if fail else self.assertTrue(user.is_active)
