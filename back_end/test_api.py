import requests


def test_login_api(logged_in_api, app_url_api):
    search_url = 'https://api.todoist.com/rest/v2/projects'
    Authorization= {'authorization': "Bearer d352f5e0ad9d7eb00c92f684824d456d1f70fc86"}
    w = logged_in_api.get(url=search_url, headers=Authorization)
    print(w.text)
