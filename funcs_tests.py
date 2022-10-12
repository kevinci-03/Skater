import unittest
from funcs import *

class TestCases(unittest.TestCase):
   def test_poundsToKG_1(self):
      self.assertAlmostEqual(poundsToKG(0), 0.0)


   def test_poundsToKG_2(self):
      self.assertAlmostEqual(poundsToKG(1), 0.453592)


   def test_poundsToKG_3(self):
      self.assertAlmostEqual(poundsToKG(2), 0.907184)
     

   def test_getMassObject_1(self):
      self.assertEqual(getMassObject('t'), 0.1)


   def test_getMassObject_2(self):
      self.assertEqual(getMassObject('p'), 1.0)


   def test_getMassObject_3(self):
      self.assertEqual(getMassObject('g'), 5.3)

   def test_getMassObject_4(self):
      self.assertEqual(getMassObject('r'), 3.0)


   def test_getMassObject_5(self):
      self.assertEqual(getMassObject('l'), 9.07)
      

   def test_getVelocityObject_1(self):
      self.assertAlmostEqual(getVelocityObject(0), 0.0)


   def test_getVelocityObject_2(self):
      self.assertAlmostEqual(getVelocityObject(3), 3.83405790)
      

   def test_getVelocityObject_3(self):
      self.assertAlmostEqual(getVelocityObject(9), 6.64078308)
      

   def test_getVelocitySkater_1(self):
      self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)
      

   def test_getVelocitySkater_2(self):
      self.assertAlmostEqual(getVelocitySkater(4, 50, 2), 25)
      

   def test_getVelocitySkater_3(self):
      self.assertAlmostEqual(getVelocitySkater(10, 54, 5), 27)
        

if __name__ == '__main__':
   unittest.main()