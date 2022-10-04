import string
from odoo import models,fields,api

class SchoolProject(models.Model):
    _name="leoschool.project.model"
    _description="Welcome to Leo's School"

    name = fields.Char(string="Full Name", required=True)
    photo = fields.Binary(string="Profile Picture")
    roll_no = fields.Char()
    role = fields.Selection([('student','Student'),('teacher','Teacher')], string="Role", required=True)
    state = fields.Selection([
        ('old','Old'),
        ('new','New'),
        ('current','Current'),
    ], string="State", copy=False, tracking=True, default="current")
    father_name = fields.Char(string="Father Name")
    dob = fields.Date(string="Date of Birth")
    address = fields.Text(string="Address")
    phone_no = fields.Char(string="Phone Number")


#     status = fields.Selection(selection=[
#        ('old', 'Old'),
#        ('new', 'New'),
#        ('current', 'Current'),
#     ], string='Status', required=True, read=True, write=True, copy=False,
#    tracking=True)