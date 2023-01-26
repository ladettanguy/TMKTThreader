from tmktthreader import Threader
from threading import Event


def test_thearder():
    e = Event()

    @Threader
    def func(event: Event):
        event.set()

    t = func(e)
    t.join()
    assert e.is_set()
