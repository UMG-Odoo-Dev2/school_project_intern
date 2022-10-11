import string
from  odoo import models,fields,api

class Exam(models.Model):
    _name = "school.exam"
    _rec_name = "subject_id"

    exam_line_ids = fields.One2many('school.exam.line','exam_id',string="Exam Data")
    teacher_id = fields.Many2one('school.project',string="Teacher")
    subject_id = fields.Many2one('school.subject',string='Subject')
   

class SchoolExam(models.Model):
    _name = "school.exam.line"

    student_id=fields.Many2one('school.project')
    score = fields.Integer(string="Score")
    status = fields.Char(string="Status")
    exam_id = fields.Many2one('school.exam')

    @api.onchange('score')
    def _onchange_score(self):
        if self.score >=0 and self.score<40:
            self.status="Fail"
        elif self.score>=40 and self.score<80:
            self.status="Pass"
        else:
            self.status="Distinction"



    
