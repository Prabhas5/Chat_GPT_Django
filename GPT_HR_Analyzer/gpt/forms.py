
from django import forms
from .models import CandidateResponse

class CandidateResponseForm(forms.ModelForm):
    class Meta:
        model = CandidateResponse
        fields = '__all__'
        labels = {
            'position_applied': 'Position Applied',
            'about_myself': 'About Myself',
            'experience': 'Experience',
            'experience_years': 'Years of Experience',
            'ans1': 'Q1 - Can you describe your experience with diary management and scheduling appointments?',
            'ans2': 'Q2 - How do you handle confidential information and sensitive situations?',
            'ans3': 'Q3 - Can you provide an example of a complex problem you have solved in a similar role?',
            'ans4': 'Q4 - How do you prioritize tasks and manage your time when dealing with a busy executive"s schedule?',
            'ans5': 'Q5 - How comfortable are you with liaising with high-level stakeholders and managing professional relationships?',
            'ans6': 'Q6 - Can you describe a situation where you had to handle an unexpected issue or emergency?',
            'ans7': 'Q7 - What experience do you have with travel planning and logistics?',
            'ans8': 'Q8 - How do you ensure effective communication between the MD and other parties?',
            'ans9': 'Q9 - Can you provide an example of an initiative you took to improve efficiency or effectiveness in your role?',
            'ans10': 'Q10 - How do you handle stress and pressure in managing a busy executive"s affairs?',
        }
        widgets = {
            'position_applied': forms.Select(attrs={'class': 'form-select'}),
            'about_myself': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'ans1': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans2': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans3': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans4': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans5': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans6': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans7': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans8': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans9': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ans10': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }