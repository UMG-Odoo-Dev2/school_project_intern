import email
from odoo import models,fields

class SchoolModel(models.Model):
    _name= "school.model"
    _description="School Management"
    name = fields.Char(string='Name', required=True)
    photo = fields.Binary(string='Image', attachment=True)
    father_name=fields.Char()
    mother_name=fields.Char()
    age = fields.Integer(string='Age')
    role=fields.Selection([('student','Student'),('teacher','Teacher')])
    state=fields.Selection([('old','Old'),('new','New'),('current','Current')])
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    school_dob = fields.Date(string="Date of Birth")
    school_blood_group = fields.Selection([('A','A+'), ('B','B+'), ('AB', 'AB+'), ('others','Others')], string='Blood Type')
    email=fields.Char()
    ph_no=fields.Char()
    address=fields.Char()
    
    status = fields.Selection(selection=[
       ('old','Old'),
       ('new','New'),('current','Current'),
   ], string='Status', required=True, readonly=True, copy=False,
   tracking=True, default='old')

    