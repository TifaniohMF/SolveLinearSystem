import unittest
from main import solve_linear_system
from decomposition.lu import decomposition_lu
from decomposition.qr import decomposition_qr
from decomposition.cholesky import decomposition_cholesky
from solver import solve_system

class testDecomposition(unittest.TestCase):
	def test_decomposition(self):
		self.assertEqual(solve_linear_system([[1,1],[1,-1]], [1,1], method='QR'), [1,0])
		self.assertEqual(solve_linear_system([[1,1],[0,1]], [1,1], method='LU'), [0,1])
		self.assertEqual(solve_linear_system([[1,0],[0,1]], [1,1], method='Cholesky'), [1,1])
