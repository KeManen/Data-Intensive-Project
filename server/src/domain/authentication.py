import bcrypt


def salt_and_hash(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    print(hashed)
    return hashed.decode(encoding="utf-8")
