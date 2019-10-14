from django.forms import ModelForm
from .models import MangoAbout


class AboutForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = MangoAbout
        fields = '__all__'
