import string
from odoo import fields,models,api

class Exam(models.Model):
    _name = "exam.model"
    _description = "Exam"
    _rec_name = "subject_id"
    
    teacher_id = fields.Many2one('school.pj',string="Teacher Name:")
    subject_id = fields.Many2one('subject.model', string="Subject Name:")
    school_exam_line =fields.One2many('school.exam.line', 'exam_id', string='School Exam Line')

class SchoolExam(models.Model):
    _name='school.exam.line'
    _description = 'School_Exam_Line'

    student_id = fields.Many2one('school.pj',string="Student Name:")
    score = fields.Integer(string="Score:")
    status = fields.Char("Status:")
    exam_id = fields.Many2one('exam.model',string="Exam ID")
    
    @api.onchange('score')
    def _onchange_score(self):
        if self.score>=0 and self.score<40:
            self.status='Fail'
        elif self.score>=40 and self.score<80:
            self.status='Pass'
        elif self.score>=80 and self.score<100:
            self.status='Pass with Distinction'
        else:
            self.status='wrong cridentail'




