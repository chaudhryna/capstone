from django.forms import ModelForm, Textarea, TextInput, Select, DateInput, DateField

from tickets.models import Ticket, TechNotes
from accounts.models import User 
    

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket 
        fields = ("title", "details", "type_of_issue")
        
        widgets = {
            'type_of_issue': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'details': Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 3}),
        }
        
class UpdateTicketForm(ModelForm):    
    class Meta:
        model = Ticket
        fields = ("status", "due_date", "assigned_tech")
        
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'due_date': DateInput(
                attrs={
                'type': 'date',
                'class': 'form-control'
                }
            ),
            'assigned_tech': Select(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super(UpdateTicketForm, self).__init__(*args, **kwargs)
        self.fields['assigned_tech'].queryset = User.objects.filter(groups__name='IT Support').order_by('last_name')
        
        
class TechNotesForm(ModelForm):
    class Meta:
        model = TechNotes
        fields = ('note',)

        widgets = {
            'note': Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3})
        }