from rest_framework.decorators import action

from .models import *
from django.views import View
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, generics, filters
from .serializers import *
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend


# phan quyen
class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'DOCTOR'


class UserView(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]


class LichKhamView(viewsets.ModelViewSet):
    queryset = LichKham.objects.all()
    serializer_class = LichKhamSerializer

    def create(self, request, *args, **kwargs):
        # Kiểm tra số lượng lịch khám trong ngày
        ngay_kham = request.data.get('NgayKham')
        if LichKham.objects.filter(NgayKham=ngay_kham).count() >= 100:
            return Response({'error': 'Đã đạt tới giới hạn số lượng lịch khám trong ngày.'},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = self.get_object()

        # Gửi email khi lịch khám được xác nhận
        if serializer.validated_data.get('active') is True:
            send_mail(
                'Lịch khám của bạn đã được xác nhận',
                'Lịch khám của bạn vào ngày {} đã được xác nhận.'.format(instance.NgayKham),
                'giabaoabc1512@gmail.com',
                [instance.MaBN.email],
                fail_silently=False,
            )

        super().perform_update(serializer)

    @action(detail=True, methods=['post'])
    def huy_lich_kham(self, request, pk=None):
        # Huỷ lịch khám theo id
        lich_kham = self.get_object()
        lich_kham.delete()
        return Response({'success': 'Đã huỷ lịch khám thành công.'})

    @action(detail=True, methods=['get'])
    def gui_email_lich_hen(self, request, pk=None):
        # Gửi email lịch hẹn theo id
        lich_kham = self.get_object()
        send_mail(
            'Lịch hẹn của bạn',
            'Lịch hẹn của bạn với bác sĩ {} vào ngày {} tại phòng khám {}.'.format(lich_kham.MaBS.last_name,
                                                                                   lich_kham.NgayKham,
                                                                                   lich_kham.MaPK.Ten),
            'giabaoabc1512@gmail.com',
            [lich_kham.MaBN.email],
            fail_silently=False,
        )
        return Response({'success': 'Đã gửi email lịch hẹn thành công.'})


class ToaThuocView(viewsets.ModelViewSet):
    queryset = ToaThuoc.objects.all()
    serializer_class = ToaThuocSerializer
    permission_classes = [IsDoctor]
    filter_backends = [filters.SearchFilter]
    search_fields = ['TenThuoc', 'CongDuong']


class BenhAnView(viewsets.ModelViewSet):
    queryset = BenhAn.objects.all()
    serializer_class = BenhAnSerializer
    permission_classes = [IsDoctor]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['NgayKham']
    ordering_fields = ['NgayKham']
