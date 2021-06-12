from django.contrib import admin

# Register your models here.
from NewApp.models import Question, Quiz


admin.site.register(Question)
admin.site.register(Quiz)

