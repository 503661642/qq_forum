# coding=utf-8
from django import forms
from qq_forum.questions.models import Question, Answer

class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255, label="标题")
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),
        max_length=2000, label="内容")
    tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255,
        required=False,
        help_text='按空格可以添加标签，例如 "音乐 学习 运动"',
        label="标签")

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']

class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Question.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}),
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']
