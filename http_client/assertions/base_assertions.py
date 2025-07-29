import allure


class BaseAssertions:

    @staticmethod
    def check_status_code_is_200(response):
        with allure.step('Status code is 200'):
            assert 200 == response.status_code, response.json()

    @staticmethod
    def check_data_is_equal(exp, act):
        assert exp == act, (f'Data is not equal!\n'
                            f'Exp: {exp}\n'
                            f'Act: {act}')
