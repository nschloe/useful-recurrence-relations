"""
exp(-(x_1^2 + ... + x_n^2)/2) / sqrt(2*pi) ** n
"""
import random
from math import gamma, pi, sqrt

import pytest
from helpers import prod

import ndim


@pytest.mark.parametrize("n", range(10))
def test_volume(n):
    ref = 1
    tol = 1.0e-14
    assert abs(ref - ndim.enr2.volume(n, "probabilists")) < abs(ref) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_monomial(n):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = prod(
        (1 + (-1) ** kk) / 2 * 2 ** ((kk + 1) / 2) / sqrt(2 * pi) * gamma((kk + 1) / 2)
        for kk in k
    )

    tol = 1.0e-14
    assert abs(ref - ndim.enr2.integrate_monomial(k, "probabilists")) < abs(ref) * tol
