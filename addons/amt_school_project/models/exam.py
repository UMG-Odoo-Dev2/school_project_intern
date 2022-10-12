import string
from odoo import fields,models,api

class ExamModel(models.Model):
    _name = "school.exam.model"
    _description = "School Exam"
    _rec_name = "teacher_id"


    child_id = fields.One2many('school.exam.line', 'parent_id', string="Student")
    #std_child_id = fields.Many2one('leoschool.project.model',  string="Student Name")
    teacher_id = fields.Many2one('leoschool.project.model', string="Teacher") # link to school panel
    subject_id = fields.Many2one('school.subject', string="Subject") # link to subject model
    status = fields.Char(string="Exam Result", readonly=True)
    score = fields.Integer(string="Score")
    #student_id = fields.Many2one('leoschool.project.model', string="Student Name")


class SchoolExam(models.Model):
    _name = 'school.exam.line'
    _description = 'School Exam'

    parent_id = fields.Many2one(comodel_name ='school.exam.model')
    student_id = fields.Many2one('leoschool.project.model', string="Student Name")
    score = fields.Integer(string="Score")
    status = fields.Char(string="Result Status", readonly=True)

    @api.onchange('score')
    def OnchangeScore(self):
        if self.score >=0 and self.score <= 39:
            self.status = 'Failed'
        elif self.score >= 40 and self.score <= 79:
            self.status = 'Passed'
        elif self.score >= 80 and self.score <= 100:
            self.status = 'Passed with Destination'
        else:
            self.status = 'Wrong Cridential!!!'

    
        
        
