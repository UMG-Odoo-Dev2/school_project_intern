import string
from odoo import fields, api, models

class CreateSchoolWizard(models.TransientModel):
    _name = 'create.school.wizard'
    _description = 'Create School Wizard'

    subjects = fields.Many2one('subject.management', string = 'Subject')

    def do_action(self):
        print('Test...........', self.read()[0])