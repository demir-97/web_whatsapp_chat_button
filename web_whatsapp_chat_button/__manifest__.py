{
    'name': 'WhatsApp Chat Button | Floating Contact Button for Website',
    'version': '18.0.1.0.1',
    'category': 'Website',
    'author': 'Meisanqo',
    'support': 'meisanqo@outlook.com',
    'summary': "A floating WhatsApp button on every page of your website: visitors tap the floating chat button and a WhatsApp chat opens on your number with an optional pre-filled message. Set the WhatsApp number, the message and the position (bottom-right or bottom-left) per website from Website > Configuration > Settings: no snippet to drag, no code. Multi-website ready, each site with its own number. Click to chat opens wa.me in a new tab, with no external script, nothing tracking your visitors and nothing loaded at all while the button is off.",
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
    'license': 'LGPL-3',
}
