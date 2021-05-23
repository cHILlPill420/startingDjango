from django import forms
class FormNorm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput)
    
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("Found bot")
        return botcatcher