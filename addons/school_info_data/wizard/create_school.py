import string
from odoo import fields, api, models

class CreateSchoolWizard(models.TransientModel):
    _name = 'create.school.wizard'
    _description = 'Create School Wizard'

    subjects = fields.Many2one('subject.management', string = 'Subject')

    def do_action(self):
        data = {
            'form' : self.read()[0],
        }
        return self.env.ref('school_info_data.action_report_create_school').report_action(self, data = data)