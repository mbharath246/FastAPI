from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash_password(password):
    return pwd_cxt.hash(password)

def verify_hash_password(plain_password, hash_passowrd):
    return pwd_cxt.verify(plain_password, hash_passowrd)