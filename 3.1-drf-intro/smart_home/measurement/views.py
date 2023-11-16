from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Sensor, Measurement


class SensorView(CreateAPIView, ListAPIView):
    '''Получить список датчиков'''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        '''Создать датчик'''
        ser = SensorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class SensorDetailView(RetrieveAPIView):
    """Получить информацию по конкретному датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        '''Изменить датчик'''
        sensor = get_object_or_404(Sensor, pk=pk)
        ser = SensorDetailSerializer(sensor, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class MeasurementView(ListAPIView):
    """Добавить измерение"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        ser = MeasurementSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
