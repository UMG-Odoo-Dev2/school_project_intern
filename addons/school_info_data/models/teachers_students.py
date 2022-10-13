from datetime import date
from email.policy import default
import string
from odoo import models,fields

class SchoolInfo(models.Model):
    _name = "teachers.students"
    _description = "Testing for my Odoo project"

    name = fields.Char()
    avator = fields.Binary()
    date_of_birth = fields.Date(string = 'Date of Birth')
    age = fields.Integer(string = 'Age', compute = '_compute_age', tracking = True)
    father_name = fields.Char()
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    degree = fields.Char()
    email = fields.Char()
    address = fields.Text()
    student_ids = fields.Char()
    score = fields.Integer()
    teacher_id = fields.Char()
    subject_id = fields.Char()
    state = fields.Selection(selection=[
          ('teacher', 'Teacher'),
          ('student', 'Student'),
     ], string="Status", required = True, default = 'student')
    active = fields.Boolean(string = "Active", default = "True")
    subjects = fields.Many2one('subject.management', string = "Subjects")
    attendance = fields.Selection([("attend", "Attendance"), ("absence", "Absence"), ("leave", "Leave")], required = True)
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0