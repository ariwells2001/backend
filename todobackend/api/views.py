from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo

from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# class TodoList(generics.ListAPIView):
#     serializer_class = TodoSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Todo.objects.filter(user=user).order_by('-created')

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    print("dunno**********************")
    
    def get_queryset(self):
        user = self.request.user
        print("Authorization key of the request headers is {}".format(self.request.META['HTTP_AUTHORIZATION']))
        return Todo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    print("what the hell?")

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
    def perform_update(self,serializer):
        serializer.instance.completed = not(serializer.instance.completed)
        serializer.save()

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try: 
            data = JSONParser().parse(request)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'error':'email taken. choose another email'},status=401)

            user = User.objects.create_user(
                username=data['username'],
                password = data['password'],
                email = data['email']
            )
            
            user.save()

            token = Token.objects.create(user=user)
            print('token is {}'.format(token))
            return JsonResponse({'token': str(token)},status=201)
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken. choose another username'},
                status=400
            )

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("here? {}".format(request))
        data = JSONParser().parse(request)
        print("requested data is {}".format(data))
        #print("Authorization key of the request headers is {}".format(request.META['HTTP_AUTHORIZATION']))
        user = authenticate(
           request,
           username=data['username'],
           password=data['password']
        ) 
        if user is None:
            return JsonResponse({'error':'unable to login. check username and password'},status=400)
        else:
            try:
                token = Token.objects.get(user=user)
                print("The existing token is {}".format(token))
            except:
                token = Token.objects.create(user=user)
                print("The new issued token is {}".format(token))
            return JsonResponse({'token':str(token)},status=201)
