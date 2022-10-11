from odoo import api,models,fields
class School(models.TransientModel):
     _name='cancel.model'
     _inherit=['mail.thread','mail.activity.mixin']
     _description='Cancel Student And Teacher'

     name = fields.Many2one('school.model', string="Name")