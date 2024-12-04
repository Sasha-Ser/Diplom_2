class Data:

    BASE_URL = ' https://stellarburgers.nomoreparties.site/api/'
    REGISTER_URL = 'auth/register'
    LOGIN_URL = 'auth/login'
    USER_URL = 'auth/user'
    CREATE_ORDER_URL = 'orders'
    LIST_ORDER_URL = 'orders/all'


    USER_REGISTER = {
        "email": "sergeev-diploma-api@yandex.ru",
        "password": "password",
        "name": "Username"
        }

    USER_REGISTER_WRONG_EMAIL = {
        "email": "007sergeev-diploma-api@yandex.ru",
        "password": "password"
        }

    USER_REGISTER_WRONG_PASS = {
        "email": "sergeev-diploma-api@yandex.ru",
        "password": "1password"
        }

    USER_REGISTER_WITHOUT_EMAIL = {
        "password": "password",
        "name": "Username"
        }

    USER_REGISTER_WITHOUT_PASS = {
        "email": "sergeev-diploma-api@yandex.ru",
        "name": "Username"
        }

    USER_REGISTER_WITHOUT_NAME = {
        "email": "sergeev-diploma-api@yandex.ru",
        "password": "password"
        }

    USER_NEW_EMAIL = {
        "email": "23sergeev-diploma-api@yandex.ru",
        "password": "password",
        "name": "Username"
    }


    USER_NEW_NAME = {
        "email": "sergeev-diploma-api@yandex.ru",
        "password": "password",
        "name": "Username1"
    }

    FULL_BURGER = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa72"]
    }

    BURGER_WITHOUT_BRED = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa72"]
    }

    BURGER_WITHOUT_FILLING = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72"]
    }

    BURGER_WITHOUT_SOUCE = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    EMPTY_BURGER = {
        "ingredients": []
    }

    BURGER_WRONG_HASH_BREAD = {
        "ingredients": ["61c0c571d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa72"]
    }

    BURGER_WRONG_HASH_FILLING = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f2001bdaaa6f", "61c0c5a71d1f82001bdaaa72"]
    }

    BURGER_WRONG_HASH_SOUCE = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d182001bdaaa72"]
    }

    RESPONSE_TEXT_SUCCESS = '"success":true'
    RESPONSE_TEXT_FALSE_FOR_INGREDIENT = '{"success":false,"message":"Ingredient ids must be provided"}'
    RESPONSE_TEXT_SERVER_ERROR = 'Internal Server Error'
    RESPONSE_TEXT_CREATE_USER_SUCCESS= f'"email":"{USER_REGISTER['email']}","name":"{USER_REGISTER['name']}"'
    RESPONSE_TEXT_EXISTING_USER = '{"success":false,"message":"User already exists"}'
    RESPONSE_TEXT_WITHOUT_REQUIRED_FIELD = '{"success":false,"message":"Email, password and name are required fields"}'
    RESPONSE_TEXT_INCORRECT_PASS_OR_EMAIL = '{"success":false,"message":"email or password are incorrect"}'
    RESPONSE_TEXT_MANDATORY_REGISTRATION = '{"success":false,"message":"You should be authorised"}'
