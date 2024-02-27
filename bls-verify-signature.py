from py_ecc import bls
import sys

from eth_typing import (
    BLSPubkey,
    BLSSignature,
)

public_key = bytes.fromhex(sys.argv[1])
signature = bytes.fromhex(sys.argv[2])
message = sys.argv[3]
message_bytes = message.encode()

print(f":: verified signature: {bls.ciphersuites.G2ProofOfPossession.Verify(BLSPubkey(public_key), message_bytes, BLSSignature(signature))}")