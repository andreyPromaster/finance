# Generated by Django 4.1.2 on 2022-10-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_company_bank_detail'),
        ('bill', '0002_alter_invoice_created_at_alter_invoice_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='staff.company'),
            preserve_default=False,
        ),
    ]