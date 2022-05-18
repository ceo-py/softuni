# zero test
from project.person import Person
from project.child import Child
import unittest

class Tests(unittest.TestCase):
   def test(self):
      person = Person("Peter", 25)
      child = Child("Peter Junior", 5)
      self.assertEqual(person.name, "Peter")
      self.assertEqual(person.age, 25)
      self.assertEqual(child.__class__.__bases__[0].__name__, "Person")

if __name__ == "__main__":
   unittest.main()