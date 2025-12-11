import allure
import pytest
from config.base_test import BaseTest
from api_client.memes_api.memes_payloads import MemesPayloads

payload = MemesPayloads()


@allure.suite('Мемы')
@allure.story('API тесты')
class TestMemes(BaseTest):

    @pytest.mark.test
    @allure.feature('Создание мема')
    @allure.title('Создать новый мем')
    @pytest.mark.high
    @pytest.mark.parametrize('new_meme', [payload.create_meme,
                                          payload.create_meme,
                                          payload.create_meme])
    def test_create_meme(self, new_meme):
        create_meme_resp = self.memes_api.create_meme(new_meme)
        get_meme_resp = self.memes_api.get_meme_by_id(create_meme_resp.id)

        self.memes_api.assertions.check_meme_fields(create_meme_resp, get_meme_resp)

    @allure.feature('Создание мема')
    @allure.title('Созданный мем должен отображаться в списке мемов')
    @pytest.mark.high
    def test_created_meme_should_be_in_memes_list(self, pre_create_and_delete_meme):
        response = self.memes_api.get_all_memes()

        self.memes_api.assertions.meme_should_be_in_list(response.data, pre_create_and_delete_meme)

    @allure.feature('Изменение мема')
    @allure.title('Отредактировать мем')
    @pytest.mark.high
    def test_update_meme(self, pre_create_and_delete_meme):
        mem_id = pre_create_and_delete_meme.id
        update_meme_resp = self.memes_api.update_meme(mem_id, payload.update_meme(mem_id))
        get_meme_resp = self.memes_api.get_meme_by_id(update_meme_resp.id)

        self.memes_api.assertions.check_meme_fields(update_meme_resp, get_meme_resp)

    @allure.feature('Изменение мема')
    @allure.title('Повторно отредактировать мем')
    @pytest.mark.medium
    def test_re_update_meme(self, pre_update_and_delete_meme):
        mem_id = pre_update_and_delete_meme.id
        update_meme_resp = self.memes_api.update_meme(mem_id, payload.update_meme(mem_id))
        get_meme_resp = self.memes_api.get_meme_by_id(update_meme_resp.id)

        self.memes_api.assertions.check_meme_fields(update_meme_resp, get_meme_resp)

    @allure.feature('Изменение мема')
    @allure.title('Отредактированный мем должен отображаться в списке мемов')
    @pytest.mark.high
    def test_updated_meme_should_be_in_memes_list(self, pre_update_and_delete_meme):
        response = self.memes_api.get_all_memes()

        self.memes_api.assertions.meme_should_be_in_list(response.data, pre_update_and_delete_meme)

    @allure.feature('Изменение мема')
    @allure.title('Повторно отредактированный мем должен отображаться в списке мемов')
    @pytest.mark.medium
    def test_re_updated_meme_should_be_in_memes_list(self, pre_update_and_delete_meme):
        mem_id = pre_update_and_delete_meme.id
        update_meme_resp = self.memes_api.update_meme(mem_id, payload.update_meme(mem_id))
        get_memes_resp = self.memes_api.get_all_memes()

        self.memes_api.assertions.meme_should_be_in_list(get_memes_resp.data, update_meme_resp)

    @allure.feature('Удаление мема')
    @allure.title('Удалить мем')
    @pytest.mark.high
    def test_delete_meme(self, pre_create_meme):
        mem_id = pre_create_meme.id
        self.memes_api.delete_meme(mem_id)

        self.memes_api.assertions.meme_should_not_be_found(mem_id)

    @allure.feature('Удаление мема')
    @allure.title('Удалить отредактированный мем')
    @pytest.mark.medium
    def test_delete_updated_meme(self, pre_update_meme):
        mem_id = pre_update_meme.id
        self.memes_api.delete_meme(mem_id)

        self.memes_api.assertions.meme_should_not_be_found(mem_id)

    @allure.feature('Удаление мема')
    @allure.title('Удаленный мем не должен отображаться в списке мемов')
    @pytest.mark.high
    def test_deleted_meme_should_not_be_in_memes_list(self, pre_create_meme):
        mem_id = pre_create_meme.id
        self.memes_api.delete_meme(mem_id)
        response = self.memes_api.get_all_memes()

        self.memes_api.assertions.meme_should_not_be_in_list(response.data, pre_create_meme)

    @allure.feature('Удаление мема')
    @allure.title('Удаленный после редактирования мем не должен отображаться в списке мемов')
    @pytest.mark.high
    def test_deleted_meme_should_not_be_in_memes_list(self, pre_update_meme):
        mem_id = pre_update_meme.id
        self.memes_api.delete_meme(mem_id)
        response = self.memes_api.get_all_memes()

        self.memes_api.assertions.meme_should_not_be_in_list(response.data, pre_update_meme)
