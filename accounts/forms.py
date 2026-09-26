from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={
                                                        'placeholder': 'email@example.com',
                                                        'autocomplete': 'email'
                                                        }))

    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ("username", 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Kreatywna nazwa użytkownika',
            'autocomplete': 'username',
            })
        self.fields['password1'].widget.attrs.update({
            'placeholder': "Min. 8 znaków",
            'autocomplete': 'new-password',
            })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Powtórz hasło',
            'autocomplete': 'new-password',
            })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nazwa użytkownika',
            'autocomplete': 'username'
            })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Hasło',
            'autocomplete': 'current-password'
            })
