from contextlib import asynccontextmanager
from database import get_db, engine, Base
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, security


app = FastAPI()


# cors설정
origins = [
    "http://localhost:5173",  # React 기본 포트
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 서버 기동 시 실행: 테이블 생성
    async with engine.begin() as conn:
        # 이 명령은 이미 테이블이 존재하면 생성하지 않고 넘어갑니다.
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 서버 종료 시 실행 (필요한 경우)

app = FastAPI(lifespan=lifespan, title="FastHire API")

@app.get("/")
async def root():
    return {"message": "FastHire API 서버가 정상적으로 작동 중이며, DB 테이블이 생성되었습니다."}


@app.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # 1. 이미 존재하는 이메일인지 확인
    result = await db.execute(select(models.User).where(models.User.email == user_data.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 등록된 이메일입니다."
        )

    # 2. 비밀번호 해싱 및 유저 객체 생성
    new_user = models.User(
        email=user_data.email,
        hashed_password=security.hash_password(user_data.password),
        nickname=user_data.nickname,
        role=user_data.role
    )

    # 3. DB 저장
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user