# coding=utf-8
from django import forms
from qq_forum.articles.models import Article

class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255, label='标题')
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),
        max_length=4000, label='内容')
    tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255,
        required=False,
        help_text='按空格可以添加标签，例如 "音乐 学习 体育"',
        label="标签")

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'status']
