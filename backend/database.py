from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL 연결 정보 (사용자명, 비밀번호, 호스트, DB이름을 본인 환경에 맞게 수정하세요)
# 예: mysql+aiomysql://root:password@localhost:3306/fast_hire_db
DB_URL = "mysql+aiomysql://root:password@localhost:3306/fast_hire_db"

engine = create_async_engine(DB_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# DB 세션 의존성 주입을 위한 함수
async def get_db():
    async with async_session() as session:
        yield session