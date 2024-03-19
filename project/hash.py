from passlib.context import CryptContext

new_pwd = CryptContext(schemes=["bcrypt"],deprecated="auto")


def hashed(password):
    return new_pwd.hash(password)


def hash_verify(hashed_password, plain_password):     
    return new_pwd.verify(hash = hashed_password, secret = plain_password)