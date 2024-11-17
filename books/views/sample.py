from django.http import JsonResponse
from books.utils.mongo_utils import get_documents, add_document, update_document, delete_document

def sample_list_view(request):
    if request.method == 'GET':
        documents = get_documents('mycollection', {})
        return JsonResponse(documents, safe=False)  # Using safe=False for non-dict objects

def sample_create_view(request):
    if request.method == 'POST':
        data = {'key': 'value'}  # Example data, adjust as per your request handling
        document_id = add_document('mycollection', data)
        return JsonResponse({'inserted_id': str(document_id)})

def sample_update_view(request):
    if request.method == 'POST':
        query = {'key': 'value'}
        new_values = {'key': 'new_value'}
        modified_count = update_document('mycollection', query, new_values)
        return JsonResponse({'modified_count': modified_count})

def sample_delete_view(request):
    if request.method == 'POST':
        query = {'key': 'value'}
        deleted_count = delete_document('mycollection', query)
        return JsonResponse({'deleted_count': deleted_count})
