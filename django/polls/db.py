import requests
from django.conf import settings
from django.http import JsonResponse

def get_users(table_id):
    url = f'{settings.NOCODB_BASE_URL}tables/{table_id}/records'
    headers = {'xc-token': settings.NOCODB_API_KEY}
    params = {'limit': 25}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Ошибка при получении данных: {response.text}')



def get_nocodb_data(request):
    url = f'{settings.NOCODB_BASE_URL}tables/mdvifo0mcofz1du/records'
    headers = {'xc-token': settings.NOCODB_API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        records = data.get('list', [])

        response_data = {
            "nocodb-data": "http://localhost:8000/nocodb-data/",
            "records": records
        }
        return JsonResponse(response_data, status=200)
    else:
        # Если произошла ошибка, возвращаем пустой JSON
        return JsonResponse({"error": "Не удалось получить данные из NocoDB"}, status=response.status_code)