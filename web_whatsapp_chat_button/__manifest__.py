{
    'name': 'WhatsApp Chat Button | Floating Contact Button for Website',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'author': 'Meisanqo',
    'support': 'meisanqo@outlook.com',
    'summary': 'A floating WhatsApp chat button on every website page — no code.',
    'description': """
WhatsApp Chat Button
======================

A floating "Chat on WhatsApp" button on every page of your website —
turned on from the website's own settings, no snippet to drag, no code.

Getting started
----------------

Website > Configuration > Settings > "WhatsApp Button": enable it, set
your WhatsApp number (with country code) and, optionally, a pre-filled
message. Save.

- Position: bottom-right or bottom-left.
- Multi-website ready: each website has its own number, message and
  on/off switch.
- Opens `wa.me` in a new tab — no external script, nothing tracks your
  visitors, nothing is loaded unless the button is enabled.
""",
    'depends': ['website'],
    'images': ['static/description/banner.png'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'web_whatsapp_chat_button/static/src/scss/whatsapp_button.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'price': 7.0,
    'currency': 'USD',
}
