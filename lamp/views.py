# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Lampu, Jadwal
from .serializers import LampuSerializer, JadwalSerializer


@api_view(['GET'])
def api_lampu_list(request):
	"""
	Untuk mengambil semua data lampu.
	"""
	# TODO: request.user = user yang mengakses melalui token
	daftar_lampu = Lampu.objects.all()
	serializer = LampuSerializer(daftar_lampu, many=True)
	return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def api_lampu_add(request):
	"""
	Api untuk menambahkan data lampu.
	"""

	data = JSONParser().parse(request)
	serializer = LampuSerializer(data=data)
	print(serializer.is_valid())

	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, status=201)
	return JsonResponse(serializer.errors, status=400)


@api_view(['PUT'])
def api_lampu_edit(request, pk):
	"""
	Api untuk mengupdate data lampu.
	"""
	try:
		lampu = Lampu.objects.get(pk=pk)
	except Lampu.DoesNotExist:
		return HttpResponse(status=404)

	data = JSONParser().parse(request)
	serializer = LampuSerializer(lampu, data=data)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data)
	return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def api_lampu_delete(request, pk):
	"""
	Api untuk menghapus data lampu.
	"""
	try:
		lampu = Lampu.objects.get(pk=pk)
	except Lampu.DoesNotExist:
		return HttpResponse(status=404)

	lampu.delete()
	return JsonResponse({'status': True})


@api_view(['GET'])
def api_lampu_detail(request, pk):
	"""
	Api untuk mengambil lampu berdasarkan pk-nya.
	"""
	try:
		lampu = Lampu.objects.get(pk=pk)
	except Lampu.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = LampuSerializer(lampu)
		return JsonResponse(serializer.data)


@api_view(['GET'])
def api_jadwal_list(request):
	"""
	Api untuk mengambil semua data jadwal.
	"""
	daftar_jadwal = Jadwal.objects.all()
	serializer = JadwalSerializer(daftar_jadwal, many=True)
	return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def api_jadwal_add(request):
	"""
	Api untuk menambahkan jadwal.
	"""
	data = JSONParser().parse(request)
	serializer = JadwalSerializer(data=data)

	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, status=201)
	return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def api_jadwal_detail(request, pk):
	"""
	Api untuk mengambil jadwal berdasarkan pk-nya.
	"""
	try:
		jadwal = Jadwal.objects.get(pk=pk)
	except Jadwal.DoesNotExist:
		return HttpResponse(status=404)

	serializer = JadwalSerializer(jadwal)
	return JsonResponse(serializer.data)


@api_view(['PUT'])
def api_jadwal_edit(request, pk):
	"""
	Api untuk mengambil jadwal berdasarkan pk-nya.
	"""
	try:
		jadwal = Jadwal.objects.get(pk=pk)
	except Jadwal.DoesNotExist:
		return HttpResponse(status=404)

	data = JSONParser().parse(request)
	serializer = JadwalSerializer(jadwal, data=data)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data)
	return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def api_jadwal_delete(request, pk):
	"""
	Api untuk mengambil jadwal berdasarkan pk-nya.
	"""
	try:
		jadwal = Jadwal.objects.get(pk=pk)
	except Jadwal.DoesNotExist:
		return HttpResponse(status=404)

	jadwal.delete()
	return JsonResponse({'status': True})
