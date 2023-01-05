from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'favorite_programming_lang', 'login_count')}),
        (gettext_lazy('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'gender', 'age', 'profile_image')}),
        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
