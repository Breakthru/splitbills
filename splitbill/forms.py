from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

class AddTagForm(forms.Form):
    transaction = forms.IntegerField()
    tag_name = forms.CharField()
