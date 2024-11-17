from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from books.utils.mongo_utils import add_document, get_documents
from decouple import config
import json
import jwt
import datetime

SECRET_KEY_JWT = config('SECRET_KEY_JWT')  # Replace with a secure key

def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Check if user already exists
            existing_user = get_documents('users', {'username': username})
            if existing_user:
                return JsonResponse({'error': 'User already exists'}, status=400)

            # Hash the password before storing
            hashed_password = make_password(password)
            user = {
                'username': username,
                'password': hashed_password,
                'created_at': datetime.datetime.utcnow()
            }
            user_id = add_document('users', user)
            return JsonResponse({'message': 'User registered successfully', 'user_id': str(user_id)}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Find the user
            user = get_documents('users', {'username': username})
            if not user:
                return JsonResponse({'error': 'Invalid username or password'}, status=400)

            user = user[0]  # Extract the first (and only) result

            # Verify the password
            if not check_password(password, user['password']):
                return JsonResponse({'error': 'Invalid username or password'}, status=400)

            # Generate JWT token
            payload = {
                'username': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, SECRET_KEY_JWT, algorithm='HS256')
            return JsonResponse({'message': 'Login successful', 'token': token}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def logout(request):
    # For token-based authentication, "logout" is usually handled client-side by deleting the token.
    # However, you can implement token blacklisting here if required.
    return JsonResponse({'message': 'Logout successful'}, status=200)
