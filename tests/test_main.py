#!/usr/bin/env python3
"""
Tests for the Hello World application.
"""
import sys
import os
import unittest
from io import StringIO

# Add the src directory to the path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import hello_world, main


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello world application."""
    
    def test_hello_world_function(self):
        """Test that hello_world() returns the correct message."""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
    
    def test_main_function_output(self):
        """Test that main() prints the correct message."""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
