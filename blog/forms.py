from django.forms import ModelForm,Textarea, TextInput
from .models import post

class PostForm(ModelForm):
# class PostForm(forms.Form):

    # title=forms.CharField(widget=forms.TextInput(attrs="class":"ejemplo"))
    # title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea'}))
    class Meta: 
       model = post
       fields = (
                 'title',
                 'content',
                 'image',
                 )
       #se pone para darle una clase a este inpit
       widgets = {
           'title':TextInput(attrs={"class":"ejemplo"})
       }     