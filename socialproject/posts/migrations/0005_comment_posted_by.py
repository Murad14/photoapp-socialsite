# Generated by Django 4.2.3 on 2023-07-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='murad', max_length=100),
            preserve_default=False,
        ),
    ]
