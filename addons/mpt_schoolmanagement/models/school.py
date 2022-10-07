import email
from email.policy import default
from odoo import models,fields

class SchoolModel(models.Model):
    _name= "school.model"
    _description="School Management"
    name = fields.Char(string='Name', required=True)
    photo = fields.Binary(string='Image', attachment=True)
    father_name=fields.Char()
    mother_name=fields.Char()
    role=fields.Selection([('student','Student'),('teacher','Teacher')])
    # subject_id=fields.Many2one('subject.model', string="Subject:")
    # subject_id = fields.Many2many('subject.model', string="Subject")
    # state=fields.Selection([('old','Old'),('new','New'),('current','Current')])
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    school_dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age')
    school_blood_group = fields.Selection([('A','A+'), ('B','B+'), ('AB', 'AB+'), ('others','Others')], string='Blood Type')
    email=fields.Char()
    ph_no=fields.Char()
    address=fields.Char()
    # active=fields.Boolean(string="Active", default=True)
    subject_id=fields.Char()
    student_id=fields.Char()
    stu_ids=fields.Char()
    teacher_id=fields.Char()
    
    state = fields.Selection(selection=[
       ('old','Old'),
       ('new','New'),('current','Current'),
   ], string='State', required=True, clickable=1, copy=False,
   tracking=True, default='current')

    