from django import forms
from .models import AdmissionApplication


class AdmissionApplicationForm(forms.ModelForm):

    class Meta:
        model = AdmissionApplication

        fields = [
            "student_name",
            "father_name",
            "mother_name",
            "date_of_birth",
            "gender",
            "applying_class",
            "mobile",
            "email",
            "address",
            "previous_school",
            "message",
        ]

        widgets = {

            "student_name": forms.TextInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter student's full name",
                }
            ),

            "father_name": forms.TextInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter father's name",
                }
            ),

            "mother_name": forms.TextInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter mother's name",
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "admission-input",
                    "type": "date",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "admission-input",
                }
            ),

            "applying_class": forms.TextInput(
    attrs={
        "class": "admission-input",
        "placeholder": "Enter applying class",
    }
),
            "mobile": forms.TextInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter mobile number",
                    "maxlength": "15",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter email address",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter complete address",
                    "rows": 4,
                }
            ),

            "previous_school": forms.TextInput(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Enter previous school name",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "admission-input",
                    "placeholder": "Any additional information...",
                    "rows": 4,
                }
            ),
        }