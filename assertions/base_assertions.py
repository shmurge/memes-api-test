import allure


class BaseAssertions:

    @staticmethod
    def check_status_code_is_200(response):
        with allure.step('Статус-код 200'):
            assert 200 == response.status_code, (f"Статус-код {response.status_code}\n"
                                                 f"{response.json()}")

    @staticmethod
    def check_status_code_is_400(response):
        with allure.step('Статус-код 400'):
            assert 400 == response.status_code, (f"Статус-код {response.status_code}\n"
                                                 f"{response.json()}")

    @staticmethod
    def check_status_code_is_404(response):
        with allure.step('Статус-код 404'):
            assert 404 == response.status_code, (f"Статус-код {response.status_code}\n"
                                                 f"{response.json()}")

    @staticmethod
    def check_data_is_equal(exp, act):
        assert exp == act, (f'Данные не идентичны!\n'
                            f'ОР: {exp}\n'
                            f'ФР: {act}')

    @staticmethod
    def is_data_in_array(data, array):
        return True if data in array else False
