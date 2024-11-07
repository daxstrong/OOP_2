import unittest
import calc_tests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(calc_tests.CalcBasicTests))
calcTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(calc_tests.CalcExTests))

print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
