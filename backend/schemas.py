from pydantic import BaseModel, EmailStr
from models import UserRole
from datetime import datetime

# 회원가입 시 받을 데이터
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    nickname: str
    role: UserRole

# 클라이언트에 응답할 데이터 (비밀번호 제외)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    nickname: str
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True