from django import forms

class HashForm(forms.Form):
    # Using Textarea because some people enters lots of things here, like a paragraph
    text = forms.CharField(label='Enter hash here:', widget=forms.Textarea)