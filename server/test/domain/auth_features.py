from src.domain.authentication import salt_and_hash, validate


def should_salt_and_hash_a_password():
    password = "My unique password"
    salted = salt_and_hash(password)
    assert validate(password, salted)
