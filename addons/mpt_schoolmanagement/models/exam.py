from importlib.metadata import files
from odoo import models,fields,api
from odoo.exceptions import ValidationError
class ExamModel(models.Model):
    _name="exam.model"
    _description="Exam"
    
    subject_id=fields.Many2one('subject.model', string="Subject Name", required=True)
    teacher_id=fields.Many2one('school.model', string="Teacher Name", required=True) #link to school panel
    stu_ids= fields.One2many('exam.model.line', 'stu_id',string="Choose Student")#link to subject model
    role=fields.Selection([('student','Student'),('teacher','Teacher')])
    state=fields.Selection([('old','Old'),('current','Current'),('new','New')])
    score=fields.Integer()
    

class SubjectInherit(models.Model):
    _name='exam.model.line'
    stu_id=fields.Many2one('school.model','Student: ')
    subject_name=fields.Char(string="Subject's Name")
    score=fields.Integer(string="Score")
    status=fields.Char(string="Status", readonly=True)

    @api.onchange('score')
    def OnchangeScore(self):
        if self.score >=0 and self.score <= 40:
            self.status = 'Fail'
        elif self.score >= 40 and self.score <= 80:
            self.status = 'Pass'
        elif self.score >= 80 and self.score <= 100:
            self.status = 'Pass with Destination'
        else:
            self.status = 'Wrong Cridential'