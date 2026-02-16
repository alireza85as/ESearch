from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm, APIRequestForm
from .models import ContactSubmission, APIRequest
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class DocsPageView(TemplateView):
    template_name = "docs.html"

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'contact_form' not in context:
            context['contact_form'] = ContactForm()
        if 'api_form' not in context:
            context['api_form'] = APIRequestForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        
        if 'submit_contact' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, _("Your message has been sent successfully!"))
                return redirect('contact')
            else:
                context['contact_form'] = contact_form
                messages.error(request, _("Please correct the errors in the contact form."))

        elif 'submit_api' in request.POST:
            api_form = APIRequestForm(request.POST)
            if api_form.is_valid():
                api_form.save()
                messages.success(request, _("Your API request has been submitted. We will contact you soon."))
                return redirect('contact')
            else:
                context['api_form'] = api_form
                messages.error(request, _("Please correct the errors in the API request form."))
        
        return self.render_to_response(context)

from django.urls import translate_url
from django.utils.http import url_has_allowed_host_and_scheme

import re

def change_language(request):
    language = request.GET.get('lang')
    referer = request.META.get('HTTP_REFERER')
    
    if not referer:
        referer = '/'
    
    # Ensure the referer is safe
    if not url_has_allowed_host_and_scheme(url=referer, allowed_hosts={request.get_host()}):
        referer = '/'

    response = HttpResponseRedirect(referer)

    if language and language in [l[0] for l in settings.LANGUAGES]:
        translation.activate(language)
        
        # Set persistent cookie
        cookie_name = getattr(settings, 'LANGUAGE_COOKIE_NAME', 'django_language')
        response.set_cookie(cookie_name, language)
        
        # Manually redirect to the new language URL
        from urllib.parse import urlparse
        path = urlparse(referer).path
        
        # Check for language prefix in path (e.g., /en/about/ or /fa/about/)
        match = re.match(r'^/([a-z]{2})(/.*|$)', path)
        if match:
            current_prefix = match.group(1)
            if current_prefix in [l[0] for l in settings.LANGUAGES]:
                # Replace the language prefix with the selected language
                new_path = f"/{language}{match.group(2)}"
                response = HttpResponseRedirect(new_path)
                response.set_cookie(cookie_name, language)
        elif path == '/':
             # Special case for root if it wasn't prefixed (unlikely with i18n_patterns default)
             new_path = f"/{language}/"
             response = HttpResponseRedirect(new_path)
             response.set_cookie(cookie_name, language)

    return response
