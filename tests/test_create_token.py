from endpoints.create_token import CreateToken


class TestCreateToken:

    def test_create_token(self):
        self.token_creator = CreateToken()
        self.token_creator.create_token()
