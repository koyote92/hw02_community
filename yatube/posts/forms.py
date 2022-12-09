from django import forms
from .models import Post

"""Код ниже в процессе разработки."""


class PostEditionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

        def clean_text(self):
            data = self.cleaned_data['text']
            if len(data) < 11:
                raise forms.ValidationError('Текст поста не может быть короче '
                                            '10 символов.')
            return data


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

        def clean_text(self):
            data = self.cleaned_data['text']
            if len(data) < 11:
                raise forms.ValidationError('Текст поста не может быть короче '
                                            '10 символов.')
            return data
