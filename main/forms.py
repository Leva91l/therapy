from django import forms


class CoopRequest(forms.Form):
    name = forms.CharField()
    e_mail = forms.CharField()
    phone = forms.CharField()
