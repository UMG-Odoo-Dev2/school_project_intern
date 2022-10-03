from odoo import models,fields

class SchoolInfo(models.Model):
    _name = "teachers.students"
    _description = "Testing for my Odoo project"

    name = fields.Char()
    avator = fields.Binary()
    father_name = fields.Char()
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    degree = fields.Char()
    email = fields.Char()
    address = fields.Text()
    role = fields.Selection([('teacher', 'Teacher'), ('student', 'Student')], 'Role')
    state = fields.Selection(selection=[
       ('teacher', 'Teacher'),
       ('student', 'Student'),
   ], string='Status')