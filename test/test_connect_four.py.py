import unittest
from connect_four import ConnectFour 
class TestConnectFour(unittest.TestCase):

    def setUp(self):
        """Setup a new game for each test"""
        self.game = ConnectFour()

    def test_initial_board(self):
        """Test that the initial board is set up correctly"""
        self.assertEqual(len(self.game.board), 6) # assuming 6 rows
        self.assertTrue(all(len(row) == 7 for row in self.game.board)) # assuming 7 columns

    # Adding more tests here to test game functionality, like adding tokens, checking for a win, etc.

if __name__ == '__main__':
    unittest.main()
