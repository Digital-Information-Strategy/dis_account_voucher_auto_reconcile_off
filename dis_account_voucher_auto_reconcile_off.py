# -*- coding: utf-8 -*-
##############################################################################
#
#	OpenERP, Open Source Management Solution
#	Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
import math
from osv import osv, fields
import openerp.addons.decimal_precision as dp

class account_voucher(osv.osv):
	_inherit = 'account.voucher'
	def onchange_amount(self, cr, uid, ids, amount, rate, partner_id, journal_id, currency_id, ttype, date, payment_rate_currency_id, company_id, context=None):
		res=super(account_voucher, self).onchange_amount(cr, uid, ids, amount, rate, partner_id, journal_id, currency_id, ttype, date, payment_rate_currency_id, company_id, context)
		for l in res['value']['line_cr_ids']:
			l['reconcile']=False
			l['amount']=0
		for l in res['value']['line_dr_ids']:
			l['reconcile']=False
			l['amount']=0
		return res
	def onchange_partner_id(self, cr, uid, ids, partner_id, journal_id, amount, currency_id, ttype, date, context=None):
		res=super(account_voucher, self).onchange_partner_id(cr, uid, ids, partner_id, journal_id, amount, currency_id, ttype, date, context)
		for l in res['value']['line_cr_ids']:
			l['reconcile']=False
			l['amount']=0
		for l in res['value']['line_dr_ids']:
			l['reconcile']=False
			l['amount']=0
		return res
account_voucher()