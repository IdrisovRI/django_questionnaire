from django import forms
from question.models import Survey, Question, Response
from question.constants import QUESTION_TYPES


class SurveyForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    end_date = forms.DateField()
    description = forms.CharField(max_length=255)

    class Meta:
        model = Survey
        exclude = ('create_date',)
        # fields = ('name', 'end_date', 'description')


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        survey_id = args[0]['survey']
        self.text = forms.CharField(max_length=255)
        self.type = forms.Select(choices=QUESTION_TYPES)
        self.survey = forms.ModelChoiceField(queryset=Survey.objects.filter(id=survey_id))

    class Meta:
        model = Question
        fields = ('survey', 'text', 'type')


class ResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)

        question_id = args[0]['question']
        self.person_id = forms.CharField(max_length=100)
        self.answer = forms.CharField(max_length=255)
        self.question = forms.ModelChoiceField(queryset=Question.objects.filter(id=question_id))

    class Meta:
        model = Response
        fields = ('person_id', 'answer', 'question')
