from email.policy import default
import string
from odoo import models,fields

class SchoolInfo(models.Model):
    _name = "teachers.students"
    _description = "Testing for my Odoo project"

    name = fields.Char()
    avator = fields.Binary()
    date_of_birth = fields.Date()
    father_name = fields.Char()
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    degree = fields.Char()
    email = fields.Char()
    address = fields.Text()
    state = fields.Selection(selection=[
          ('teacher', 'Teacher'),
          ('student', 'Student'),
     ], string="Status")
    active = fields.Boolean(string = "Active", default = "True")
    subject_id = fields.Many2one('subject.management', string = "Sub_id")