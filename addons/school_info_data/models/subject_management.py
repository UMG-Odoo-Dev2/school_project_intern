from curses import keyname
from dbm import _KeyType
from odoo import models, fields

class Subject(models.Model):
    _name = "subject.management"
    _description = "All subject"

    subjects = fields.Char()
    subject_id = fields.Char(string = 'Sub_id')
    chapter = fields.Integer()
    start_date = fields.Date()
    end_date = fields.Date()
    