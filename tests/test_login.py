from tasks import login

data = {
    "user": "stori.prueba8@yopmail.com",
    "password": "Holamundo1",
}


def test_login(driver):
    login.with_data(driver, data)
