#!/usr/bin/env python

"""Tests for `sample_prj` package."""

import pytest

from sample_prj import sample_prj


@pytest.fixture
def sample_fixture():
    """Setup test fixture"""
    return 1


def test_func(sample_fixture):
    """Test the sample function"""
    assert sample_prj.sample_func(1) == 2


def test_negative(sample_fixture):
    """Negative test of sample function"""
    assert sample_prj.sample_func(-2) == -1


def test_inc():
    assert sample_prj.inc(1) == 2


def test_dec():
    assert sample_prj.dec(2) == 1


def test_sum():
    assert sample_prj.sum(3, 4) == 7


def test_mult():
    assert sample_prj.mult(3, 4) == 12


def test_square():
    assert sample_prj.square(5) == 25
