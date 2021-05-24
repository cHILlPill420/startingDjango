from django import forms
from django.core import validators

#custom validator

def check_name(value):
    if value[0] == '0' or value[0] == '1' or value[0] == '2' or value[0] == '3' or value[0] == '4' or value[0] == '5' or value[0] == '6' or value[0] == '7' or value[0] == '8' or value[0] == '9':
        raise forms.ValidationError("name shouldn't start with numbers")

class FormNorm(forms.Form):
    name = forms.CharField(validators=[check_name])
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])
    # validators did all of following
    #cleaned method
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Found bot")
    #     return botcatcher