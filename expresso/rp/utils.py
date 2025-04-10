def hash_for_zokrates_cli(msg):
    "Writes the input arguments for verifyEddsa in the ZoKrates stdlib to file."
    M0 = msg.hex()[:64]
    M1 = msg.hex()[64:]
    b0 = [str(int(M0[i:i + 8], 16)) for i in range(0, len(M0), 8)]
    b1 = [str(int(M1[i:i + 8], 16)) for i in range(0, len(M1), 8)]
    return " ".join(b0 + b1)