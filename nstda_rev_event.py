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
from openerp.exceptions import ValidationError

class nstda_rev_event(models.Model):

    
    _name = 'nstda.rev.event'
    _rec_name = 'event_name'
    event_name = fields.Char('Event Name')
    event_reg_ids = fields.One2many('nstda.rev.registration','event_name_id','Register Code')
    
    @api.one
    @api.constrains('event_name')
    def _check_name(self):
        obj = self.search([['event_name','=',self.event_name]])
        if len(obj) > 1:
            raise ValidationError("ชื่อกิจกรรมซ้ำ")
            
    
    
   