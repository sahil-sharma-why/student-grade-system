import unittest
from student_grade_system import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Sahil")

    def test_initial_average_zero(self):
        self.assertEqual(self.student.calculate_average(), 0)

    def test_add_valid_grade(self):
        self.student.add_grade(80)
        self.assertEqual(self.student.grades, [80])

    def test_add_invalid_grade(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(150)

    def test_average_calculation(self):
        self.student.add_grade(80)
        self.student.add_grade(90)
        self.assertEqual(self.student.calculate_average(), 85)

    def test_pass_status_true(self):
        self.student.add_grade(60)
        self.assertTrue(self.student.has_passed())

    def test_pass_status_false(self):
        self.student.add_grade(20)
        self.assertFalse(self.student.has_passed())

    def test_zero_grade(self):
        """Test that adding a zero grade works correctly (failing case)."""
        self.student.add_grade(0)
        self.assertEqual(self.student.calculate_average(), 0)
        self.assertFalse(self.student.has_passed())

    def test_full_marks(self):
        """Test that 100 as a grade gives a passing average."""
        self.student.add_grade(100)
        self.assertEqual(self.student.calculate_average(), 100)
        self.assertTrue(self.student.has_passed())

    def test_multiple_grades(self):
        """Test average with multiple grades."""
        self.student.add_grade(40)
        self.student.add_grade(60)
        self.student.add_grade(80)
        self.assertEqual(self.student.calculate_average(), 60)
        self.assertTrue(self.student.has_passed())

    def test_empty_grades(self):
        """Test that average is 0 when no grades are added."""
        empty_student = Student("Bob")
        self.assertEqual(empty_student.calculate_average(), 0)
        self.assertFalse(empty_student.has_passed())
