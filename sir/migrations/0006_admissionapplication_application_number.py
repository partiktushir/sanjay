from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sir", "0005_alter_schoolsettings_location_embed_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="admissionapplication",
            name="application_number",
            field=models.CharField(
                max_length=20,
                blank=True,
                null=True,
                editable=False,
            ),
        ),
    ]