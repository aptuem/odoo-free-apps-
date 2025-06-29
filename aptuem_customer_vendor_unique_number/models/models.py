from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')

    _sql_constraints = [
        ('unique_phone', 'UNIQUE(phone)', 'This phone number is already assigned to another customer.'),
        ('unique_mobile', 'UNIQUE(mobile)', 'This mobile number is already assigned to another customer.'),
    ]

    @api.constrains('phone', 'mobile')
    def _check_unique_phone_mobile(self):
        for record in self:
            # Check for duplicate phone in phone or mobile
            if record.phone:
                existing_partner = self.search([
                    ('id', '!=', record.id),
                    '|',
                    ('phone', '=', record.phone),
                    ('mobile', '=', record.phone)
                ], limit=1)
                if existing_partner:
                    raise ValidationError(_(
                        "The phone number '%s' is already assigned to the customer '%s'."
                        % (record.phone, existing_partner.name)
                    ))

            # Check for duplicate mobile in phone or mobile
            if record.mobile:
                existing_partner = self.search([
                    ('id', '!=', record.id),
                    '|',
                    ('phone', '=', record.mobile),
                    ('mobile', '=', record.mobile)
                ], limit=1)
                if existing_partner:
                    raise ValidationError(_(
                        "The mobile number '%s' is already assigned to the customer '%s'."
                        % (record.mobile, existing_partner.name)
                    ))
