{
    'name': "Account Bill Report",

    'summary': """Se agrega reporte de facturas con saldos de debitos por conciliar""",

    'author': "Tonny Velazquez",
    'website': "corner.store59@gmail.com",

    'category': 'account',
    'version': '15.0.0.0.1',
    'depends': ['account', 'l10n_cl_fe'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
        # 'views/templates.xml',
    ],
}
