from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super(Co, self).__init__(*args, **kwargs)
    #     # self.name.widget.attrs.update({'class': 'form-control'})
    #     # self.fields['name'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ('name', 'email', 'body')
        labels = {
            'name': 'Имя',
            'email': 'E-mail',
            'body': 'Сообщение',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }




