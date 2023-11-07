{
    'name': "Account Payment Flow",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author': "Tonny Velazquez Juarez",
    'website': "corner.store59@gmail.com",
    'category': 'account',
    'version': '15.0.0.0.1',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_payment_flow_view.xml',
        'views/account_payment_regiter_views.xml'
    ],
}
