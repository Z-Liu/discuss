from django import forms

from links.models import Comment


class CommentModelForm(forms.ModelForm):
    link_pk = forms.IntegerField(wiget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('body',)
