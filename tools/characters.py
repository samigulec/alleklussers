"""
De Stroomploeg — AlleKlussers character cast.
One source of truth: builds the inline <symbol> sprite for index.html
and standalone SVG files in img/characters/.

Run:  python3 tools/characters.py
"""
import pathlib, re

INK = '#16161a'
CHEEK = '#FFB4A2'
METAL = '#D5D9E0'

def face(lx, rx, ey, cy, mouth, r=5.5, cheek_dx=10, delay='0s'):
    """Eyes (blink together), white highlights, cheeks and smile."""
    return f'''<g class="ch-eyes" style="animation-delay:{delay}"><circle cx="{lx}" cy="{ey}" r="{r}" fill="{INK}"/><circle cx="{rx}" cy="{ey}" r="{r}" fill="{INK}"/><circle cx="{lx+2}" cy="{ey-2}" r="1.8" fill="#fff"/><circle cx="{rx+2}" cy="{ey-2}" r="1.8" fill="#fff"/></g>
<ellipse cx="{lx-cheek_dx}" cy="{cy}" rx="6.5" ry="4.2" fill="{CHEEK}"/><ellipse cx="{rx+cheek_dx}" cy="{cy}" rx="6.5" ry="4.2" fill="{CHEEK}"/>
<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'''

CAST = {
    # Stekkie — the plug from the logo, the main character
    'stekkie': f'''<path d="M60 98 C 60 114 86 104 98 116" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<rect x="40" y="10" width="11" height="30" rx="4" fill="{METAL}" stroke="{INK}" stroke-width="4"/>
<rect x="69" y="10" width="11" height="30" rx="4" fill="{METAL}" stroke="{INK}" stroke-width="4"/>
<rect x="20" y="36" width="80" height="64" rx="24" fill="#FFFFFF" stroke="{INK}" stroke-width="4.5"/>
<path d="M56 86 h8" stroke="{INK}" stroke-width="3" opacity=".18" stroke-linecap="round"/>
{face(47, 73, 62, 76, "M53 74 Q 60 82 67 74", delay='0s')}''',

    # Vonk — a little lightning bolt, storingen & spoed
    'vonk': f'''<path d="M66 4 L18 70 H52 L40 116 L102 44 H68 L84 4 Z" fill="#F5A524" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>
<path d="M8 34 l8 5 M108 70 l6 6 M104 18 l-6 7" stroke="#F5A524" stroke-width="4" stroke-linecap="round"/>
{face(50, 70, 52, 62, "M54 60 Q 60 67 66 60", r=5, cheek_dx=9, delay='1.3s')}''',

    # Kastje — the groepenkast
    'kastje': f'''<rect x="20" y="12" width="80" height="98" rx="16" fill="#E9EDF4" stroke="{INK}" stroke-width="4.5"/>
<rect x="30" y="24" width="60" height="26" rx="6" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>
<g fill="#F5A524" stroke="{INK}" stroke-width="2.4"><rect x="35" y="29" width="8" height="16" rx="2"/><rect x="48" y="29" width="8" height="16" rx="2"/><rect x="61" y="29" width="8" height="16" rx="2"/><rect x="74" y="29" width="8" height="16" rx="2" fill="#4CAF7A"/></g>
<rect x="34" y="112" width="12" height="6" rx="3" fill="{INK}"/><rect x="74" y="112" width="12" height="6" rx="3" fill="{INK}"/>
{face(47, 73, 72, 85, "M53 84 Q 60 92 67 84", delay='2.1s')}''',

    # Lampje — the light bulb, verlichting
    'lampje': f'''<path d="M60 4 v6 M22 22 l5 5 M98 22 l-5 5 M10 52 h7 M110 52 h-7" stroke="#F5A524" stroke-width="4" stroke-linecap="round"/>
<circle cx="60" cy="52" r="36" fill="#FFD166" stroke="{INK}" stroke-width="4.5"/>
<path d="M36 40 a26 26 0 0 1 14 -14" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".7"/>
<rect x="43" y="84" width="34" height="24" rx="6" fill="{METAL}" stroke="{INK}" stroke-width="4"/>
<path d="M45 92 h30 M45 100 h30" stroke="{INK}" stroke-width="2.5" opacity=".45"/>
<path d="M52 108 h16 l-3 7 h-10 z" fill="{INK}"/>
{face(48, 72, 50, 63, "M53 61 Q 60 69 67 61", delay='.6s')}''',

    # Dosie — the socket; the two holes are its eyes
    'dosie': f'''<rect x="14" y="14" width="92" height="92" rx="28" fill="#FFFFFF" stroke="{INK}" stroke-width="4.5"/>
<circle cx="60" cy="60" r="31" fill="#F1EFE9" stroke="{INK}" stroke-width="3.5"/>
<rect x="53" y="27" width="14" height="6" rx="3" fill="{METAL}" stroke="{INK}" stroke-width="2"/>
<rect x="53" y="87" width="14" height="6" rx="3" fill="{METAL}" stroke="{INK}" stroke-width="2"/>
{face(48, 72, 56, 70, "M54 69 Q 60 76 66 69", r=6.5, cheek_dx=6, delay='1.8s')}''',

    # Schildje — the shield, keuring & veiligheid
    'schildje': f'''<path d="M60 8 L100 22 V56 C100 84 83 102 60 112 C37 102 20 84 20 56 V22 Z" fill="#A9DDBF" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>
<path d="M60 18 L90 28 V56 C90 77 78 91 60 100" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity=".55"/>
<circle cx="86" cy="94" r="14" fill="#4CAF7A" stroke="{INK}" stroke-width="4"/>
<path d="M79 94 l5 5 l9 -10" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
{face(48, 72, 52, 65, "M53 63 Q 60 71 67 63", delay='2.6s')}''',

    # Laadie — the EV charger, laadpalen & slimme elektra
    'laadie': f'''<path d="M82 70 C 108 70 108 98 96 104" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<rect x="88" y="100" width="16" height="12" rx="4" fill="{METAL}" stroke="{INK}" stroke-width="3.5"/>
<rect x="30" y="8" width="54" height="102" rx="16" fill="#FF8A65" stroke="{INK}" stroke-width="4.5"/>
<rect x="38" y="18" width="38" height="36" rx="9" fill="#FFFFFF" stroke="{INK}" stroke-width="3.5"/>
<path d="M60 64 l-7 12 h9 l-5 12" fill="none" stroke="#FFD166" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="22" y="108" width="70" height="8" rx="4" fill="{INK}"/>
{face(50, 64, 34, 44, "M52 43 Q 57 48 62 43", r=4, cheek_dx=6, delay='.9s')}''',
}

NAMES = {'stekkie': 'Stekkie', 'vonk': 'Vonk', 'kastje': 'Kastje', 'lampje': 'Lampje', 'dosie': 'Dosie', 'schildje': 'Schildje', 'laadie': 'Laadie'}

root = pathlib.Path(__file__).resolve().parent.parent
symbols = []
for key, body in CAST.items():
    body = re.sub(r'\n\s*', '', body)
    symbols.append(f'<symbol id="ch-{key}" viewBox="0 0 120 120">{body}</symbol>')
    (root / 'img/characters' / f'{key}.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-label="{NAMES[key]}">{body}</svg>\n')

sprite = ('<!-- De Stroomploeg: character sprite, generated by tools/characters.py -->\n'
          '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>\n'
          + '\n'.join(symbols) + '\n</defs></svg>\n<!-- /De Stroomploeg -->')

html = (root / 'index.html').read_text()
if '<!-- De Stroomploeg' in html:
    html = re.sub(r'<!-- De Stroomploeg: .*?<!-- /De Stroomploeg -->', lambda m: sprite, html, flags=re.S)
else:
    html = html.replace('<a class="skip"', sprite + '\n\n<a class="skip"', 1)
(root / 'index.html').write_text(html)
print('ok', len(CAST), 'characters')
