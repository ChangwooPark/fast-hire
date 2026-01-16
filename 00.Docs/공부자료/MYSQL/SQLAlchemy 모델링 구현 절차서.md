# 📑 SQLAlchemy 모델링 구현 절차서 (Step-by-Step Guide)

이 문서는 설계된 데이터베이스 스키마를 바탕으로 FastAPI 환경에서 SQLAlchemy ORM을 구현하는 표준 절차를 정리한 가이드입니다.

---

## 1. 환경 준비 및 패키지 설치 (Environment)

가상환경(venv)이 활성화된 상태에서 DB 연결 및 비동기 처리를 위한 필수 라이브러리를 설치합니다.

```bash
# SQLAlchemy: 파이썬 표준 ORM
# aiomysql: MySQL 비동기 연결을 위한 드라이버
# cryptography: MySQL 8.0 이상의 보안 인증 방식을 지원하기 위한 패키지
pip install sqlalchemy aiomysql cryptography
```

---

## 2. 데이터베이스 연결 및 세션 설정 (`database.py`)
애플리케이션과 MySQL 사이의 통로를 만드는 과정입니다. FastAPI의 비동기 성능을 활용하기 위해 `AsyncSession`을 설정합니다.

1. DB_URL 설정: `mysql+aiomysql://계정:비번@호스트:포트/DB명` 형식으로 작성합니다.

2. Engine 생성: `create_async_engine`을 통해 비동기 엔진을 생성합니다.

3. Sessionmaker: 실제 DB 작업을 수행할 개별 세션을 생성하는 공장을 설정합니다.

4. Base 선언: 모든 테이블 모델이 상속받을 기초 클래스인 `declarative_base()`를 생성합니다

---

## 3. 공통 타입 및 Enum 정의 (`models.py`)
데이터의 정합성을 높이기 위해 공통으로 사용될 상수를 정의합니다.

1. Enum 클래스: 사용자 역할(seeker, recruiter) 등 정해진 값만 허용해야 하는 컬럼을 위해 파이썬 enum.Enum을 상속받아 정의합니다.

2. Base 상속 준비: database.py에서 정의한 Base 클래스를 임포트하여 모델 클래스 정의 시 상속받습니다.

---

## 4. 테이블 모델 클래스 구현 (`models.py`)
SQL 설계서의 각 테이블을 파이썬 클래스로 변환합니다.

1. 클래스 정의: __tablename__을 통해 실제 DB 테이블 이름을 명시합니다.

2. 컬럼 매핑: Column, BigInteger, String 등을 사용하여 SQL 타입을 매핑합니다.

3. 외래 키 설정: ForeignKey("부모테이블.id", ondelete="CASCADE")를 사용하여 관계를 맺습니다.

4. 자동 시간 기록: * server_default=func.now(): 생성 시 DB 시각 자동 기록

* onupdate=func.now(): 수정 시 DB 시각 자동 갱신

---

## 5. 고급 제약 조건 설정 (`__table_args__`)
단일 컬럼 정의 외에 복합적인 규칙이 필요한 경우 클래스 내 `__table_args__`를 사용합니다.

1. UniqueConstraint: 여러 컬럼의 조합이 유일해야 할 때 설정합니다. (예: 특정 유저가 특정 공고에 방을 하나만 만들 수 있도록 제한)

2. Index: 조회 성능 최적화를 위해 인덱스를 생성합니다. 특히 채팅 메시지처럼 `(room_id, created_at)` 순서의 조회가 빈번한 경우 복합 인덱스를 설정합니다.

---

## 6. DB 반영 및 세션 의존성 주입
모델 작성이 완료되면 이를 실제 서비스에 연결합니다.

1. 테이블 생성: Base.metadata.create_all을 사용하거나 마이그레이션 도구(Alembic)를 통해 DB에 테이블을 생성합니다.

2. get_db 함수: FastAPI의 Depends를 사용하여 API 호출 시마다 세션을 생성하고 반환(Yield)하는 의존성 함수를 작성합니다.