from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Category, Course, Lesson
from django import forms
from ckeditor_uploader.widgets \
import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


# Register your models here.
class CourseAdmin (admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['image_view']

    def image_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='120' />")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }



class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    readonly_fields = ['image_view']
    list_display = ['id', 'created_date', 'active']
    search_fields = ['id']
    list_filter = ['id', 'created_date']
    def image_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)