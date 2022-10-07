from  odoo import models,fields

class Exam(models.Model):
    _name = "school.exam"

    teacher_id = fields.Many2one('school.project',string ="Teacher")
    student_ids = fields.One2many('school.exam.line','student_id', string ="Student")
    subject_id = fields.Many2one('school.subject',string ="Subject")
    

class SchooExam(models.Model):
    _name = "school.exam.line"

    student_id = fields.Many2one('school.project')
    # score = fields.Integer(string="Score")
    # status = fields.Char(string="Status")
