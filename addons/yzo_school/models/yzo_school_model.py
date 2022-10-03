from odoo import models,fields,api

class YZO_School(models.Model):
    _name="yzo.school.model"
    _description="School Information"

    # avator=fields.Binary()
    # id=fields.Char("ID")
    roll_no=fields.Char("Roll Number:")
    name=fields.Char("Name:",required=True)
    father_name=fields.Char("Father Name:")
    date_of_birth=fields.Date(string="Date Of Birth:")
    phone_no=fields.Char("Phone Number:")
    address=fields.Text(string="Address:")
    role=fields.Selection(
         [('student','Student'),('teacher','Teacher')],'Role:'
    )
    
#     role = fields.Selection(selection=[
#        ('teacher', 'Teacher'),
#        ('student', 'Student'),
#    ], string='Status', required=True, readonly=True, copy=False,
#    tracking=True)

    state=fields.Selection(
        [('old','Old'),('new','New'),('current','Current')]
    )

    status = fields.Selection(selection=[
        ('old', 'Old'),
        ('new', 'New'),
        ('current', 'Current')], string='Status:', required=True, readonly=True, copy=False,tracking=True
    )