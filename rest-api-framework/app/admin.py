from django.contrib import admin
from .models import Profile, Post, Groups
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Profile)
class profapi(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Post)
class postapi(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Groups)
class groupsapi(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

