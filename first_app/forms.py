from django import forms
class FormNorm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)
    