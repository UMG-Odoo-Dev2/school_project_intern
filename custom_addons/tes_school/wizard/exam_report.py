from odoo import api,fields,models

class ExamReportWizard(models.TransientModel):
    _name = "exam.report.wizard"
    _description = "Exam Result"

    student_id = fields.Many2one('school.pj', string="Student Name")

    # def action_print_report(self):
    #     domain=[]
    #     student_id= self.student_id
    #     if student_id:
    #         domain + = []