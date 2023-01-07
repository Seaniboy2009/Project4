from .models import Booking, Table
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table', 'number_of_guests', 'booking_time', 'booked_by')
        widgets = {
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
            'booking_time': forms.TextInput(attrs={'type': 'time'}),
        }


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number', 'num_seats')


class DeleteTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_number',)
