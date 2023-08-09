
import pdb, requests, json, os
from dotenv import load_dotenv
from django.http import JsonResponse
from rest_framework import status
from requests.exceptions import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view

# Create your views here.
load_dotenv()

# function that sends a get request to the api
@api_view(['GET'])
def get_users(request):
    try:
        url = os.getenv('BASE_URL')
        response = requests.get(url)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
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
        response = requests.post(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except requests.exceptions.RequestException as e:
        response = {"error": f"Connection Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)

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
        response = requests.patch(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)
    
# function that sends a delete request to the api
@api_view(['DELETE'])
def delete_user(request, id):
    try:
        url = os.getenv('BASE_URL') + str(id) + '/'
        response = requests.patch(url)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)

def get_user(request, id):
    try:
        url = os.getenv('BASE_URL') + str(id) + '/'
        response = requests.get(url)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)

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
        response = requests.post(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)
    
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
        response = requests.patch(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)
    
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
        response = requests.delete(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=status.HTTP_200_OK, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)
 
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
        response = requests.post(url, data=data, headers=headers)
        return JsonResponse(response.json(), status=response.status_code, safe=False)
    except RequestException as e:
        response = {"error": f"Error during API call: {e}"}
        return JsonResponse(response, status=status.HTTP_408_REQUEST_TIMEOUT, safe=False)