from django.contrib import admin

import trump2.models as m

admin.site.register(m.Course)
admin.site.register(m.School)
admin.site.register(m.Instructor)
admin.site.register(m.Lesson)
