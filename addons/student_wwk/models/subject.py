from  odoo import models,fields

class Subject(models.Model):
    _name = "school.subject"
    _rec_name = "subjects"
    
   
    subjects = fields.Char('Subjects')
    teacher_id = fields.Many2one('school.project',string="Teacher")
    # stdent_ids = fields.Char()
    # student_id = fields.Char()
    
   