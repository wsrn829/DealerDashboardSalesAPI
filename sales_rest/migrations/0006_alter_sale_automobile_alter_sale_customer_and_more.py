# Generated by Django 4.2 on 2024-02-04 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sales_rest", "0005_alter_automobilevo_sold_alter_automobilevo_vin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="automobile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sales",
                to="sales_rest.automobilevo",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sales",
                to="sales_rest.customer",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="salesperson",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sales",
                to="sales_rest.salesperson",
            ),
        ),
    ]
