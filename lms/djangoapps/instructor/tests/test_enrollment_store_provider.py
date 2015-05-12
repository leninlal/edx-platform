"""
Exercises tests on the base_store_provider file
"""

from django.test import TestCase
from instructor.cybersource_enrollment_report import CyberSourceEnrollmentReportProvider
from instructor.enrollment_report_provider import EnrollmentReportProvider


class BadImplementationEnrollmentReportProvider(EnrollmentReportProvider):
    """
    Test implementation of EnrollmentProvider to assert that non-implementations of methods
    raises the correct methods
    """

    def get_user_profile(self, user_id):
        """
        Fake implementation of method which calls base class, which should throw NotImplementedError
        """
        super(BadImplementationEnrollmentReportProvider, self).get_user_profile(user_id)

    def get_enrollment_info(self, user, course_id):
        """
        Fake implementation of method which calls base class, which should throw NotImplementedError
        """
        super(BadImplementationEnrollmentReportProvider, self).get_enrollment_info(user, course_id)

    def get_payment_info(self, user, course_id):
        """
        Fake implementation of method which calls base class, which should throw NotImplementedError
        """
        super(BadImplementationEnrollmentReportProvider, self).get_payment_info(user, course_id)


class TestBaseNotificationDataProvider(TestCase):
    """
    Cover the EnrollmentReportProvider class
    """

    def test_cannot_create_instance(self):
        """
        EnrollmentReportProvider is an abstract class and we should not be able
        to create an instance of it
        """

        with self.assertRaises(TypeError):
            # parent of the BaseEnrollmentReportProvider is EnrollmentReportProvider
            super(BadImplementationEnrollmentReportProvider, self)

    def test_get_provider(self):
        """
        Makes sure we get an instance of the registered enrollment provider
        """

        provider = CyberSourceEnrollmentReportProvider()

        self.assertIsNotNone(provider)
        self.assertTrue(isinstance(provider, CyberSourceEnrollmentReportProvider))

    def test_base_methods_exceptions(self):
        """
        Asserts that all base-methods on the EnrollmentProvider interface will throw
        an NotImplementedError
        """

        bad_provider = BadImplementationEnrollmentReportProvider()

        with self.assertRaises(NotImplementedError):
            bad_provider.get_enrollment_info(None, None)

        with self.assertRaises(NotImplementedError):
            bad_provider.get_payment_info(None, None)

        with self.assertRaises(NotImplementedError):
            bad_provider.get_user_profile(None)