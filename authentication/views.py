from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json

from authentication.models import User
from authentication.serializers import UserSerializer


@api_view(['GET', 'POST']) 
def signup(request): # function to signup the user based on username, email, password

    user_data = json.loads(request) # parses dict/json
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']

    find_user = User.objects.filter(username=username).values()

    if not bool(find_user): # if this username does not exist yet
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        return JsonResponse({'message': "Successfully signed up"}, status=200)
    else:
        return JsonResponse({'message': 'Username is already taken'}, status=409)


@api_view(['GET', 'POST'])
def signin(request): # function to signin the user based on username and password
    
    user_data = json.loads(request) # parses dict/json
    username = user_data['username']
    password = user_data['password']

    match_response = User.objects.filter(username=username, \
                                            password=password).values()

    if not bool(match_response): # if username or password is incorrect
        return JsonResponse({'message': "Username or password is incorrect"}, 
                                status=401)
    else:
        return JsonResponse({'message': "Successfully signed in"}, 
                                status=200)


@api_view(['GET'])
def read_users(request): # function to read all the info of users from database

    if request.method == "GET":
        users = User.objects.all()

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse({'message': users_serializer.data},
                                status = 200,
                                    safe=False)


@api_view(['GET'])
def get_user(request): # function to get the info of one user based on username

    user_data = json.loads(request) # parses dict/json
    username = user_data['username']
    
    try:
        user = User.objects.get(username=username)
        user_serializer     = UserSerializer(user)
        return JsonResponse({'message': 
                                    user_serializer.data}, 
                                        status=200)

    except User.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND, safe=False)


@api_view(['DELETE'])
def delete_user(request): # function to delete the user based on username

    user_data = json.loads(request) # parses dict/json
    username = user_data['username']

    user_delete = User.objects.filter(username=username).delete()
    if user_delete[0] != 0:
        return JsonResponse({'message': f"User has been successfully deleted"}, status=200)

    else:
        return JsonResponse({'message': 'User does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)


# def signout(request):
#     logout(request)
#     messages.success(request, "Logged out successfully")