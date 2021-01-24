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

def save_context(context) -> None:
    """Test printing out context data.

    :return: None
    :rtype: None
    """

    raise NotImplemented

@pytest.fixture
def supply_curve() -> SupplyCurve:
    """Return a supply curve for use with tests.

    :return: A Supply curve.
    :rtype: SupplyCurve
    """

    supply_demand_data = load_test_data()
    return SupplyCurve(supply_demand_data)


@pytest.fixture
def demand_curve() -> DemandCurve:
    """Return a demand curve for use with tests.

    :return: A demand curve.
    :rtype: DemandCurve
    """

    supply_demand_data = load_test_data()
    return DemandCurve(supply_demand_data)
