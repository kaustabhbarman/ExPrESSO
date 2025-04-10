import hashlib
import subprocess

from expresso.idp.idp import IdentityProvider
from expresso.rp.utils import hash_for_zokrates_cli


def generate_secret():
    uid = int.to_bytes(1234567, 64, "big")

    raw = hashlib.sha256(uid).digest()
    raw += raw

    digest = hashlib.sha256(raw).digest()
    digest += digest

    return raw, digest


class RelyingParty():

    def __init__(self, idp: IdentityProvider):
        self.idp = idp
        self.token = None
        self.secret = None

    def compute_witness(self):
        preimage, digest = generate_secret()

        sig_R, sig_S = self.idp.request_token(digest)
        pk = self.idp.public_key

        hash_preimage = hash_for_zokrates_cli(preimage)
        hash_digest = hash_for_zokrates_cli(digest)
        signature_args = f"{sig_R.x} {sig_R.y} {sig_S} {pk.p.x.n} {pk.p.y.n}"

        witness_args = (hash_preimage + " " + signature_args + " " + hash_digest).split()

        subprocess.run([
            "zokrates", "compute-witness",
            "-i", "expresso/oidf/.artifacts/out",
            "-o", "expresso/rp/.artifacts/witness",
            "--circom-witness", "expresso/rp/.artifacts/out.wtns",
            "-a", *witness_args
        ])

    def generate_proof(self):
        proofPath = "expresso/rp/.artifacts/proof.json"
        subprocess.run([
            "zokrates", "generate-proof",
            "-i", "expresso/oidf/.artifacts/out",
            "-p", "expresso/oidf/.artifacts/proving.key",
            "-j", proofPath,
            "-w", "expresso/rp/.artifacts/witness",
        ])
        return proofPath