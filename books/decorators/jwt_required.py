import jwt
from django.http import JsonResponse
from functools import wraps
from django.conf import settings
from decouple import config

SECRET_KEY = config('SECRET_KEY_JWT')

def jwt_required(func):
    @wraps(func)
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)
        
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = payload  # Attach user information to the request for further use
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        return func(request, *args, **kwargs)
    return wrapped_view
