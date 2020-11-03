from datetime import datetime
from django import forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Notification, Event, User


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email']


class NotificationsForm(forms.ModelForm):
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    actual_events = Event.objects.filter(Q(date__gte=today) & Q(hour__gte=current_time)).order_by('date')

    TYPES = (
        ('Email', 'Email'),
        ('Webhook', 'Webhook')
    )

    FREQ = (
        ('Week', 'Weekly'),
        ('Day', 'Daily'),
        ('Live', 'Live')
    )

    event = forms.ModelChoiceField(queryset=actual_events, required=True)
    frequency = forms.ChoiceField(choices=FREQ, required=True)
    type = forms.ChoiceField(choices=TYPES, required=True)
    endpoint = forms.URLField(required=False, help_text="Type your endpoint address if needed")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('event', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('endpoint', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('frequency', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = Notification
        fields = ['event', 'frequency', 'type', 'enabled']
