from odoo import models,fields

class teachers_students(models.Model):
    _name = 'teachers.students'
    _description = 'Info of studnts and teachers'

    name = fields.Char()
    father_name = fields.Char()
    date_of_birth = fields.Date()
    role = fields.Selection([('teacher', 'Teacher'), ('student', 'Student')], 'Role')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender')
    attendance = fields.Selection([('attend', 'Attend'), ('absence', 'Absence')], 'Attendance')
    degree = fields.Char()
    phone = fields.Char()
    description = fields.Text()
    state = fields.Selection(selection=[
       ('teacher', 'Teacher'),
       ('student', 'Student'),
   ], string='Status', required=True, readonly=True, copy=False,
   tracking=True, default='student')
