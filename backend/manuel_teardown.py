"""Teardown data."""
import asyncio

from test.setup.service.dummy_destroy_data import DestroyData


if __name__ == '__main__':
    asyncio.run(DestroyData.destroy_data())
