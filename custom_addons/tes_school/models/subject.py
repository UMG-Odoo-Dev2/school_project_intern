
from dataclasses import field
from odoo import fields,models

class Subject(models.Model):
    _name = "subject.model"
    _description = "Subject"
    # _rec_name = 'teacher_id'
    _rec_name = 'subjects'

    subjects = fields.Char("Subject:")
    teacher_id = fields.Many2one("school.pj",string="Teacher Name:")
    # subject_id = fields.Char()
    # name = fields.Char("Subject:")
   
    
    



