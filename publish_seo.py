#!/usr/bin/env python3
"""Przygotuj SEO do publikacji: python publish_seo.py https://wybrana-domena.pl
Nie wymaga dodatkowych bibliotek. Uruchom w kopii strony po wyborze domeny.
"""
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import re,sys
if len(sys.argv)!=2:raise SystemExit('Użycie: python publish_seo.py https://twojadomena.pl')
base=sys.argv[1].strip().rstrip('/')
u=urlparse(base)
if u.scheme!='https' or not u.hostname or u.path or u.query or u.fragment or u.username or u.password or 'example' in u.netloc or 'twojadomena' in u.netloc:
 raise SystemExit('Podaj prawdziwą domenę https bez ścieżki, np. https://mojepokoje.pl')
root=Path(__file__).resolve().parent
pages=['index.html','noclegi-klobuck.html','noclegi-czestochowa.html','noclegi-pracownicze-kamyk.html','noclegi-dla-pielgrzymow.html']
for name in pages:
 p=root/name;html=p.read_text(encoding='utf-8')
 url=base+('/' if name=='index.html' else '/'+name)
 html=re.sub(r'<link\b(?=[^>]*\brel=["\']canonical["\'])[^>]*>', '', html,flags=re.I)
 html=re.sub(r'<meta\b(?=[^>]*\bproperty=["\'](?:og:url|og:image|og:image:alt)["\'])[^>]*>', '', html,flags=re.I)
 inject=(f'<link rel="canonical" href="{url}">'
         f'<meta property="og:url" content="{url}">'
         f'<meta property="og:image" content="{base}/assets/img/IMG_3123.webp">'
         '<meta property="og:image:alt" content="Budynek Pokoi Gościnnych w Kamyku">')
 html=html.replace('</head>',inject+'</head>',1)
 html=html.replace('SITE_ORIGIN',base)
 p.write_text(html,encoding='utf-8')
ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns)
rootnode=ET.Element('{%s}urlset'%ns)
for name in pages:
 item=ET.SubElement(rootnode,'{%s}url'%ns);ET.SubElement(item,'{%s}loc'%ns).text=base+('/' if name=='index.html' else '/'+name)
ET.ElementTree(rootnode).write(root/'sitemap.xml',encoding='utf-8',xml_declaration=True)
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n',encoding='utf-8')
print('Gotowe: 5 kanonicznych adresów, metadane udostępniania, JSON-LD, sitemap.xml, robots.txt.')
