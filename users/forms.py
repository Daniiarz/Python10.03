from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    username = forms.CharField(required=True)
    password1 = forms.CharField(label="Password", required=True)
    password2 = forms.CharField(label="Retype password", required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data["password1"]
        password2 = cleaned_data["password2"]
        if password1 != password2:
            msg = "Passwords does not match!"
            self.add_error("password1", msg)
            self.add_error("password2", msg)

        return cleaned_data
