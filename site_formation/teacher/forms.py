from .models import Attendance
from django.forms import ModelForm

class AttendanceForm(ModelForm):
    class Meta:
        model=Attendance
        fields=['student','session','date_of_attendance', 'attendance_choices']


