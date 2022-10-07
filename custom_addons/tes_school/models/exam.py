import string
from odoo import fields,models,api

class Exam(models.Model):
    _name = "exam.model"
    _description = "Exam"
    
    teacher_id = fields.Many2one('school.pj', string="Teacher")

    # @api.onchange('teacher_id')
    # def _onchange_(self):
    #     for rec in self:
    #         school_pj = rec.env['school.pj'].sudo().search([])
    #         print(school_pj)

    subject_id = fields.Many2one('subject.model', string="Subject:")
    # student_ids=fields.One2many('school.exam.line', 'student_id',string="Student Name:")
    score = fields.Integer("Score Result")
    status = fields.Char("Status")

class SchoolExam(models.Model):
    _name='school.exam.line'

    student_id = fields.Many2one('school.pj')
    subject_name = fields.Char(string="Subject Name")
    score = fields.Integer(string="Score:")
    status = fields.Char("Status:")



