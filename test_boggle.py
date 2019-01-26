import unittest
import boggle
from string import ascii_uppercase

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
        
    def test_grid_contains_uppcs_letters(self):
        
        """
        Ensure each coordinate within the grid structure
        contains letters
        """
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    
    def test_neighbours_of_a_position(self):
        """
        Ensure a position has 8 neighbour
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
        
    def test_all_grid_neighbours(self):
        
        """
        Ensure that all grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid) #creates a new list from the dictionary`s key
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
            
            
    def test_converting_path_to_word(self):
        """
        Ensure that paths can be converted to word
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
        
    def test_search_grid_for_words(self):
        
        """
        Ensure certain patterns can be found in a path_to_word
        """
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)