import string
from odoo import fields, models

class Attendance(models.Model):
    _name = 'attendance.students'
    _description = 'Checking Attendance'

    # student_id = fields.Many2one('teachers.students')
    # roll_no = fields.Char('create.session', related='student_id.roll_no')
    attendance_date = fields.Date(string = 'Date')
    attendance = fields.Selection([('present', 'Present', 'absent', 'Absent', 'leave', 'Leave')], string = "Attendance")
    reason = fields.Text()

    