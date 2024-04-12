import asyncio
import asyncpg
from data import config


class Database:
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
        asyncpg.create_pool(
            user=config.PGUSER,
            database=config.DBNAME,
            password=config.PGPASSSEORD,
            host=config.IP,
            port=config.DBPORT,
            loop=loop
            )
        )