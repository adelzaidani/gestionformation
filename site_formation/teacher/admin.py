from django.contrib import admin
from .models import Attendance, Assessment
from django.utils.safestring import mark_safe


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

    def colored_assessmeent(self,obj):
        if obj.assessment <50:
            return mark_safe('<span style="color:red;">{}/100</span>' .format(obj.assessment))
        else:

            return mark_safe('<span style="color:green;">{}/100</span>'.format(obj.assessment))

    colored_assessmeent.short_description='evaluation'


    list_display = [
        'student',
        'session',
        'colored_assessmeent',
    ]
    search_fields = [
        'student__user__first_name',
        'student__user__last_name',
        'session__training__name',
    ]
    list_display_links = [
        'colored_assessmeent',
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