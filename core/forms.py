from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactSubmission, APIRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Name')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your Email')}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Subject')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Your Message'), 'rows': 5}),
        }

class APIRequestForm(forms.ModelForm):
    class Meta:
        model = APIRequest
        fields = ['company_name', 'website', 'email', 'use_case', 'message']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Company Name')}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': _('Company Website')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Work Email')}),
            'use_case': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Primary Use Case')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Additional Details'), 'rows': 3}),
        }
        
    def clean_website(self):
        website = self.cleaned_data.get('website')

        if website and not website.startswith(('http://', 'https://')):
            website = 'https://' + website

        return website
        
