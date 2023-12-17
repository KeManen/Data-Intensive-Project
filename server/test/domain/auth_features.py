from src.domain.authentication import salt_and_hash


def should_salt_and_hash_a_password():
    salted = salt_and_hash("My unique password")
    assert len(salted) == 60
