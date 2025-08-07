from faker import Faker
from api_client.base_models import RequestAuthorizationModel

fake = Faker()


class Usernames:
    valid_username = RequestAuthorizationModel(
        name=f"{fake.first_name()} {fake.last_name()}"
    )

    invalid_usernames = [
        RequestAuthorizationModel(name=""),
        RequestAuthorizationModel(name=123450),
        RequestAuthorizationModel(name=1234.5678),
        RequestAuthorizationModel(name=[f"{fake.first_name()} {fake.last_name()}"]),
        RequestAuthorizationModel(name={fake.first_name(): fake.last_name()})
    ]
