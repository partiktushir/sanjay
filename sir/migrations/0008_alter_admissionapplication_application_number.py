from django.db import migrations, models


def backfill_application_numbers(apps, schema_editor):
    AdmissionApplication = apps.get_model("sir", "AdmissionApplication")
    database = schema_editor.connection.alias
    applications = AdmissionApplication.objects.using(database)

    seen_numbers = set()
    applications_to_update = []

    for application in applications.order_by("pk"):
        number = application.application_number
        if not number or number in seen_numbers:
            applications_to_update.append(application.pk)
        else:
            seen_numbers.add(number)

    next_number = 1
    for application_id in applications_to_update:
        while f"LRMP{next_number:06d}" in seen_numbers:
            next_number += 1

        number = f"LRMP{next_number:06d}"
        applications.filter(pk=application_id).update(
            application_number=number
        )
        seen_numbers.add(number)
        next_number += 1


class Migration(migrations.Migration):

    dependencies = [
        ("sir", "0007_alter_admissionapplication_application_number"),
    ]

    operations = [
        migrations.RunPython(
            backfill_application_numbers,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="admissionapplication",
            name="application_number",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=20,
                unique=True,
            ),
        ),
    ]
