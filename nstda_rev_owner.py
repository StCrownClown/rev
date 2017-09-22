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

class nstda_rev_owner(models.Model):

    
    _name = 'nstda.rev.owner'
    _rec_name = 'event_name_id'
    event_name_id = fields.Many2one('nstda.rev.event','Event Name')
    res_user_id = fields.Many2one('res.users','Res User ID')
    
    
    #@api.one
    #@api.constrains('event_name')
    #def _check_name(self):
    #    obj = self.search([['event_name','=',self.event_name]])
    #    if len(obj) > 1:
    #        raise ValidationError("ชื่อกิจกรรมซ้ำ")
    
            
    
    
   