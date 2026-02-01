from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import ShortLink

"""Django form for creating a ShortLink"""
class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url', 'expires_at']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'https://example.com/your-long-url'
            }),
            'expires_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }
        labels = {
            'original_url': 'Enter URL to shorten',
            'expires_at': 'Expiration date (optional)'
        }

    def clean_expires_at(self):
        value = self.cleaned_data.get('expires_at')
        if value and value <= timezone.localdate():
            raise ValidationError('Expiration date must be in the future.')
        return value

