import json

from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from cinema.usecases.reservas import reservar_sala, listar_reservas


class SalasViewSet(viewsets.ViewSet):
    @action(methods=["get", "post"], detail=True)
    def reservas(self, request, pk):
        id_sala = int(pk)
        if request.method == "POST":
            try:
                reservar_sala(id_sala)
                return JsonResponse({"msg": "Sala reservada"}, status=201, )
            except PermissionError as e:
                return JsonResponse({"msg": str(e)}, status=422)
        else:
            reservas = listar_reservas(id_sala)
            return JsonResponse({"msg": "OK", "reservas": reservas}, status=200, )
