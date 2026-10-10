import re
from urllib.parse import quote

from odoo import fields, models, _


class Website(models.Model):
    _inherit = 'website'

    wa_button_enabled = fields.Boolean(string='Enable WhatsApp Button')
    wa_button_number = fields.Char(
        string='WhatsApp Number',
        help="Include the country code, e.g. +1 555 123 4567. Spaces and dashes are fine.",
    )
    wa_button_message = fields.Char(
        string='Default Message',
        default=lambda self: _("Hello! I have a question."),
    )
    wa_button_position = fields.Selection(
        [('right', 'Right'), ('left', 'Left')],
        string='Position', default='right', required=True,
    )

    def _wa_button_url(self):
        self.ensure_one()
        digits = re.sub(r'\D', '', self.wa_button_number or '')
        if not digits:
            return False
        url = 'https://wa.me/%s' % digits
        if self.wa_button_message:
            url += '?text=%s' % quote(self.wa_button_message)
        return url
