from expresso.idp.idp import IdentityProvider
from expresso.oidf.oidf import OpenIdFoundation
from expresso.rp.rp import RelyingParty

def main():
    oidf = OpenIdFoundation()
    idp = IdentityProvider()
    rp = RelyingParty(idp)

    oidf.compile()
    oidf.setup()

    rp.compute_witness()
    proof = rp.generate_proof()
    idp.verify(proof)

if __name__ == "__main__":
    main()