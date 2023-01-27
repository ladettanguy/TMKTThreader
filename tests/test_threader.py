from tmktthreader import Threader, AsyncThreader
from threading import Event


def test_thearder():
    e = Event()

    @Threader
    def func(event: Event):
        event.set()

    t = func(e)
    t.join()
    assert e.is_set()


def test_async_threader():
    e = Event()

    @AsyncThreader
    async def func(event: Event):
        event.set()

    t = func(e)
    t.join()
    assert e.is_set()