from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('DOCTOR', 'Bác sĩ'),
        ('PATIENT', 'Bệnh nhân'),
        ('NURSE', 'Y tá'),
    )

    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default='PATIENT')
    avatar = CloudinaryField('avatar', null=True)
    DiaChi = models.CharField(max_length=100, null=True, blank=False, default='sg')


class LichTruc(models.Model):
    NgayTruc = models.DateField(null=False)
    user = models.ForeignKey('User', related_name='lichtrucs', on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.TenThuoc


class PhongKham(models.Model):
    Ten = models.CharField(max_length=100, null=False, unique=True, blank=False)

    def __str__(self):
        return self.Ten


class LichKham(models.Model):
    MaBN = models.ForeignKey('User', related_name='LichKham_BN', on_delete=models.CASCADE)
    MaBS = models.ForeignKey('User', related_name='LichKham_BS', on_delete=models.CASCADE)
    MaPK = models.ForeignKey('PhongKham', related_name='LichKham_PK', on_delete=models.CASCADE)
    NgayKham = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(null=False, default=1)


class ToaThuoc(models.Model):
    Thuoc = models.ManyToManyField('Thuoc', through='ChiTietToaThuoc', related_name='ToaThuoc')

    def __str__(self):
        return self.Thuoc.__str__()


class Thuoc(models.Model):
    TenThuoc = models.CharField(max_length=100, null=False, unique=True, blank=False)
    Gia = models.FloatField(null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.TenThuoc


class ChiTietToaThuoc(models.Model):
    ToaThuoc = models.ForeignKey('ToaThuoc', on_delete=models.CASCADE)
    Thuoc = models.ForeignKey('Thuoc', on_delete=models.CASCADE)
    CongDuong = models.TextField(null=False, blank=False)
    SoLuong = models.IntegerField(null=False, blank=False)
    LieuLuong = models.CharField(max_length=50, null=False, blank=False)
    ChuThich = models.TextField(blank=True)


class BenhAn(models.Model):
    MaBN = models.ForeignKey('User', related_name='BenhAn_BN', on_delete=models.CASCADE)
    MaBS = models.ForeignKey('User', related_name='BenhAn_BS', on_delete=models.CASCADE)
    MaTT = models.ForeignKey('ToaThuoc', related_name='BenhAn_TT', on_delete=models.CASCADE, null=True, blank=True)
    NgayKham = models.DateTimeField(auto_now_add=True)
    NoiDung = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Bệnh án của {self.MaBN.last_name} do {self.MaBS.last_name} khám vào {self.NgayKham}'


class HoaDon(models.Model):
    maTT = models.ForeignKey('ToaThuoc', related_name='TT', on_delete=models.CASCADE)
    NgayMua = models.DateTimeField(null=False, blank=False)
    TongTien = models.FloatField(null=False, blank=False)
