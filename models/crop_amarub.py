from odoo import models, fields, api, _


class CropAmarub(models.Model):
    _name = 'crop.amarub'
    _description = 'Crop Management Module'

    contact_type = fields.Char(string='Contact Type')
    crop_category_and_type = fields.Char(string='Crop Category and Crop Type')
    crop_block_location = fields.Char(string='Crop Category Type Block Location')
    crop_row_location = fields.Char(string='Crop Category Type Row Location')
    crop_collection_method = fields.Char(string='Crop Collection Method')
    water_type = fields.Char(string='Water Type')
    irrigation_type_usage = fields.Char(string='Irrigation Type and Irrigation Usage')

    def action_create_crop_record(self):
        # Action to open a form view to add a new crop record
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Crop Amarub Record'),
            'view_mode': 'form',
            'res_model': 'crop.amarub',
            'target': 'new',
        }

    @api.model
    def create_crop_record(self, values):
        # Custom method to create a new crop management record
        return self.create(values)

    def get_crop_details(self, crop_id):
        # Custom method to get details of a specific crop by ID
        return self.browse(crop_id) if self.exists() else False

    def update_crop_record(self, crop_id, values):
        # Custom method to update an existing crop record
        crop = self.browse(crop_id)
        if crop:
            crop.write(values)
        return crop

    @api.model
    def default_get(self, fields):
        res = super(CropAmarub, self).default_get(fields)
        return res

    def button_create_crop_amarub(self):
        # Button to trigger crop record creation form
        return self.action_create_crop_record()
