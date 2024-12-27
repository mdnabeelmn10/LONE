from django import forms
from .models import QuestionnaireResponse

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
                  'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18']
        widgets = {
            'q1': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q2': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q3': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q4': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q5': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q6': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q7': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q8': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q9': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q10': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q11': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q12': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q13': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q14': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q15': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q16': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q17': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
            'q18': forms.Select(choices=[(0, 'Not at all'), (1, 'Several days'), (2, 'More than half the days'), (3, 'Nearly every day')]),
        }