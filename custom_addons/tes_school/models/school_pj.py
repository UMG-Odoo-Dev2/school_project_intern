from odoo import fields,models

class School(models.Model):
    _name = "school.pj"
    _description = "School Project"

    # roll_no = fields.Char("Roll Number:")
    avatar = fields.Binary("Profile Photo")
    name = fields.Char("Name:",required=True)
    dob = fields.Date("Date Of Birth:")
    father_name = fields.Char("Father Name:")
    ph_no = fields.Char("Phone Number:")
    email = fields.Char("Email:")
    address = fields.Text("Address:")
    gender = fields.Selection([('male','Male'),('female','Female')])
    role = fields.Selection([('student','Student'),('teacher','Teacher')],'Role:')
    state = fields.Selection([('old','Old'),('new','New'),('current','Current')],'State:')
    status = fields.Selection(selection=[
       ('old', 'Old'),
       ('new', 'New'),
       ('current', 'Current'),
   ], string='Status:',  copy=False,
   tracking=True)    
    
    
    



