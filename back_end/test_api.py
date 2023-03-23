import requests

PROJECT_ID = None


def get_task_id(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    response = requests.get(url=f'{app_url_api}/tasks', headers=headers)
    assert response.status_code == 200
    return response.json()[-1]['id']


def test_login_api(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    response = requests.get(url=f'{app_url_api}/projects', headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_adding_new_project(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    data = {"name": "New Project", "is_favorite": 'True', "color": "red", "order": 2}
    response = requests.post(url=f'{app_url_api}/projects', headers=headers, data=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'New Project'
    assert response.json()['is_favorite'] is True
    global PROJECT_ID
    PROJECT_ID = response.json()['id']


def test_adding_new_task_to_project(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    data = {"content": "Buy Milk", "project_id": PROJECT_ID, "description": "We are empty of milk"}
    response = requests.post(url=f'{app_url_api}/tasks', headers=headers, data=data)
    assert response.status_code == 200
    assert response.json()['content'] == 'Buy Milk'
    assert response.json()['project_id'] == PROJECT_ID
    assert response.json()['description'] == 'We are empty of milk'


def test_update_task(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    updated_data = {"content": "Buy Chocolate", "project_id": "2308912219", "description": "We are empty of chocolate"}
    created_task_id = get_task_id(app_url_api)
    response = requests.post(f'{app_url_api}/tasks/{created_task_id}', headers=headers, data=updated_data)
    assert response.status_code == 200
    assert response.json()['content'] == updated_data['content']
    assert response.json()['description'] == updated_data['description']


def test_delete_task(app_url_api):
    headers = {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    created_task_id = get_task_id(app_url_api)
    response = requests.delete(f'{app_url_api}/tasks/{created_task_id}', headers=headers)
    assert response.status_code == 204
    response = requests.get(url=f'{app_url_api}/tasks/{created_task_id}', headers=headers)
    assert response.status_code == 404