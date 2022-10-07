from odoo import models,fields

class SubjectModel(models.Model):
    _name="subject.model"
    _description="Subjects"
    _rec_name='subject'
    subject=fields.Char(string="Subject's Name:")
    subject_id=fields.Char()
    student_ids=fields.Char()
    teacher_id=fields.Char()