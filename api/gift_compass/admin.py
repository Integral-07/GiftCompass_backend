from django.contrib import admin
from .models import Test, Page, Content, Choice, Answer, SelectedChoice


admin.site.register(Test)
admin.site.register(Page)
admin.site.register(Content)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(SelectedChoice)