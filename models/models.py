from odoo import models, fields, api

class Course(models.Model):
    _name ='openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    #responsible_id = fields.Many2one('res.user', ondelete='set null', string="Responsible",index=True)
    session_ids = fields.One2many('openacademy.session','course_id', string="Sessions")
class Session(models.Model):
    _name = 'openacademy.session'
    _description ="OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_data = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")


    lehrer_id = fields.Many2one('res.partner', string="lehrer")
    course_id =fields.Many2one('openacademy.course',ondelete='cascade',string="Course", required=True)
class Student(models.Model):
    _name = 'openacademy.student'

    name = fields.Char(required=True)
    #das ist ein Kommentar
