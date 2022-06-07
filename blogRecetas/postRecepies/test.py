import unittest
from django.test import TestCase


unittest.main()

TestCase.assertEqual(1, 1)
TestCase.assertTrue(True)
TestCase.assertFalse(False)
TestCase.assertIsNone(None)
TestCase.assertIsNotNone(1)
TestCase.assertIsInstance(1, int)
TestCase.assertNotEqual(1, 2)
TestCase.assertNotEqual(1, 1)
TestCase.assertNotEqual(1, None)
TestCase.assertNotEqual(1, True)