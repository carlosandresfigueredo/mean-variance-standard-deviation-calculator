import unittest
import numpy as np
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate_mean(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['mean']
        expected = [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
        self.assertEqual(actual[0], expected[0], "Expected different mean values.")
        self.assertEqual(actual[1], expected[1], "Expected different mean values.")
        self.assertAlmostEqual(actual[2], expected[2], places=1, msg="Expected different mean values.")

    def test_calculate_variance(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['variance']
        expected = [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]
        np.testing.assert_almost_equal(actual[0], expected[0], 1, "Expected different variance values.")
        np.testing.assert_almost_equal(actual[1], expected[1], 1, "Expected different variance values.")
        self.assertAlmostEqual(actual[2], expected[2], places=1, msg="Expected different variance values.")

    def test_calculate_std(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['standard deviation']
        expected = [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]
        np.testing.assert_almost_equal(actual[0], expected[0], 1, "Expected different standard deviation values.")
        np.testing.assert_almost_equal(actual[1], expected[1], 1, "Expected different standard deviation values.")
        self.assertAlmostEqual(actual[2], expected[2], places=1, msg="Expected different standard deviation values.")

    def test_calculate_max(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['max']
        expected = [[6, 7, 8], [2, 5, 8], 8]
        self.assertEqual(actual, expected, "Expected different max values.")

    def test_calculate_min(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['min']
        expected = [[0, 1, 2], [0, 3, 6], 0]
        self.assertEqual(actual, expected, "Expected different min values.")

    def test_calculate_sum(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])['sum']
        expected = [[9, 12, 15], [3, 12, 21], 36]
        self.assertEqual(actual, expected, "Expected different sum values.")

    def test_calculate_value_error(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", mean_var_std.calculate, [0, 1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    unittest.main()