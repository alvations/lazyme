import sys
import time

import pytest

from lazyme.timing import retry


def test_retry_eventually_succeeds():
    calls = {"n": 0}

    @retry(ValueError, tries=3, delay=0, backoff=1)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError("nope")
        return "ok"

    assert flaky() == "ok"
    assert calls["n"] == 2


def test_retry_gives_up():
    @retry(ValueError, tries=2, delay=0, backoff=1)
    def always_fails():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always_fails()


@pytest.mark.skipif(sys.platform == "win32", reason="SIGALRM not available on Windows")
def test_timeout_raises():
    from lazyme.timing import timeout
    with pytest.raises(TimeoutError):
        with timeout(seconds=1):
            time.sleep(3)


@pytest.mark.skipif(sys.platform == "win32", reason="SIGALRM not available on Windows")
def test_timeout_noop_when_fast():
    from lazyme.timing import timeout
    with timeout(seconds=5):
        pass
