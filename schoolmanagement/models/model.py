from odoo import models,fields
class School(models.Model):
     _name='school.model'
     _description='hello school'
     name=fields.Char("Name")
     role = fields.Selection([
          ('student','Student'),
          ('teacher','Teacher')
     ], string='Role')
     status = fields.Selection([
          ('old','Old'),
          ('new','New'),
          ('current','Current')
     ], string='Status')
     country = fields.Selection([
          ('myanmar','Myanmar'),
          ('thailand','Thailand'),
          ('America','American'),
          ('austrail','Austrail')
     ], string='Country')
     
     father_name=fields.Char("Father Name")
     mother_name=fields.Char("Mother Name")
     date_of_birth=fields.Date()
     ph_no=fields.Integer()
     active=fields.Boolean(string="Active",default=True)
    
     state = fields.Selection(selection=[
          ('draft', 'Draft'),
          ('in_progress', 'In Progress'),
          ('done', 'Done'),
          ('cancel', 'Cancelled'),
          
     ], string="Status")
     
     date_of_birth=fields.Date()
     avator=fields.Binary()
     description=fields.Text()
