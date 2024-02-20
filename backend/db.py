from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(
    "postgresql+asyncpg://admin:thisisatest@127.0.0.1:5432/alfredo",
    echo=True,
)

# async_sessionmaker: a factory for new AsyncSession objects.
# expire_on_commit - don't expire objects after transaction commit
async_session = async_sessionmaker(engine, expire_on_commit=False)