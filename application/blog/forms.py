from django import forms
from django.forms import ModelForm, Textarea
from .models import Article, Author
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from ckeditor.widgets import CKEditorWidget

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# crispy forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from crispy_forms.layout import Field




class ArticleForm(forms.ModelForm):
	contenu = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Article
		# widgets = {
		# 	'contenu': Textarea(attrs={'cols': 10, 'rows': 5}),
		# }
		fields = ['titre', 'contenu', 'image']


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    anniv = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    # pdp = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'anniv', 'password1')





class CustomCheckbox(Field):
    template = 'blog/pages/custom_checkbox.html'

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            CustomCheckbox('check_me_out'), #ce checkbox est personnalisé dont custom_checkbox.html est le template
            Submit('submit', 'Sign in')
        )
