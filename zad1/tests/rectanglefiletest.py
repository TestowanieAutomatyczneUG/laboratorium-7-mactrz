import unittest
from src.sample.Rectangle import *

class RectangleParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/rectangle_data_test")
      tmpRectangle = Rectangle()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            inp, second, result = int(data[0]),int(data[1]), int(data[2].strip("\n"))
            self.assertEqual(tmpRectangle.surface(inp, second), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()