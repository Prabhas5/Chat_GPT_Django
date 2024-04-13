from django.db import models
from django.db import models

class CandidateResponse(models.Model):
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Other', 'Other')
    ]

    position_applied = models.CharField(max_length=50, choices=POSITION_CHOICES)
    about_myself = models.TextField()
    experience = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    ans1 = models.TextField()
    ans2 = models.TextField()
    ans3 = models.TextField()
    ans4 = models.TextField()
    ans5 = models.TextField()
    ans6 = models.TextField()
    ans7 = models.TextField()
    ans8 = models.TextField()
    ans9 = models.TextField()
    ans10 = models.TextField()

    def __str__(self):
        return f"Candidate Response - {self.position_applied}"

