from django import forms

from .models import *

class CommMessageForm(forms.ModelForm):
    class Meta:
        model=CommMessages
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={
            'class':'w-full py-4 rounded-xl border'
            })
        }

