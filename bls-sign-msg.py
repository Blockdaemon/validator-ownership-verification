from py_ecc import bls
import sys

# Determine the validator public key
public_key = bls.ciphersuites.G2ProofOfPossession.SkToPk(int(sys.argv[1], 16))
print(f":: public key from private key: {public_key.hex()}")

# Set the message
message_bytes = sys.argv[2].encode()

# Sign the message
print(f":: signature: {bls.ciphersuites.G2ProofOfPossession.Sign(int(sys.argv[1], 16), message_bytes).hex()}")
