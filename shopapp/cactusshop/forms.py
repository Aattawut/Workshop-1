from django import forms
from .models import Contact, Comment

class ContactForm(forms.ModelForm):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    e_mail = forms.EmailField(max_length=60)
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ['firstname','lastname','e_mail','message',]

class CommentForm(forms.ModelForm):
    # product_comment = forms.CharField(max_length=100)
    # message = forms.Textarea()
    # rating = forms.IntegerField()
    
    class Meta:
        model = Comment
        fields = ['message','rating']

    
