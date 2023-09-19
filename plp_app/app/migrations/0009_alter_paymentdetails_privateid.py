# Generated by Django 4.1.3 on 2023-01-10 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_paymentdetails_privateid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentdetails",
            name="privateId",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.private",
            ),
        ),
    ]