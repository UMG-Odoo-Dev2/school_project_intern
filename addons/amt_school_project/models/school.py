import string
from odoo import models,fields

class SchoolProject(models.Model):
    _name="leoschool.project.model"
    _description="Welcome to Leo's School"
    _rec_name = 'name'

    name = fields.Char(string="Full Name", required=True)
    photo = fields.Binary(string="Profile Picture")
    roll_no = fields.Char()
    #subject_ids = fields.Many2many('school.subject', string="Subject")
    student_ids = fields.Char(string="Student")
    teacher_id = fields.Char(string="Teacher")
    subject_id = fields.Char(string="Subject")
    #child_id = fields.One2many('leoschool.project.line', 'parent_id', string="Exam Result")
    role = fields.Selection([('student','Student'),('teacher','Teacher')], string="Role", required=True)
    state = fields.Selection([
        ('old','Old'),
        ('new','New'),
        ('current','Current'),
    ], string="State", copy=False, default="current")
    father_name = fields.Char(string="Father Name")
    dob = fields.Date(string="Date of Birth")
    address = fields.Text(string="Address")
    phone_no = fields.Char(string="Phone Number")

# class ExamRetreat(models.Model):
#     _name = 'leoschool.project.line'

#     parent_id = fields.Many2one(comodel_name = 'leoschool.project.model')
#     subject_id = fields.Many2one('school.exam.model')

