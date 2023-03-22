
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db(db_session: AsyncSession) -> AsyncSession:
    async with db_session() as session:
        return session
