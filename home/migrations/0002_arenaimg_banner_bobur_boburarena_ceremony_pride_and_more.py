# Generated by Django 4.2.3 on 2023-08-20 15:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArenaImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('bg_img', models.ImageField(upload_to='shop_banner')),
            ],
        ),
        migrations.CreateModel(
            name='Bobur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230)),
                ('text', models.TextField()),
                ('img', models.ManyToManyField(to='home.img')),
            ],
        ),
        migrations.CreateModel(
            name='BoburArena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', models.ImageField(upload_to='arena/')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ceremony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('img', models.ImageField(upload_to='ceremony/')),
            ],
        ),
        migrations.CreateModel(
            name='Pride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('img', models.ImageField(upload_to='pride/')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', models.ImageField(upload_to='reference/')),
                ('description', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='NewCategoryNew',
            new_name='NewCategory',
        ),
        migrations.RenameModel(
            old_name='Arena',
            new_name='StroeArena',
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Training',
        ),
        migrations.DeleteModel(
            name='TeamCategory',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='age',
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='status',
            field=models.IntegerField(choices=[(1, 'Darvozabon'), (2, 'Himoyachi'), (3, 'Markaz'), (4, 'Hujumchi')], default=1),
            preserve_default=False,
        ),
    ]
