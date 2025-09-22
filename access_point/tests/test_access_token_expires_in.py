from odoo.tests.common import SingleTransactionCase


class TestTokenExpiry(SingleTransactionCase):
    def test_access_token_expires_in(self) -> None:
        expires_in = self.env.ref("access_token_expires_in")
        self.assertEqual(expires_in.value, 31536000)
