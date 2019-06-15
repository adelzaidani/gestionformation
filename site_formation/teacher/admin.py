from django.contrib import admin
from .models import Attendance, Assessment


class AttendanceAdmin(admin.ModelAdmin):
    actions = None


    list_display = [
        'student',
        'session',
        'date_of_attendance',
        'attendance_choices',
    ]
    readonly_fields = [
        'student',
        'session',
        'date_of_attendance',
    ]
    date_hierarchy ='date_of_attendance'

    list_filter=[
        'session',
        'date_of_attendance',
        'attendance_choices',
    ]

    search_fields = [
        'student__user__first_name',
        'student__user__last_name',
        'session__training__name',
        ]
    list_display_links = [
        'attendance_choices',
    ]

    def has_add_permission(self,request):
        return False


    def has_delete_permission(self,request, obj=None):
        return False

admin.site.register(Attendance,AttendanceAdmin)


class AssessmentAdmin(admin.ModelAdmin):
    actions = None

    list_display = [
        'student',
        'session',
        'assessment',
    ]
    search_fields = [
        'student__user__first_name',
        'student__user__last_name',
        'session__training__name',
    ]
    list_display_links = [
        'assessment',
    ]

    list_filter = [
        'session',

    ]
    readonly_fields = [
        'student',
        'session',
    ]

    def has_add_permission(self,request):
        return False


    def has_delete_permission(self,request, obj=None):
        return False


admin.site.register(Assessment,AssessmentAdmin)