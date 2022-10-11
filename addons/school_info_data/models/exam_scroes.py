import string
from sys import api_version
from odoo import fields,models,api
from . import subject_management

class ExamModel(models.Model):
    _name = "exam.scores"
    _description = "School Exam"

    subject_ids = fields.One2many('exams.marks','exam_id', string="Select Subject")
    student_ids = fields.Many2one('teachers.students', string="Students")
    exam_ids = fields.Many2one('exam.info', string = "Exam")
    teacher_id = fields.Many2one('teachers.students', string = 'Tec_id', related='exam_ids.teacher_id')

class SubjectInherit(models.Model):
    _name = 'exams.marks'

    subject_id = fields.Many2one('subject.management')
    score = fields.Integer(string="Score")
    status = fields.Char(string = "Status")
    exam_id = fields.Many2one('exam.scores', string = 'ID')

    @api.onchange('score')
    def _onchange_score(self):
        if self.score <= 39:
            self.status = "Fail"
        elif self.score <= 79 :
            self.status = "Pass"
        elif self.score <= 80:
            self.status = "Destiction"
        elif self.score <=100:
            self.status = "Perfect"
        else:
            self.status = "No exam result"