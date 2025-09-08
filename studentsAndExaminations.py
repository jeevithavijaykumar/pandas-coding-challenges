# Table: Students
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| student_id    | int     |
#| student_name  | varchar |
#+---------------+---------+
# student_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID and the name of one student in the school.


# Table: Subjects
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key (column with unique values) for this table.
# Each row of this table contains the name of one subject in the school.


# Table: Examinations
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.

import pandas as pd
import numpy as np

class Solution:
    def students_and_examinations(self, students, subjects, examinations):

        df = students.merge(subjects, how = 'cross')
        df_exam = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
        df_exam['attended_exams'] = df_exam['attended_exams'].fillna(0).astype(int)
        result = df.merge(df_exam, how = 'left', on = ['student_id','subject_name'])
        result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
        return result[['student_id','student_name','subject_name','attended_exams']].sort_values(by=['student_id','subject_name'])


students = pd.DataFrame({'student_id': [1,2,3],
                         'student_name': ['Alice','Bob', 'Charlie']})

subjects = pd.DataFrame({'subject_name': ['Math','Physics']})

examinations = pd.DataFrame({'student_id': [1, 1, 2, 3, 3, 3],
                            'subject_name': ['Math', 'Physics', 'Math', 'Math', 'Physics', 'Physics']})

s= Solution()
output = s.students_and_examinations( students, subjects, examinations)
print(output)