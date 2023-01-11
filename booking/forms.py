from .models import Booking, Table, TIME_SLOTS
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
import datetime

NUMBER_OF_SEATS = [
    ('2', '2'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        booking_time = forms.ChoiceField(choices=TIME_SLOTS,)
        number_of_guests = forms.ChoiceField(choices=NUMBER_OF_SEATS,)
        fields = ('number_of_guests', 'booking_date', 'booking_time',)
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
        }


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.ModelForm):
    class Meta:
        model = Table
        # tables = list(Table.objects.all())
        # table_number = forms.ChoiceField(choices=tables,)
        fields = ('table_number',)
