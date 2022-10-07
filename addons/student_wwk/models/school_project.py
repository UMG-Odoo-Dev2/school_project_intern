from  odoo import models,fields

class SchoolProject(models.Model):
    _name = "school.project"
    _description = "This is school project"

    name = fields.Char('Full Name:')
    roll_num = fields.Char('Roll Number:')
    gender = fields.Selection([('male','Male'),('female','Female')],'Gender:')
    role = fields.Selection([('student','Student'),('teacher','Teacher')],'Role:')
    state = fields.Selection([('presence','Presence'),('absence','Absence'),('former','Former')],'State:')
    dob = fields.Date('Date of Birth:')
    father_name = fields.Char('Father Name:')
    mother_name = fields.Char('Mother Name:')
    kanban_state = fields.Selection([('normal', 'Grey'),('done', 'Green'),('blocked', 'Red')], string='Kanban State', copy=False, default='normal', required=True)
    ph_no = fields.Char('Phone Number:')
    email = fields.Char('Email:')
    avator = fields.Binary()
    status = fields.Selection(selection=[
       ('presence', 'Presence'),
       ('absence', 'Absence'),
       ('former', 'Former'),
   ], string='Status', required=True,readonly=True,  copy=False,
   tracking=True)
   
   

