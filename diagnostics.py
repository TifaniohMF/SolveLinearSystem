"""Numerical diagnostics for linear-system solves."""

import numpy as np


def validate_system(A, b):
    """Return normalized inputs or raise a useful validation error."""
    matrix = np.asarray(A, dtype=float)
    vector = np.asarray(b, dtype=float)

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A must be a square two-dimensional matrix")
    if vector.ndim != 1 or vector.shape[0] != matrix.shape[0]:
        raise ValueError("b must be a vector with one entry per row of A")
    if not np.isfinite(matrix).all() or not np.isfinite(vector).all():
        raise ValueError("A and b must contain only finite values")
    return matrix, vector


def build_certificate(A, b, x, method):
    """Build an auditable numerical certificate for a computed solution."""
    residual = A @ x - b
    scale = np.linalg.norm(A, ord=np.inf) * np.linalg.norm(x, ord=np.inf)
    scale += np.linalg.norm(b, ord=np.inf)
    backward_error = np.linalg.norm(residual, ord=np.inf) / max(scale, 1.0)
    condition = float(np.linalg.cond(A))

    warnings = []
    if not np.isfinite(condition) or condition > 1e12:
        warnings.append("matrix is ill-conditioned")
    if backward_error > 1e-10:
        warnings.append("large backward error")

    return {
        "method": method,
        "residual_norm_inf": float(np.linalg.norm(residual, ord=np.inf)),
        "backward_error": float(backward_error),
        "condition_estimate": condition,
        "rank": int(np.linalg.matrix_rank(A)),
        "warnings": warnings,
        "reliable": not warnings,
    }