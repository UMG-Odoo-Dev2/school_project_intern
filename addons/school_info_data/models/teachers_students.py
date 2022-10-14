from datetime import date
from email.policy import default
import string
from odoo import models,fields

class SchoolInfo(models.Model):
    _name = "teachers.students"
    _description = "Testing for my Odoo project"
    _rec_name = 'name'

    name = fields.Char()
    avator = fields.Binary()
    date_of_birth = fields.Date(string = 'Date of Birth')
    # age = fields.Integer(string = 'Age', compute = '_compute_age', tracking = True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    father_name = fields.Char()
    degree = fields.Char()
    email = fields.Char()
    address = fields.Text()
    subject_id = fields.Char()
    state = fields.Selection(selection=[
          ('teacher', 'Teacher'),
          ('teacher_head', 'Teacher HEAD'),
          ('student', 'Student'),
     ], string="Status", required = True, default = 'student')
    active = fields.Boolean(string = "Active", default = "True")
    subjects = fields.Many2one('subject.management', string = "Subjects")
    # def _compute_age(self):
    #     for rec in self:
    #         today = date.today()
    #         if rec.date_of_birth:
    #             rec.age = today.year - rec.date_of_birth.year
    #         else:
    #             rec.age = 0