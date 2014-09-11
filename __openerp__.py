# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
        "name" : "Conciliación Completa automática desactivada",
        "version" : "1.0",
        "author" : "DIS S.A.",
        "website" : "http://dis.co.cr",
        "category" : "Contabilidad",
        "description": """
        * Cambia el resultado del onchange de cliente en pagos de cliente, con el fin de que no aparezca marcada la opción de Conciliación Completa.
        """,
        "depends" : ['base','account_voucher'],
        "init_xml" : [ ],
        "demo_xml" : [ ],
        "data" : [ ],
        "installable": True
}
