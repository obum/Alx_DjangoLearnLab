# Generated by Django 5.1.3 on 2024-12-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tag_alter_comment_post_tagpost_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.ManyToManyField(blank=True, through='blog.TagPost', to='blog.post'),
        ),
    ]
