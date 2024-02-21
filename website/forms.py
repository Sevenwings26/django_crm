from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# token for git 
# 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

git clone https://username:ghp_tokenstring@github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

git clone https://Sevenwings26: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@github.com/Sevenwings26/CRM_Django.git



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=150,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unique email address'}))
    
    
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] ='User name'
        self.fields['username'].label = ''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_only </small></span>'
        
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text=' <ul class="form-text text-muted" > <li>Your password can\'t be too similar to your personal information.</li> <li> Your password must contain 8 characters. </li><li>Your password can\'t be too commonly used password</li> <li> Your password can\'t be entirely numeric. </ul>'
        
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        