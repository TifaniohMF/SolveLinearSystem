import numpy as np
import pytest
from main import solve_linear_system
from decomposition.lu import decomposition_lu
from decomposition.cholesky import decomposition_cholesky
from decomposition.qr import decomposition_qr
from solver import solve_system
from diagnostics import build_certificate, validate_system


def test_lu_solve_system():
    A = np.array([[4.0, 3.0], [6.0, 3.0]])
    b = np.array([10.0, 12.0])

    L, U = decomposition_lu(A)
    x = solve_system(L, U, b, kind='LU')

    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected)


def test_cholesky_solve_system():
    A = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])

    L = decomposition_cholesky(A)
    x = solve_system(L, L.T, b, kind='Cholesky')

    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected)


def test_qr_solve_system():
    A = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    b = np.array([7.0, 8.0, 9.0])

    Q, R = decomposition_qr(A)
    y = np.dot(Q.T, b)
    x = solve_system(None, R, y, kind='QR')

    assert np.allclose(np.dot(A, x), b)


def test_solve_linear_system_all_methods():
    A = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])

    for method in ['LU', 'Cholesky', 'QR']:
        x = solve_linear_system(A, b, method=method)
        assert np.allclose(np.dot(A, x), b)


def test_certificate_reports_small_residual():
    A = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    x, certificate = solve_linear_system(A, b, method='Cholesky', return_certificate=True)

    assert np.allclose(A @ x, b)
    assert certificate['residual_norm_inf'] < 1e-12
    assert certificate['reliable'] is True


def test_validation_rejects_non_finite_and_non_square_inputs():
    with pytest.raises(ValueError, match="square"):
        validate_system([[1.0, 2.0]], [1.0])
    with pytest.raises(ValueError, match="finite"):
        validate_system([[np.nan]], [1.0])


def test_certificate_flags_ill_conditioned_matrix():
    A = np.array([[1.0, 1.0], [1.0, 1.0 + 1e-14]])
    b = np.array([2.0, 2.0])
    x = np.linalg.solve(A, b)
    certificate = build_certificate(A, b, x, 'numpy')

    assert 'matrix is ill-conditioned' in certificate['warnings']
