from odoo import fields,models
from . import subject_management
from . import teachers_students

class ExamModel(models.Model):
    _name = "exam.scores"
    _description = "School Exam"

    exam_name = fields.Many2one('exam.info', string = "Exam", required = True)
    student_id = fields.Many2one('teachers.students', string = "Student", required = True)
    teacher_id = fields.Many2many('teachers.students', string="Teacher", required=True) # link to school panel
    subject_id = fields.Many2one('subject.management', string="Subject") # link to subject model
    score = fields.Integer()
    