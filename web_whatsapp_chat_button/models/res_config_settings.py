from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wa_button_enabled = fields.Boolean(related='website_id.wa_button_enabled', readonly=False)
    wa_button_number = fields.Char(related='website_id.wa_button_number', readonly=False)
    wa_button_message = fields.Char(related='website_id.wa_button_message', readonly=False)
    wa_button_position = fields.Selection(related='website_id.wa_button_position', readonly=False)
