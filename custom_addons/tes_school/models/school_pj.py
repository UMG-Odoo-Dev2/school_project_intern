from odoo import fields,models

class School(models.Model):
    _name = "school.pj"
    _description = "School Project"
    
    # active = fields.Boolean(string="Active",default=False)
    # roll_no = fields.Char("Roll Number:")
    avatar = fields.Binary("Profile Photo")
    name = fields.Char("Name:",required=True)
    dob = fields.Date("Date Of Birth:")
    father_name = fields.Char("Father Name:")
    ph_no = fields.Char("Phone Number:")

    # student_ids = fields.Char()
    # subject_id = fields.Many2one('subject.model',string="Subject:")
    # teacher_id = fields.Char()

    email = fields.Char("Email:")
    address = fields.Text("Address:")
    gender = fields.Selection([('male','Male'),('female','Female')])
    role = fields.Selection([('student','Student'),('teacher','Teacher')],'Role:')
    state = fields.Selection(selection=[
       ('old', 'Old'),
       ('new', 'New'),
       ('current', 'Current'),
   ], string='State:', copy=False,default='current',tracking=True)    
    
    
    



