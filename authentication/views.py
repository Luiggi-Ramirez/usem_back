from django.contrib.auth.hashers import make_password, check_password

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from authentication.models import CustomUser

class Register(APIView):
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = make_password(request.data['password'])
        
        try:
            user = CustomUser.objects.create(first_name = first_name, last_name = last_name, phone_number = phone_number, email = email, password = password)
            Token.objects.create(user = user)
            data = {'code': 201, 'msg': 'Usuario creado'}
            code = status.HTTP_201_CREATED
        except Exception as err:
            print(err)
            data = {'code': 400, 'msg': 'error al crear usuario o ya existe'}
            code = status.HTTP_400_BAD_REQUEST
        return Response(data, status = code)        
        
        
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        email = email.replace(" ", "")
        
        try:
            user = CustomUser.objects.get(email = email)
            hash_pass = user.password
            verify_pass = check_password(password, hash_pass)
        except:
            verify_pass = False
        
        if verify_pass:
            try:
                token = Token.objects.get(user = user)
            except Token.DoesNotExist:
                token = Token.objects.create(user = user)
            data = {'code': 202, 'msg': 'Aceptado', 'id': user.id, 'first_name': user.first_name, 'email': user.email, 'token': str(token.key)}
            code = status.HTTP_202_ACCEPTED
        else:    
            data = {'code': 401, 'msg': 'Credenciales incorrectas'}
            code = status.HTTP_401_UNAUTHORIZED
    
        return Response(data, status = code)
            

class Logout(APIView):
    def post(self, request):
        email = request.data['email']
        try:
            user = CustomUser.objects.get(email = email)
            token = Token.objects.get(user = user)
            token.delete()
            data = {'code': 200, 'msg': 'Sesión cerrada'}
            code = status.HTTP_200_OK
        except:
            data = {'code': 401, 'msg': 'Credenciales incorrectas'}
            code = status.HTTP_401_UNAUTHORIZED
        return Response(data, status = code)

