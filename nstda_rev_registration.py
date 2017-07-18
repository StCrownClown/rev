# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
import datetime
from datetime import datetime, timedelta
from dateutil import relativedelta as rdelta
from openerp.tools.translate import _
from email import _name
from bsddb.dbtables import _columns
from openerp import tools
import re
from openerp import SUPERUSER_ID
from docutils.parsers import null

class nstda_rev_registration(models.Model):
    

    @api.one
    def _get_register_date(self):
        datetime_object = datetime.strptime(self.register_date, '%Y-%m-%d %H:%M:%S')
        newdate = datetime_object + timedelta(hours = 7)
        self.register_date_cal= newdate
        
    @api.one
    def _get_emp_name(self):
        emp_id = self.env['nstdamas.employee'].search([ ['emp_rusers_id', '=', self.register_code] ] , limit=1)
        self.emp_name= str(emp_id.emp_prf_id.prf_name) + " "+str(emp_id.emp_fname)+" "+str(emp_id.emp_lname)

    @api.one
    def _get_emp_org(self):
        emp_id = self.env['nstdamas.employee'].search([ ['emp_rusers_id', '=', self.register_code] ] , limit=1)
        self.emp_org= emp_id.emp_org_id.org_name
        
    @api.one
    def _get_emp_dvs(self):
        emp_id = self.env['nstdamas.employee'].search([ ['emp_rusers_id', '=', self.register_code] ] , limit=1)
        self.emp_dvs= emp_id.emp_dvs_id.dvs_name
        
    @api.one
    def _get_emp_dpm(self):
        emp_id= self.env['nstdamas.employee'].search([ ['emp_rusers_id', '=', self.register_code] ] , limit=1)
        self.emp_dpm= emp_id.emp_dpm_id.dpm_name

    _name = 'nstda.rev.registration'
    _rec_name = 'register_code'
    emp_id = fields.Many2one('nstdamas.employee','รหัสพนักงาน')
    register_code = fields.Char('รหัสพนักงาน')
    event_name_id = fields.Many2one('nstda.rev.event','Event Name')
    register_fullname = fields.Char('ชื่อ-นามสกุล ')
    register_org = fields.Selection([
                                    ("CO", "CO"),
                                    ("CT", "CT"),
                                    ("TMC", "TMC"),
                                    ("NECTEC", "NECTEC"),
                                    ("NANOTEC", "NANOTEC"),
                                    ("BIOTEC", "BIOTEC"),
                                    ("MTEC", "MTEC"),
                                    ("Serv.", "Serv."),
                                    ("Government", "Government"),
                                    ("University", "University"),
                                    ("Private", "Private"),
                                    ], string="Type")
    register_department = fields.Char('ฝ่าย/บริษัท/มหาลัย')
    register_division = fields.Char('Division')
    register_session = fields.Char('Session')
    register_date = fields.Datetime('วันที่ลงทะเบียน')
    register_date_cal = fields.Char('วันที่ลงทะเบียน_fnc', readonly=True, store=False, compute='_get_register_date')
    emp_name = fields.Char(string="ชื่อ-นามสกุล", compute='_get_emp_name', store=False)
    emp_org = fields.Char(string="ศูนย์", compute='_get_emp_org', store=False)
    emp_dvs = fields.Char(string="ฝ่าย", compute='_get_emp_dvs', store=False)
    emp_dpm = fields.Char(string="งาน", compute='_get_emp_dpm', store=False)
    
    _sql_constraints = [
        ('reg_event_unique', 'unique(register_code, event_name_id)', 'คุณได้ลงทะเบียนเข้าร่วมงานแล้ว'),
    ]