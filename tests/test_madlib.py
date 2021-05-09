import pytest
from madlib_cli import __version__

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.skip
def test_version1():
    assert __version__ == '0.1.0'

