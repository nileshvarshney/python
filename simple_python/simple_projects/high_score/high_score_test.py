import unittest
from high_score import high_score, last_score, top_three_scores

class ScoreTest(unittest.TestCase):
    def test_high_score(self):
        scores = [90,100,20]
        self.assertEqual(high_score(scores),100)

    def test_last_score(self):
        scores = [90,100,20]
        expected = 20
        self.assertEqual(last_score(scores), expected)

    def test_top_three_scores(self):
        scores = [90,100,20, 200, 43, 21]
        expected = [200,100,90]
        self.assertListEqual(top_three_scores(scores), expected)

if __name__ == "__main__":
    unittest.main()