from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import Staff


class StaffAdminForm(forms.ModelForm):

    username = forms.CharField(required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = '__all__'

    def save(self, commit=True):

        staff = super().save(commit=False)

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username:

            if staff.user:
                user = staff.user
                user.username = username
            else:
                user = User(username=username)

            if password:
                user.set_password(password)

            user.save()
            staff.user = user

        if commit:
            staff.save()

        return staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'speciality')

    def get_username(self, obj):
        return obj.user.username if obj.user else "-"