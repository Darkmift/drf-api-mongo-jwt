from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from books.utils.mongo_utils import get_documents, add_document, update_document, delete_document
from books.decorators.jwt_required import jwt_required
import json

@jwt_required
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book_id = add_document('books', data)
            return JsonResponse({'message': 'Book created successfully!', 'book_id': str(book_id)}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def list_books(request):
    if request.method == 'GET':
        try:
            books = get_documents('books', {})
            return JsonResponse(books, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def update_book(request, book_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            modified_count = update_document('books', {'_id': book_id}, data)
            if modified_count:
                return JsonResponse({'message': 'Book updated successfully!'}, status=200)
            return JsonResponse({'error': 'Book not found or not updated'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            deleted_count = delete_document('books', {'_id': book_id})
            if deleted_count:
                return JsonResponse({'message': 'Book deleted successfully!'}, status=200)
            return JsonResponse({'error': 'Book not found or not deleted'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
