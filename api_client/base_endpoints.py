class BaseEndpoints:

    HOST = 'http://memesapi.course.qa-practice.com'

    authorization = f'{HOST}/authorize'
    is_token_alive = lambda self, token: f'{BaseEndpoints.HOST}/authorize/{token}'
