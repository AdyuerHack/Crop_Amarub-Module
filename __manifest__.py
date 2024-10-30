{
    'name': 'Crop Amarub',
    'version': '1.0',
    'category': 'Agriculture',
    'summary': 'Crop Management Module for Amarub',
    'author': 'Adyuer Ojeda',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/crop_amarub_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
