from django import forms


class RemoveUser(forms.Form):
    username = forms.CharField()


class DeleteCard(forms.Form):
    name = forms.CharField()
