import bcrypt


def salt_and_hash(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode(encoding="utf-8")


def validate(password: str, candidate: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), candidate.encode("utf-8"))
