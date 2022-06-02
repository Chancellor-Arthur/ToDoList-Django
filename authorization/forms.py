from django import forms


class AuthorizationForm(forms.Form):
    user = forms.CharField(max_length=20,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter login',
                                      'aria-label': 'Authorization',
                                      'aria-describedby': 'add-btn'}))
    password = forms.CharField(max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter password',
                                          'aria-label': 'Authorization',
                                          'aria-describedby': 'add-btn'}))


class RegistrationForm(forms.Form):
    user = forms.CharField(max_length=20,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter login',
                                      'aria-label': 'Authorization',
                                      'aria-describedby': 'add-btn'}))
    password = forms.CharField(max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter password',
                                          'aria-label': 'Authorization',
                                          'aria-describedby': 'add-btn'}))
