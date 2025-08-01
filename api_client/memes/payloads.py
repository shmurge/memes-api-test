from faker import Faker
from api_client.memes.models.request_memes_models import RequestCreateMemeModel

fake = Faker()


class MemesPayloads:

    create_meme = RequestCreateMemeModel(
        text=fake.text(),
        url=fake.url(),
        tags=[fake.text(max_nb_chars=5),
              fake.text(max_nb_chars=6),
              fake.text(max_nb_chars=7)
              ],
        info={"colors": [fake.color(),
                         fake.color()
                         ],
              "names": [fake.name(),
                        fake.name()
                        ]
              }
    )