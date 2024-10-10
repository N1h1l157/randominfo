from flask import Flask, render_template
from leetgen.leet import generate_leet
from passgen.password import generate_password_1
from passgen.password import generate_password_2
from othergen.name_random import (
    generate_qq_name,
    generate_chinese_name,
    generate_english_name,
    generate_english_place,
    generate_japanese_name,
)
from othergen.data_random import (
    generate_random_email,
    generate_random_phone,
    generate_random_birth,
)
from othergen.city_random import get_city_coordinates

import uuid

app = Flask(__name__)


@app.route("/")
def index():
    leet = generate_leet()
    pass1 = generate_password_1(10)

    pass2 = generate_password_2(10)

    name_en = generate_english_name()
    name_zh = generate_chinese_name()
    name_qq = generate_qq_name()
    name_jap = generate_japanese_name()

    email = generate_random_email()
    phone = generate_random_phone()
    birth = generate_random_birth()

    place_en = generate_english_place()
    place_zh, coordinates = get_city_coordinates()

    return render_template(
        "index.html",
        name_zh=name_zh,
        name_qq=name_qq,
        name_jap=name_jap,
        name_en=name_en,
        leet=leet,
        pass1=pass1,
        pass2=pass2,
        place_en=place_en,
        place_zh=place_zh,
        coordinates=coordinates,
        email=email,
        phone=phone,
        birth=birth,
        uuid=str(uuid.uuid4()),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
