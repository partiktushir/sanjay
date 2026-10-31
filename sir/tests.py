from django.core import mail
from django.test import TestCase
from django.test import override_settings
from django.urls import reverse

from .models import AdmissionApplication, SchoolSettings


class PublicPagesTests(TestCase):
    def test_public_pages_render_without_school_settings(self):
        page_names = (
            "home",
            "gallery",
            "result",
            "about",
            "admission",
            "admission_success",
            "facilities",
            "academics",
            "sports",
        )

        for page_name in page_names:
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))
                self.assertEqual(response.status_code, 200)

    def test_homepage_uses_configured_map_embed_url(self):
        map_embed_url = "https://maps.example.test/embed?place=school"
        SchoolSettings.objects.create(
            school_name="Test School",
            location_embed_url=map_embed_url,
        )

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'src="{map_embed_url}"')

    def test_shared_stylesheet_is_included_on_homepage(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/static/css/style.css"')

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        EMAIL_HOST_USER="noreply@example.test",
        ADMISSION_EMAIL="admissions@example.test",
    )
    def test_admission_submission_is_saved_and_emailed(self):
        response = self.client.post(
            reverse("admission"),
            {
                "student_name": "Test Student",
                "father_name": "Test Parent",
                "applying_class": "6th",
                "mobile": "9876543210",
                "address": "Test address",
            },
        )

        self.assertRedirects(response, reverse("admission_success"))
        application = AdmissionApplication.objects.get()
        self.assertEqual(application.application_number, "LRMP000001")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["admissions@example.test"])
