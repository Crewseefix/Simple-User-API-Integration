import pdb, requests, json, os
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from dotenv import load_dotenv


load_dotenv()
# function that sends a get request to the api
@api_view(['GET'])
def get_users(request):
    try:
        url = os.getenv('BASE_URL')
        try:
            response = requests.get(url)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

# function that sends a post request to the api
@api_view(['POST'])
def create_user(request):
    try:
        url = os.getenv('BASE_URL')
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.post(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY) 
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)
    
# function that sends a patch request to the api
@api_view(['PATCH'])
def patch_user(request, id):
    try:
        url = os.getenv('BASE_URL') + str(id) + '/'
        headers = {'Content-Type': 'application/json'}
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.patch(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

# function that sends a delete request to the api
@api_view(['DELETE'])
def delete_user(request, id):
    try:
        url = os.getenv('BASE_URL') + str(id) + '/'
        try:
            response = requests.delete(url)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

def get_user(request, id):
    try:
        url = os.getenv('BASE_URL') + str(id) + '/'
        try:
            response = requests.get(url)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(['POST'])
def create_users(request):
    try:
        url = os.getenv('BASE_URL') + 'updates/'
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.post(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

@api_view(['PATCH'])
def patch_users(request):
    try:
        url = os.getenv('BASE_URL') + 'updates/'
        headers = {'Content-Type': 'application/json'}
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.patch(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

@api_view(['DELETE'])
def delete_users(request):
    try:
        url = os.getenv('BASE_URL') + 'updates/'
        headers = {'Content-Type': 'application/json'}
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.delete(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=status.HTTP_200_OK, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)

@api_view(['POST'])
def create_patch_delete(request):
    try:
        url = os.getenv('BASE_URL') + 'createdeleteandupdate/'
        headers = {'Content-Type': 'application/json'}
        try:
            data = json.dumps(request.data)
        except Exception:
            response = {"error": "Invalid request."}
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST, safe=False)
        try:
            response = requests.post(url, data=data, headers=headers)
        except Exception:
            response = {"error": f"Server error connecting to upstream: {url}"}
            return JsonResponse(response, status=status.HTTP_502_BAD_GATEWAY)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except Exception:
        response = {"error": f"Connection to server failed"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT)