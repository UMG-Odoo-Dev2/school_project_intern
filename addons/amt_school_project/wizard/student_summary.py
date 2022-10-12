import string
from tokenize import String
from odoo import models,fields,api

class StudentSummary(models.TransientModel):
    _name = 'student.summary.wizard'
    _description = 'Student Summary Wizard'

    student_id = fields.Many2one('leoschool.project.model', string="Student Name")

