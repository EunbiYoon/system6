from django import forms
from report.models import Comment

class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Comment
        fields = ('comment_body',)