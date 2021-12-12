from django import forms
from .models import Instructor, Course, Lesson, School
import floppyforms
from dal import autocomplete
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.utils.html import format_html
from datetimewidget.widgets import DateTimeWidget
def getAllCourseNames():
    courseset = []
    allCourses = Course.objects.all()
    for i in allCourses:
        if (not(i.name in courseset)):
            courseset.append(i.name)
    return courseset

class DateInput(forms.DateInput):
    input_type = 'date'

class NewInstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude = []
'''class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
    def render(self):
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<div id="{0}">', id_) if id_ else '<div>'
        output = [start_tag]
        for widget in self:
            output.append(format_html(u'<span>{0}</span>', force_text(widget)))
        output.append('</span>')
        return mark_safe('\n'.join(output))'''
class NewCourseForm(forms.ModelForm):
    '''name = forms.CharField(label='New Course Name:', max_length=100)
    level = forms.ChoiceField(choices = Course.LEVELS)
    group = forms.CharField(label="Class", max_length = 20)
    owner = forms.CharField(label="Instructor", max_length = 100)
    startDate = forms.DateField(label="Date of First Lesson",
                                 help_text = "Enter in dd/mm/yyyy format")
    endDate = forms.DateField(label="Date of Last Lesson",
                               help_text = "Enter in dd/mm/yyyy format")
    startTime = forms.TimeField(label="Start Time",
                                 help_text = "Enter in hh:mm format")
    endTime = forms.TimeField(label="End Time",
                               help_text = "Enter in hh:mm format")
    day = forms.ChoiceField(label="Day of Lesson", choices = Course.DAYS)
    interval = forms.IntegerField(label="Number of Weeks Between Each Lesson")
    contact = forms.CharField(label="Name of Teacher-in-charge",
                               max_length = 200)
    email = forms.EmailField(label="Email Address of Teacher-in-charge")
    number = forms.CharField(label="Contact Number of Teacher-in-charge",
                               max_length = 20)

    updated = forms.BooleanField(label="updated?")'''

    class Meta:
        model = Course
        exclude = ['school']
        widgets = {
            'startDate': DateInput(attrs={
                'class':'datepicker',
            }),
            'endDate': DateInput(attrs={
                'class':'datepicker',
            }),
            'name': floppyforms.widgets.Input(datalist=getAllCourseNames()),
        }

class NewLessonForm(forms.Form):
    '''instructorslis = Instructor.objects.all().values_list('id','name', 'location', 'toe', 'remarks')
    instructorslist=[]
    for instr in instructorslis:
        tempstr = instr[1]
        for i in range(20-len(instr[1])):
            tempstr+='.'
        tempstr+=instr[2]
        for i in range(10-len(instr[2])):
            tempstr+='.'
        tempstr+=instr[3]
        for i in range(15-len(instr[3])):
            tempstr+='.'
        tempstr+=instr[4]
        instructorslist.append((instr[1], tempstr))
    instructorslist = [(instr[0], instr[1]+'\tLocation: '+instr[2] +'\tTerms Of Employment: ' +instr[3] +'\tremarks: '+instr[4] +')') for instr in instructorslis]'''
    instructorslist = Instructor.objects.all().values_list('id','name')
    instructorslist = sorted(instructorslist, key = lambda x:x[1])
    instructors = forms.MultipleChoiceField(choices= instructorslist, widget=forms.CheckboxSelectMultiple)
    startTime = forms.DateTimeField(label="Time of lesson", widget= DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3))
    duration = forms.DurationField(help_text = "Enter in hh:mm:ss format")
    comments = forms.CharField(required=False, widget=forms.Textarea)

class NewSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = []

class EditInstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude = []

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['school', 'name']
        widgets = {
            'startDate': DateInput(attrs={
                'class':'datepicker',
            }),
            'endDate': DateInput(attrs={
                'class':'datepicker',
            }),
        }

class EditLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['course', 'calendar_event_id', 'lesson_id', 'synced', 'endTime']
        widgets = {
            'instructors': forms.CheckboxSelectMultiple(),
            'startTime' : DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        }

class EditSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = []
