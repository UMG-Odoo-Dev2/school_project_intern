
from dataclasses import field
from odoo import fields,models

class Subject(models.Model):
    _name = "subject.model"
    _description = "Subject"
    _rec_name = 'subjects'

    subjects = fields.Char("Subject:")
    subject_id = fields.Char()
    # name = fields.Char("Subject:")
   
    
    



