from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        label="제목",
        widget=forms.TextInput(
            attrs={
                "class": "my-title",
                "placeholder": "Enter the title!",
            }
        ),
    )
    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                "class": "my-content",
                "placeholder": "Enter the content!",
                "rows": 5,
                "cols": 50,
            }
        ),
    )
    image = forms.ImageField(
        label="사진",
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "my-image",
            }
        ),
    )

    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "image",
        )


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label="제목",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "my-title",
#                 "placeholder": "Enter the title!",
#             }
#         ),
#     )
#     content = forms.CharField(
#         label="내용",
#         widget=forms.Textarea(
#             attrs={
#                 "class": "my-content",
#                 "placeholder": "Enter the content!",
#                 "rows": 5,
#                 "cols": 50,
#             }
#         ),
#     )
#     image = forms.ImageField(
#         label="사진",
#         required=False,
#         widget=forms.FileInput(
#             attrs={
#                 "class": "my-image",
#             }
#         ),
#     )
