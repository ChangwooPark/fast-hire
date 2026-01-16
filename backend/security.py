import bcrypt

def hash_password(password: str) -> str:
    # 1. 평문 비밀번호를 바이트로 변환
    pwd_bytes = password.encode('utf-8')
    # 2. 솔트(Salt) 생성 및 해싱
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # 3. DB 저장을 위해 문자열로 디코딩하여 반환
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # DB의 해시된 문자열을 바이트로 변환 후 검증
    return bcrypt.checkpw(
        plain_password.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )