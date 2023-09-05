from django.forms import ModelForm
from accounts.models import Profile
    

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ("phone", "title", "image")
        

