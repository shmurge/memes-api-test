import allure
import pytest
from config.base_test import BaseTest
from api_client.base_payloads import Usernames
from api_client.memes_api.memes_payloads import MemesPayloads

auth_payload = Usernames()
payload = MemesPayloads()


@allure.suite('Мемы')
@allure.story('Эндпоинт тесты')
class TestMemesEndpoints(BaseTest):

    @allure.feature('Безопасность')
    @allure.title('Авторизация с валидными кредами')
    @pytest.mark.critical
    def test_user_authorization(self):
        self.base_api.user_authorization(auth_payload.valid_username)

    @allure.feature('Безопасность')
    @allure.title('Статус 400 при отправке невалидных кредов')
    @pytest.mark.high
    @pytest.mark.parametrize('username', auth_payload.invalid_usernames)
    def test_400_on_authorization_with_invalid_data(self, username):
        self.base_api.auth_with_invalid_data(username)

    @allure.feature('Поиск мема')
    @allure.title('Статус 404 при невалидном id мема')
    @pytest.mark.medium
    @pytest.mark.parametrize('meme_id', payload.invalid_meme_ids_list)
    def test_404_on_get_meme_with_invalid_id(self, meme_id):
        self.memes_api.get_meme_with_invalid_id(meme_id)

    @allure.feature('Изменение мема')
    @allure.title('Статус 404 при невалидном id мема')
    @pytest.mark.medium
    @pytest.mark.parametrize('meme_id', payload.invalid_meme_ids_list)
    def test_404_on_update_meme_with_invalid_id(self, meme_id):
        self.memes_api.update_meme_with_invalid_id(meme_id, MemesPayloads().update_meme(meme_id))

    @allure.feature('Изменение мема')
    @allure.title('Статус 400, если поле text не строка')
    @pytest.mark.medium
    @pytest.mark.parametrize('text', [1234, 463.465, ['qwer', 123], ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_update_meme_with_invalid_text_format(self, pre_create_and_delete_meme, text):
        meme_id = pre_create_and_delete_meme.id
        model = payload.update_meme(meme_id)
        model.text = text

        self.memes_api.update_meme_with_invalid_payload(meme_id, model)

    @allure.feature('Изменение мема')
    @allure.title('Статус 400, если поле url не строка')
    @pytest.mark.medium
    @pytest.mark.parametrize('url', [1234, 463.465, ['qwer', 123], ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_update_meme_with_invalid_url_format(self, pre_create_and_delete_meme, url):
        meme_id = pre_create_and_delete_meme.id
        model = payload.update_meme(meme_id)
        model.url = url

        self.memes_api.update_meme_with_invalid_payload(meme_id, model)

    @allure.feature('Изменение мема')
    @allure.title('Статус 400, если поле tags не список')
    @pytest.mark.medium
    @pytest.mark.parametrize('tags', [1234, 463.465, 'this is string', ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_update_meme_with_invalid_tags_format(self, pre_create_and_delete_meme, tags):
        meme_id = pre_create_and_delete_meme.id
        model = payload.update_meme(meme_id)
        model.tags = tags

        self.memes_api.update_meme_with_invalid_payload(meme_id, model)

    @allure.feature('Изменение мема')
    @allure.title('Статус 400, если поле info не словарь')
    @pytest.mark.medium
    @pytest.mark.parametrize('info', [1234, 463.465, 'this is string', ['qwer', 123], ('wert', 234.56), None])
    def test_400_on_update_meme_with_invalid_info_format(self, pre_create_and_delete_meme, info):
        meme_id = pre_create_and_delete_meme.id
        model = payload.update_meme(meme_id)
        model.info = info

        self.memes_api.update_meme_with_invalid_payload(meme_id, model)

    @allure.feature('Изменение мема')
    @allure.title('Статус 400, если id в url и пэйлоуде не идентичны')
    @pytest.mark.medium
    def test_400_on_update_meme_with_different_id_in_url_and_payload(self, pre_create_and_delete_meme):
        meme_id = pre_create_and_delete_meme.id
        model = payload.update_meme(meme_id)
        model.id = meme_id + 1

        self.memes_api.update_meme_with_invalid_payload(meme_id, model)

    @allure.feature('Изменение мема')
    @allure.title('Статус 403 при редактировании чужого мема')
    @pytest.mark.medium
    def test_403_on_update_someone_else_meme(self):
        meme_id = self.memes_api.get_someone_else_meme_id()
        self.memes_api.update_someone_else_meme(meme_id, payload.update_meme(meme_id))

    @allure.feature('Создание мема')
    @allure.title('Статус 400, если поле text не строка')
    @pytest.mark.medium
    @pytest.mark.parametrize('text', [1234, 463.465, ['qwer', 123], ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_create_meme_with_invalid_text_format(self, text):
        payload.create_meme.text = text
        self.memes_api.create_meme_with_invalid_payload(payload.create_meme)

    @allure.feature('Создание мема')
    @allure.title('Статус 400, если поле url не строка')
    @pytest.mark.medium
    @pytest.mark.parametrize('url', [1234, 463.465, ['qwer', 123], ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_create_meme_with_invalid_url_format(self, url):
        payload.create_meme.url = url
        self.memes_api.create_meme_with_invalid_payload(payload.create_meme)

    @allure.feature('Создание мема')
    @allure.title('Статус 400, если поле tags не список')
    @pytest.mark.medium
    @pytest.mark.parametrize('tags', [1234, 463.465, 'this is string', ('wert', 234.56), {'key': 'value'}, None])
    def test_400_on_create_meme_with_invalid_tags_format(self, tags):
        payload.create_meme.tags = tags
        self.memes_api.create_meme_with_invalid_payload(payload.create_meme)

    @allure.feature('Создание мема')
    @allure.title('Статус 400, если поле info не словарь')
    @pytest.mark.medium
    @pytest.mark.parametrize('info', [1234, 463.465, 'this is string', ['qwer', 123], ('wert', 234.56), None])
    def test_400_on_create_meme_with_invalid_info_format(self, info):
        payload.create_meme.info = info
        self.memes_api.create_meme_with_invalid_payload(payload.create_meme)

    @allure.feature('Удаление мема')
    @allure.title('Статус 404 при невалидном id мема')
    @pytest.mark.medium
    @pytest.mark.parametrize('meme_id', payload.invalid_meme_ids_list)
    def test_404_on_delete_meme_with_invalid_id(self, meme_id):
        self.memes_api.delete_meme_with_invalid_id(meme_id)

    @allure.feature('Удаление мема')
    @allure.title('Статус 403 при удалении чужого мема')
    @pytest.mark.medium
    def test_403_on_delete_someone_else_meme(self):
        meme_id = self.memes_api.get_someone_else_meme_id()
        self.memes_api.delete_someone_else_meme(meme_id)
