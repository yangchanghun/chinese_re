# Generated by Django 5.0.4 on 2024-04-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]