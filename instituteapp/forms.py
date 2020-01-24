from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control'
            }
        )
    )
    location = forms.CharField(
        label='Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'your location',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'your number',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'your email',
                'class': 'form-control'
            }
        )
    )
