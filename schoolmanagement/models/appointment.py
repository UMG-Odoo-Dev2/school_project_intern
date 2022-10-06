from odoo import api,models,fields
class SchoolAppointment(models.Model):
    _name='appointment.model'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='school appointment'
    
    name_id=fields.Many2one('school.model', string='Name')
#     role = fields.Selection([
#           ('student','Student'),
#           ('teacher','Teacher')
#     ], string='Student',related='name_id.role')
    

    subject_id = fields.Many2one(comodel_name='subject.model', string='Subject')
    teacher= fields.Char("Teacher")
#     priority widget
    priority=fields.Selection([
      ('0','Normal'),
      ('1','Low'),
      ('2','High'),
      ('3','Very High')],string="Priority")
#     On Change
    score=fields.Integer()
    @api.onchange('subject_id')
    def onchange_subject_id(self):
      self.teacher=self.subject_id.teacher


#     student_id = fields.One2many('school.model',string="Choose Student")
#     role = fields.Selection(
#         [
#             ('student','Student'),
#             ('teacher','Teacher')
#         ]
#     )
#     state = fields.Selection(
#         [
#             ('old','Old'),
#             ('current','Current'),
#             ('new','New')
#         ]
#     )

#     class SubjectInherit(models.Model):
#       _name = 'school.exam.line'


      #student_id = fields.One2many('school.model')
#       name = fields.Char(string="Student Name")
#       score = fields.Integer(string="Score")
    