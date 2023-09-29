from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

from accounts.models import User, Profile


class Ticket(models.Model):
    TYPE_OF_ISSUE = [
        ('HARDWARE', 'Hardware'),
        ('SOFTWARE', 'Software'),
        ('ACCOUNT', 'Account'),
        ('PASSWORD', 'Password'),
        ('OTHER', 'Other'),
    ]
    STATUS = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('UNDER_REVIEW', 'Under review'),
        ('AWAITING_RESPONSE', 'Awaiting response'),
        ('IN_PROCESS', 'In process'),
        ('COMPLETE', 'Complete')
    ]
    type_of_issue = models.CharField(
        max_length=10, choices=TYPE_OF_ISSUE, blank=True, default='HARDWARE')
    status = models.CharField(max_length=20, null=True,
                              choices=STATUS, default='OPEN')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    assigned_tech = models.ForeignKey(User, on_delete=models.SET_NULL,
                                      blank=True, null=True, related_name='assigned_tech')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class TechNotes(models.Model):
    tech = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tech', blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='tech_notes')
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Date: {} by {}'.format(self.created, self.tech)
