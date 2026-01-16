from sqlalchemy import Column, BigInteger, String, Text, Boolean, DateTime, ForeignKey, Enum, Index, UniqueConstraint
from sqlalchemy.sql import func
from database import Base
import enum

class UserRole(str, enum.Enum):
    seeker = "seeker"
    recruiter = "recruiter"

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    nickname = Column(String(50), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    owner_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    salary = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class ChatRoom(Base):
    __tablename__ = "chat_rooms"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    post_id = Column(BigInteger, ForeignKey("job_posts.id", ondelete="CASCADE"), nullable=False)
    seeker_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    recruiter_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # 중복 생성 방지 제약 조건 (post_id + seeker_id 유니크)
    __table_args__ = (
        UniqueConstraint('post_id', 'seeker_id', name='unique_post_seeker'),
    )

class Message(Base):
    __tablename__ = "messages"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    room_id = Column(BigInteger, ForeignKey("chat_rooms.id", ondelete="CASCADE"), nullable=False)
    sender_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # 성능 최적화를 위한 복합 인덱스 (방별 시간순 조회)
    __table_args__ = (
        Index('idx_room_created', 'room_id', created_at.desc()),
    )