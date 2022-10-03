from odoo import fields,models

class Student(models.Model):
    _name = "school.pj"
    _description = "School Project"

    roll_no = fields.Char("Roll Number:")
    name = fields.Char("Name:",required=True)
    dob = fields.Date("Date Of Birth:")
    father_name = fields.Char("Father Name:")
    ph_no = fields.Char("Phone Number:")
    email = fields.Char("Email:")
    address = fields.Text("Address")
    role = fields.Selection([('student','Student'),('teacher','Teacher')],'Role')
    state = fields.Selection([('old','Old'),('absent','Absent'),('present','Present')],'State')
    status = fields.Selection(selection=[
       ('old', 'Old'),
       ('absent', 'Absent'),
       ('present', 'Present'),
   ], string='Status', required=True, copy=False,
   tracking=True)    
    
    
    



