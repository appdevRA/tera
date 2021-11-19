# Generated by Django 3.2.6 on 2021-11-19 15:50

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbv', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Dissertation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('abstract', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'Dissertation',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('member', models.IntegerField(blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 466385))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Headers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5)),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 469385))),
            ],
            options={
                'db_table': 'Practice',
            },
        ),
        migrations.CreateModel(
            name='Proxies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy', models.CharField(max_length=100)),
                ('isUsed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Proxies',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 468385))),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ra.admin')),
            ],
            options={
                'db_table': 'Site',
            },
        ),
        migrations.CreateModel(
            name='User_folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=25)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 467385))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Folders',
            },
        ),
        migrations.CreateModel(
            name='User_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_files',
            },
        ),
        migrations.CreateModel(
            name='User_bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('websiteTitle', models.CharField(max_length=1000)),
                ('itemType', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('journalItBelongs', models.CharField(blank=True, max_length=1000)),
                ('volume', models.IntegerField(blank=True)),
                ('numOfCitation', models.CharField(blank=True, max_length=1000)),
                ('numOfDownload', models.CharField(blank=True, max_length=1000)),
                ('numOfPages', models.CharField(blank=True, max_length=1000)),
                ('edition', models.CharField(blank=True, max_length=20)),
                ('publisher', models.CharField(blank=True, max_length=1000)),
                ('publicationYear', models.CharField(blank=True, max_length=20)),
                ('dateAccessed', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 464385))),
                ('dateAdded', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 464385))),
                ('DOI', models.CharField(blank=True, max_length=200)),
                ('ISSN', models.CharField(blank=True, max_length=100)),
                ('isRemoved', models.IntegerField(default=0)),
                ('isFavorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Bookmarks',
            },
        ),
        migrations.CreateModel(
            name='User_access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_access', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 468385))),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.department')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_access',
            },
        ),
        migrations.CreateModel(
            name='Group_bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 23, 50, 38, 466385))),
                ('is_trash', models.IntegerField(default=0)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_bookmark')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.group')),
            ],
            options={
                'db_table': 'Group_bookmarks',
            },
        ),
        migrations.CreateModel(
            name='Dissertation_authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('dissertation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.dissertation')),
            ],
            options={
                'db_table': 'Dissertation_authors',
            },
        ),
        migrations.CreateModel(
            name='Bookmark_folders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_bookmark')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Bookmark_folders',
            },
        ),
        migrations.AddField(
            model_name='admin',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.department'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
