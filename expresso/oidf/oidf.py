import subprocess

class OpenIdFoundation:
    def __init__(self):
        pass

    def compile(self):
        subprocess.run(
            [
                "zokrates", "compile",
                "-i", "expresso/oidf/circuit/eddsa.zok",
                "-o","expresso/oidf/.artifacts/out",
                "-r", "expresso/oidf/.artifacts/out.r1cs",
                "-s", "expresso/oidf/.artifacts/abi.json"
            ],
        )

    def setup(self):
        subprocess.run(
            [
                "zokrates", "setup",
                "-i", "expresso/oidf/.artifacts/out",
                "-p", "expresso/oidf/.artifacts/proving.key",
                "-v", "expresso/oidf/.artifacts/verification.key"
            ],
        )
