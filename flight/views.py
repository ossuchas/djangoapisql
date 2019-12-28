from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from flight.models import Schedule
from flight.serializers import ScheduleSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def schedule_list(request):
    # Get All
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedules_serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(schedules_serializer.data, safe=False)

    # Add one
    if request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    if request.method == 'DELETE':
        Schedule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def schedule_detail(request, id):
    try:
        schedule = Schedule.objects.get(id=id)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Retrive one
    if request.method == 'GET':
        schedule_serializer = ScheduleSerializer(schedule)
        return JsonResponse(schedule_serializer.data)

    # Update one
    if request.method == 'PUT':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(schedule, data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one
    if request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
