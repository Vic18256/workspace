import unittest
import boggle

class test_boggle(unittest.TestCase):
    
    """ 
    Our test suite for boggle solver
    
    """
    def test_can_create_an_empty_grid(self):
        
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_width_times_height(self):
        """
        Test is to ensure thta width * height is equal to grid size
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)
   
    def test_grid_coordinate(self):
        """
        Test to see if coordinates (0,0) exist within a 2*2 grid
        """
        grid = boggle.make_grid(2,2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)