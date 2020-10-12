#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from cdp_backend.database import validators

from .. import test_utils

#############################################################################


@pytest.mark.parametrize(
    "router_string, expected_result",
    [
        (None, True),
        ("lorena-gonzalez", True),
        ("lorena", True),
        ("LORENA", False),
        ("gonzález", False),
        ("lorena_gonzalez", False),
        ("lorena gonzalez", False),
    ],
)
def test_check_router_string(router_string, expected_result):
    actual_result = validators.check_router_string(router_string)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "email, expected_result",
    [
        (None, True),
        ("Lorena.Gonzalez@seattle.gov", True),
        ("lorena.gonzalez@seattle.gov", True),
        ("Lorena.gov", False),
        ("Lorena@", False),
        ("Lorena@seattle", False),
        ("Lorena Gonzalez@seattle", False),
        ("Lorena.González@seattle.gov", False),
    ],
)
def test_check_email(email, expected_result):
    actual_result = validators.check_email(email)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "uri, expected_result",
    [
        (None, True),
        (__file__, True),
        ("file://does-not-exist.txt", False),
    ],
)
def test_local_check_resource_exists(uri, expected_result):
    actual_result = validators.check_resource_exists(uri)
    assert actual_result == expected_result


@pytest.mark.skipif(
    not test_utils.check_internet_available(),
    reason="No internet connection",
)
@pytest.mark.parametrize(
    "uri, expected_result",
    [
        (None, True),
        ("https://docs.pytest.org/en/latest/index.html", True),
        ("https://docs.pytest.org/en/latest/does-not-exist.html", False),
    ],
)
def test_remote_check_resource_exists(uri, expected_result):
    actual_result = validators.check_resource_exists(uri)
    assert actual_result == expected_result