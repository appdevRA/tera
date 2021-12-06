# Generated by Django 3.2.8 on 2021-12-01 15:43

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


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
                ('time', models.DateTimeField(default=datetime.datetime(2021, 12, 1, 15, 43, 46, 931581, tzinfo=utc))),
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
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ra.admin')),
            ],
            options={
                'db_table': 'Site',
            },
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_removed', models.IntegerField(default=0)),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_group',
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
                ('dateAccessed', models.DateTimeField(default=django.utils.timezone.now)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('DOI', models.CharField(blank=True, max_length=200)),
                ('ISSN', models.CharField(blank=True, max_length=100)),
                ('isRemoved', models.IntegerField(default=0)),
                ('isFavorite', models.BooleanField(default=False)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_bookmark',
            },
        ),
        migrations.CreateModel(
            name='User_access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_access', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.department')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_access',
            },
        ),
        migrations.CreateModel(
            name='Group_bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_removed', models.IntegerField(default=0)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_bookmark')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_group')),
            ],
            options={
                'db_table': 'Group_bookmark',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_removed', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Folder',
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
            name='Bookmark_folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_removed', models.IntegerField(default=0)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.user_bookmark')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ra.folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Bookmark_folder',
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
