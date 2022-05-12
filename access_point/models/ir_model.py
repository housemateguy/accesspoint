# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class IrModel(models.Model):
    """Enable models to be available for API request."""

    _inherit = "ir.model"

    rest_api = fields.Boolean("REST API", default=False, help="Allow this model to be fetched through REST API")