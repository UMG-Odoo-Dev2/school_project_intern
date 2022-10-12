import string
from odoo import models,fields

class SubjectModel(models.Model):
    _name = "school.subject"
    _description = "Subject"

    name = fields.Char(string="Subject Name")
    student_id = fields.Char()
    teacher_id = fields.Char()
    subject_ids = fields.Char()