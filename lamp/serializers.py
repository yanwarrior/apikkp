from rest_framework import serializers
from .models import Lampu, Jadwal


class LampuSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	nama = serializers.CharField(required=True, max_length=30)
	status = serializers.BooleanField(default=True, required=False)

	def create(self, validate_data):
		return Lampu.objects.create(**validate_data)

	def update(self, instance, validate_data):
		instance.nama = validate_data.get('nama', instance.nama)
		instance.status = validate_data.get('status', instance.status)
		instance.save()
		return instance


class JadwalSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	lampu = serializers.PrimaryKeyRelatedField(queryset=Lampu.objects.all())
	tanggal = serializers.DateField(required=True)
	jam = serializers.TimeField(required=True)
	state = serializers.BooleanField(required=True)

	def create(self, validate_data):
		return Jadwal.objects.create(**validate_data)

	def update(self, instance, validate_data):
		instance.lampu = validate_data.get('lampu', instance.lampu)
		instance.tanggal = validate_data.get('tanggal', instance.tanggal)
		instance.jam = validate_data.get('jam', instance.jam)
		instance.state = validate_data.get('state', instance.state)
		instance.save()
		return instance
