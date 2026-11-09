from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cuenta
from .serializers import CuentaSerializer

@api_view(['GET'])
def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    serializer = CuentaSerializer(cuentas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def ver_cuenta(request, id):
    try:
        cuenta = Cuenta.objects.get(id=id)
    except Cuenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CuentaSerializer(cuenta)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def agregar_cuenta(request):
    serializer = CuentaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modificar_cuenta(request, id):
    try:
        cuenta = Cuenta.objects.get(id=id)
    except Cuenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CuentaSerializer(cuenta, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_cuenta(request, id):
    try:
        cuenta = Cuenta.objects.get(id=id)
    except Cuenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    cuenta.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
