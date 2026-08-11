# WhatsApp Chat Button

**A floating "Chat on WhatsApp" button on every page — turned on from Website settings.**

No snippet to drag, no code: enable it once and every page of the website
gets a floating round button that opens a WhatsApp chat with your number,
pre-filled with a message of your choice.

## Getting started

Website > Configuration > Settings (Websites list) > open your website >
**WhatsApp Button** tab: enable it, set your WhatsApp number (with country
code) and, optionally, a pre-filled message. Save.

- **Position**: bottom-right or bottom-left.
- **Multi-website ready**: each website has its own number, message and
  on/off switch.
- Opens `wa.me` in a new tab — no external script, nothing tracks your
  visitors, nothing is loaded unless the button is enabled.

## Technical

One new field group on the `website` model (`wa_button_*`) plus a small
`website.layout` template extension and a stylesheet. No JavaScript, no
new model, no security rules.

---
Author: Meisanqo — meisanqo@outlook.com
