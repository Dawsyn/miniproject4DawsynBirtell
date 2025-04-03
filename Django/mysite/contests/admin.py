from django.contrib import admin
from .models import Contest
# Register your models here.

admin.site.register(Contest)  # Register the Form model with the admin site.

class ChoiceInline(admin.TabularInline):
    extra = 3

class ContestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["name"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["name", "email", "age", "sex"]
    list_filter = ["name"]
    search_fields = ["name", "email"]

class ContestCreation(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Date information", {"fields": ["email"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]   
