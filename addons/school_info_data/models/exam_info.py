from sre_parse import State
from odoo import fields, models

class ExamManagement(models.Model):
    _name = 'exam.info'
    _description = 'Test for exam'


    name = fields.Char(required = True)
    months = fields.Selection([('jan', 'January'), ('feb', 'February'), ('march', 'March'), ('apri', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sept', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'December')], string = 'Months', required = True)
    duration = fields.Char(required = True)
    teacher_id = fields.Many2one('teachers.students', string = 'Tec_id')
    exam_date_start = fields.Date(required = True)
    exam_date_end = fields.Date(required = True)
    student_id = fields.Many2many('teachers.students', string = "Students")
    subject_ids = fields.Many2many('subject.management', string = "Subjects")