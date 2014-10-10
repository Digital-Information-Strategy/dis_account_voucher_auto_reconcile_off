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
        * También se quitaron los botones de pagar factura de las vistas de facturas de cliente y proveedor, ya que al desactivar los onchange, estos botones no funcionan correctamente.
        """,
        "depends" : ['base','account','account_voucher'],
        "init_xml" : [ ],
        "update_xml" : ['dis_account_voucher_auto_reconcile_off_view.xml'],
        "demo_xml" : [ ],
        "data" : [ ],
        "installable": True
}
