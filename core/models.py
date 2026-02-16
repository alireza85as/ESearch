from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactSubmission(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=255, blank=True)
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Contact Submission")
        verbose_name_plural = _("Contact Submissions")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"

class APIRequest(models.Model):
    company_name = models.CharField(_("Company Name"), max_length=255)
    website = models.URLField(_("Website"), blank=True)
    email = models.EmailField(_("Work Email"))
    use_case = models.CharField(_("Use Case"), max_length=255)
    message = models.TextField(_("Additional Details"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(_("Approved"), default=False)

    class Meta:
        verbose_name = _("API Request")
        verbose_name_plural = _("API Requests")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.use_case}"
