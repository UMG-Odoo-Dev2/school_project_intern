from odoo import models,fields,api

class ExamReport(models.TransientModel):
    _name = 'exam.report.wizard'
    _description = 'Exam Report'

    student_id = fields.Many2one('school.project',string="Student")

    def do_print(self):
        pass
        # domain=[]
        # student_id = self.student_id
        # if student_id:
        #     domain +=[('student_id','=',student_id.id)]
        # subjects = self.env['school.exam'].search(domain)
        # record_list=[]
        # for subject in subjects:
        #     vals = {
        #         'subject_id':subject.subject_id,
        #         'score':subject.score
        #     }
        #     record_list.append(vals)
        # data = {
        #     'from_data':self.read()[0],
        #     'subjects':record_list
        # }
        # return self.env.ref('student_wwk.action_report_result').report_action(data=data)