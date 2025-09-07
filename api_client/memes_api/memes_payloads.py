from faker import Faker
from api_client.memes_api.models.request_memes_models import (
    RequestCreateMemeModel,
    RequestUpdateMemeModel
)

fake = Faker()


class MemesPayloads:
    create_meme = RequestCreateMemeModel(
        text=fake.text(),
        url=fake.url(),
        tags=[fake.text(max_nb_chars=5),
              fake.text(max_nb_chars=6),
              fake.text(max_nb_chars=7)
              ],
        info={"colors": [fake.color() for _ in range(2)],
              "names": [fake.name() for _ in range(2)]
              }
    )

    def update_meme(self, mem_id):
        model = RequestUpdateMemeModel(
            id=mem_id,
            text=fake.text(),
            url=fake.url(),
            tags=[fake.text(max_nb_chars=7),
                  fake.text(max_nb_chars=8),
                  fake.text(max_nb_chars=10)
                  ],
            info={"names": [fake.name() for _ in range(3)],
                  "phone_numbers": [fake.phone_number() for _ in range(3)]
                  }
        )

        return model

    invalid_meme_ids_list = [-1, 20.01, 0.1, [10], {1: 2}, "qwe", ['qwe', 'rty'], ('adsa', 213, 23.459)]
