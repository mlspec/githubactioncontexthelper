"""

tests.conftest.py
~~~~~~~~~~~~~~~~~

This module is used by PyTest to detect test fixtures that are used by
multiple test modules. For more imformation on fixtures in PyTest, see
https://docs.pytest.org/en/latest/fixture.html.
"""

import json
from typing import Any, Dict, List

import pytest

from githubactioncontexthelper import load_context, save_context

@pytest.fixture
def save_context_test() -> None:
    """Test printing out context data.

    :return: None
    :rtype: None
    """

    a = save_context('a')

    raise NotImplemented

@pytest.fixture
def load_context_test() -> None:
    """Test printing out context data.

    :return: None
    :rtype: None
    """

    a = load_context()

    raise NotImplemented

