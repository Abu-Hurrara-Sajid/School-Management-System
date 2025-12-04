import unittest

import school_managment as sm


class StudentTests(unittest.TestCase):
    def test_student_to_values(self):
        student = sm.Student("Ali", "Khan", "2006-03-14", "9", "555-1234")
        self.assertEqual(
            student.to_values(),
            ("Ali", "Khan", "2006-03-14", "9", "555-1234"),
        )


class GradeTests(unittest.TestCase):
    def test_performance_percentages(self):
        record = sm.PerformanceRecord(1, "Math", "Quiz", 18, 20, "T1")
        self.assertEqual(record.percentage(), 90.0)
        zero_total = sm.PerformanceRecord(1, "Science", "Lab", 10, 0, "T1")
        self.assertEqual(zero_total.percentage(), 0.0)

    def test_grade_from_percentage(self):
        self.assertEqual(sm.grade_from_percentage(95), "A")
        self.assertEqual(sm.grade_from_percentage(82), "B")
        self.assertEqual(sm.grade_from_percentage(74), "C")
        self.assertEqual(sm.grade_from_percentage(66), "D")
        self.assertEqual(sm.grade_from_percentage(12), "F")
        self.assertEqual(sm.grade_from_percentage(0), "N/A")


if __name__ == "__main__":
    unittest.main()
