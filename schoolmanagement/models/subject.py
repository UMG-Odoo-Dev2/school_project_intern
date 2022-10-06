from odoo import models,fields
class SchoolAppointment(models.Model):
    _name='subject.model'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='school subject'
    _rec_name='subject'
    subject=fields.Char("Subject")
    teacher = fields.Char("Teacher")
    active=fields.Boolean(string="Active",default=True)
    
    # student_id = fields.Many2one(comodel_name='school.model', string='Student')
#  field_name_id = fields.Many2one('comodel_name', string='field_name') 