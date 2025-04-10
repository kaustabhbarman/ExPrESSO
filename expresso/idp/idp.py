import subprocess

from zokrates_pycrypto.eddsa import PrivateKey, PublicKey

class IdentityProvider():

    def __init__(self):
        self.private_key = PrivateKey.from_rand()
        self.public_key = PublicKey.from_private(self.private_key)

    def sign(self, message):
        return self.private_key.sign(message)

    def request_token(self, message):
        return self.sign(message)

    def verify(self, proof):
        # TODO check nonce

        subprocess.run([
            "zokrates", "verify",
            "-j", proof,
            "-v", "expresso/oidf/.artifacts/verification.key",
        ])