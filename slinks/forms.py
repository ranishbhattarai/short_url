from django import forms
from .models import ShortLink
# This is a Django form for creating a ShortLink

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'https://example.com/your-long-url'
            }),
        }
        labels = {
            'original_url': 'Enter URL to shorten'
        }

        
    