import unittest as ut


class TestSort(ut.TestCase):
    """Functiontest"""

    def setUp(self):
        self.nlist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        self.slist = sorted(self.nlist)

    def test_functionality(self):
        for i in range(1, len(self.slist)):
            self.failIf(self.slist[i - 1] > self.slist[i])

    def testlenght(self):
        self.assertAlmostEquals(len(self.nlist), len(self.slist))

    def testbeginning(self):
        self.assertEqual(min(self.slist), self.slist[0])


suit = ut.TestSuite()

TestSort("test_functionality")
suit.addTest(TestSort("test_functionality"))
suit.addTest(TestSort("testlenght"))
suit.addTest(TestSort("testbeginning"))
testrunner = ut.TextTestRunner(verbosity=2)
testrunner.run(suit)
