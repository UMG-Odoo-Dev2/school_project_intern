
from odoo import models,fields
class School(models.Model):
     _inherit='school.model'
     
     _description='hello school'
     nrc=fields.Char("NRC No")