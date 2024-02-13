# Generated by Django 3.2.23 on 2024-02-12 14:09

import cloudinary.models
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
            name='PhongKham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ten', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenThuoc', models.CharField(max_length=100, unique=True)),
                ('Gia', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('user_type', models.CharField(choices=[('DOCTOR', 'Bác sĩ'), ('PATIENT', 'Bệnh nhân'), ('NURSE', 'Y tá')], default='PATIENT', max_length=7)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar')),
                ('NgaySinh', models.DateField(null=True)),
                ('DiaChi', models.CharField(default='sg', max_length=100, null=True)),
                ('role', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ToaThuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CongDuong', models.TextField()),
                ('SoLuong', models.IntegerField()),
                ('LieuLuong', models.CharField(max_length=50)),
                ('ChuThich', models.TextField(blank=True)),
                ('MaThuoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ToaThuoc', to='Web.thuoc')),
            ],
        ),
        migrations.CreateModel(
            name='LichTruc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NgayTruc', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lichtrucs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LichKham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NgayKham', models.DateTimeField()),
                ('MaBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LichKham_BN', to=settings.AUTH_USER_MODEL)),
                ('MaBS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LichKham_BS', to=settings.AUTH_USER_MODEL)),
                ('MaPK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LichKham_PK', to='Web.phongkham')),
            ],
        ),
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NgayMua', models.DateTimeField()),
                ('TongTien', models.FloatField()),
                ('maTT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TT', to='Web.toathuoc')),
            ],
        ),
        migrations.CreateModel(
            name='BenhAn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NgayKham', models.DateTimeField(default='01-01-2000')),
                ('NoiDung', models.TextField(default='!ok')),
                ('MaBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BenhAn_BN', to=settings.AUTH_USER_MODEL)),
                ('MaBS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BenhAn_BS', to=settings.AUTH_USER_MODEL)),
                ('MaTT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BenhAn_TT', to='Web.toathuoc')),
            ],
        ),
    ]
