"""Setup data."""
import asyncio

from test.setup.service.dummy_create_data import CreateData


if __name__ == '__main__':
    asyncio.run(CreateData.create_dummy_data())
