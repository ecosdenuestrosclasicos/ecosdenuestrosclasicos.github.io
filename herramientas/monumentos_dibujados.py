"""Monumentos dibujados a mano (SVG) con el estilo de la ilustración: contorno marrón,
piedra cálida, sombras suaves y una matita de hierba en la base. Se exportan a PNG."""
import subprocess, os
OUT = "/home/claude/pers/cut/"
C = "#5A3A22"   # contorno
PIEDRA, PIEDRA2, SOMBRA = "#EED9AA", "#DDBF86", "#B98F55"
HIERBA, HIERBA2 = "#8E9B4A", "#6F7C35"

def hierba(cx, y, w):
    p = []
    for i in range(-int(w/2), int(w/2), 11):
        p.append(f'<path d="M{cx+i},{y} q1.5,-5 3,-7 q1,4 2,7" fill="{HIERBA}" stroke="{C}" stroke-width="1"/>')
    return f'<ellipse cx="{cx}" cy="{y+2}" rx="{w/2+6}" ry="6" fill="{HIERBA2}" stroke="{C}" stroke-width="1.2"/>' + "".join(p)

DIB = {}
L = 'stroke="#5A3A22" stroke-width=".8" opacity=".55" fill="none"'
DETALLE = {
  # sillares y ventanitas en el faro
  "faro": f'<path {L} d="M38 96h64M38 114h64M38 132h64M70 78v18M54 96v18M86 96v18M62 114v18M78 114v18M50 56h40M56 46v26M84 46v26"/>',
  # piedras en el castillo y sombra bajo las almenas
  "castillo": f'<path {L} d="M24 56h132M40 48v26M56 48v26M72 48v26M108 48v26M124 48v26M140 48v26M70 38h40"/><path d="M24 70h132v4H24z" fill="#5A3A22" opacity=".18"/>',
  # vetas de madera del caballo, crines y clavos
  "caballo": f'<path {L} d="M30 78h84M28 70h88M34 92v16M52 92v16M88 92v16M106 92v16"/><path d="M112 22 l-8 12 M116 26 l-8 12 M120 30 l-8 12" stroke="#5A3A22" stroke-width="1.6"/><g fill="#5A3A22">{"".join(f"<circle cx=\'{x}\' cy=\'66\' r=\'1.2\'/>" for x in range(40,112,12))}</g>',
  # gradas con sombras y escena
  "teatro": f'<path d="M48 92 A37 31 0 0 1 122 92 L114 92 A29 24 0 0 0 56 92Z" fill="#5A3A22" opacity=".12"/><path {L} d="M24 74 L40 66M146 74 L130 66M60 40 L66 52M110 40 L104 52"/><rect x="58" y="94" width="54" height="5" fill="url(#pv)" stroke="#5A3A22" stroke-width="1.2"/>',
  # crestas del volcán y lava
  "vesubio": f'<path {L} d="M60 46 L48 90 M72 54 L70 100 M84 44 L104 92 M66 62 L58 110 M92 58 L116 104"/><path d="M70 54 q-2 10 3 18 q4 -8 1 -18z" fill="#C2582C" opacity=".75"/>',
  # hojas del olivo
  "olivo": f'<g fill="#9DA862" stroke="#5A3A22" stroke-width=".7">{"".join(f"<ellipse cx=\'{x}\' cy=\'{y}\' rx=\'5\' ry=\'2\' transform=\'rotate({r} {x} {y})\'/>" for x,y,r in [(34,64,-30),(48,44,20),(64,30,-15),(82,40,25),(90,58,-20),(72,72,15),(52,78,-25),(40,52,35),(76,56,10),(60,52,-35)])}</g>',
  # muelles del puerto
  "puerto": f'<path {L} d="M30 40 l8 6 M120 40 l-8 6 M24 66 l10 -2 M126 66 l-10 -2 M50 84 l4 -6 M100 84 l-4 -6"/>',
}
# Faro de Alejandría: tres cuerpos (cuadrado, octogonal y cilíndrico) sobre la isla de Faros
DIB["faro"] = (140, 170, f'''
<path d="M10 150 Q70 132 130 150 L130 160 L10 160 Z" fill="{PIEDRA2}" stroke="{C}" stroke-width="2"/>
<rect x="38" y="78" width="64" height="72" fill="{PIEDRA}" stroke="{C}" stroke-width="2.2"/>
<rect x="38" y="78" width="14" height="72" fill="{PIEDRA2}"/>
<path d="M50 92h10v12H50zM80 92h10v12H80zM65 112h10v14H65z" fill="#7A5634" stroke="{C}" stroke-width="1.2"/>
<rect x="34" y="72" width="72" height="8" fill="{PIEDRA2}" stroke="{C}" stroke-width="2"/>
<path d="M48 72 L52 40 H88 L92 72 Z" fill="{PIEDRA}" stroke="{C}" stroke-width="2.2"/>
<path d="M48 72 L52 40 H60 L58 72 Z" fill="{PIEDRA2}"/>
<rect x="46" y="36" width="48" height="6" fill="{PIEDRA2}" stroke="{C}" stroke-width="2"/>
<path d="M58 36 L60 18 H80 L82 36 Z" fill="{PIEDRA}" stroke="{C}" stroke-width="2"/>
<path d="M70 2 C62 10 64 16 70 19 C76 16 78 10 70 2 Z" fill="#E8913A" stroke="#8A3B1E" stroke-width="1.5"/>
<path d="M70 8 C67 12 68 15 70 17 C72 15 73 12 70 8Z" fill="#F7D36B"/>
''')
# Vesubio con la columna de humo y unas columnas de Pompeya
DIB["vesubio"] = (170, 140, f'''
<path d="M64 40 C50 30 66 22 58 12 C70 14 72 4 82 8 C92 0 102 12 96 20 C108 24 100 36 90 38" fill="#CFC5B5" stroke="{C}" stroke-width="1.6" opacity=".95"/>
<path d="M4 128 L60 46 L72 54 L84 44 L150 128 Z" fill="#B49A72" stroke="{C}" stroke-width="2.2"/>
<path d="M60 46 L72 54 L84 44 L100 70 L76 66 L56 78 Z" fill="#8F7556"/>
<path d="M4 128 L60 46 L40 128 Z" fill="#C8B08A" opacity=".7"/>
<path d="M30 110 q20 -8 40 0 M88 104 q16 -6 30 2" stroke="{C}" stroke-width="1" fill="none" opacity=".6"/>
<g fill="{PIEDRA}" stroke="{C}" stroke-width="1.8">
  <rect x="118" y="96" width="44" height="6"/><rect x="122" y="102" width="6" height="26"/><rect x="134" y="102" width="6" height="26"/>
  <rect x="146" y="102" width="6" height="26"/><rect x="156" y="102" width="5" height="26"/>
</g>''' + hierba(85, 128, 150))
# Teatro griego de Siracusa (gradas excavadas en la roca)
DIB["teatro"] = (170, 110, f'''
<path d="M6 92 A79 70 0 0 1 164 92 Z" fill="{PIEDRA2}" stroke="{C}" stroke-width="2.2"/>
<path d="M20 92 A65 57 0 0 1 150 92" fill="none" stroke="{C}" stroke-width="1.4"/>
<path d="M34 92 A51 44 0 0 1 136 92" fill="none" stroke="{C}" stroke-width="1.4"/>
<path d="M48 92 A37 31 0 0 1 122 92" fill="{PIEDRA}" stroke="{C}" stroke-width="1.4"/>
<path d="M85 22 V92 M38 40 L58 70 M132 40 L112 70" stroke="{C}" stroke-width="1.4"/>
<ellipse cx="85" cy="94" rx="30" ry="6" fill="{PIEDRA}" stroke="{C}" stroke-width="1.6"/>
''' + hierba(85, 96, 150))
# Caballo de Troya
DIB["caballo"] = (150, 150, f'''
<rect x="18" y="112" width="112" height="10" rx="2" fill="#8A5A33" stroke="{C}" stroke-width="2"/>
<g fill="#6E4527" stroke="{C}" stroke-width="2"><circle cx="34" cy="128" r="9"/><circle cx="114" cy="128" r="9"/></g>
<g fill="#A8733F" stroke="{C}" stroke-width="2">
  <rect x="34" y="78" width="10" height="34"/><rect x="52" y="78" width="10" height="34"/>
  <rect x="88" y="78" width="10" height="34"/><rect x="106" y="78" width="10" height="34"/>
</g>
<path d="M26 82 Q26 56 48 56 H102 L112 18 L134 24 L132 38 L122 38 L118 64 Q122 82 116 84 Z" fill="#B98049" stroke="{C}" stroke-width="2.4"/>
<path d="M40 62 H100 M40 72 H112" stroke="#7A4E2A" stroke-width="1.4"/>
<path d="M112 18 L106 6 L118 14" fill="#7A4E2A" stroke="{C}" stroke-width="1.6"/>
<circle cx="124" cy="28" r="2.2" fill="{C}"/>
<path d="M26 66 Q10 70 14 92" fill="none" stroke="{C}" stroke-width="3"/>
''' + hierba(74, 136, 120))
# Castillo de Sagunto sobre su cerro
DIB["castillo"] = (180, 110, f'''
<path d="M2 100 C30 66 60 58 92 58 C124 58 150 66 178 100 Z" fill="#C9AF7C" stroke="{C}" stroke-width="2"/>
<path d="M2 100 C30 66 60 58 92 58 L70 100 Z" fill="#B59966" opacity=".6"/>
<path d="M24 74 V48 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 V74 Z" fill="{PIEDRA}" stroke="{C}" stroke-width="2"/>
<path d="M70 48 V26 h8 v6 h8 v-6 h8 v6 h8 v-6 h8 V48" fill="{PIEDRA}" stroke="{C}" stroke-width="2"/>
<path d="M82 74 v-12 a8 8 0 0 1 16 0 v12" fill="#7A5634" stroke="{C}" stroke-width="1.6"/>
<path d="M24 62 H156" stroke="{SOMBRA}" stroke-width="1.2"/>
''' + hierba(90, 98, 160))
# Puerto circular de Cartago (puerto militar con la isla del almirantazgo)
DIB["puerto"] = (150, 110, f'''
<ellipse cx="75" cy="58" rx="68" ry="40" fill="{PIEDRA2}" stroke="{C}" stroke-width="2"/>
<ellipse cx="75" cy="58" rx="52" ry="29" fill="#8FB7D3" stroke="{C}" stroke-width="2"/>
<ellipse cx="75" cy="56" rx="17" ry="10" fill="{PIEDRA}" stroke="{C}" stroke-width="2"/>
<rect x="68" y="40" width="14" height="10" fill="{PIEDRA}" stroke="{C}" stroke-width="1.6"/>
<path d="M66 40 L75 33 L84 40" fill="{PIEDRA2}" stroke="{C}" stroke-width="1.6"/>
<path d="M75 87 V104" stroke="#8FB7D3" stroke-width="8"/><path d="M71 87 V104 M79 87 V104" stroke="{C}" stroke-width="1.6"/>
<g stroke="{C}" stroke-width="1.2">{"".join(f'<line x1="{75+52*__import__("math").cos(a/10)}" y1="{58+29*__import__("math").sin(a/10)}" x2="{75+60*__import__("math").cos(a/10)}" y2="{58+34*__import__("math").sin(a/10)}"/>' for a in range(0,63,4))}</g>
''')
# Olivo de Ítaca
DIB["olivo"] = (120, 130, f'''
<path d="M58 120 C54 100 62 92 52 80 M60 120 C64 102 58 94 70 82" stroke="#6E4A2C" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M58 120 C54 100 62 92 52 80 M60 120 C64 102 58 94 70 82" stroke="{C}" stroke-width="1.4" fill="none"/>
<path d="M60 86 C26 90 14 66 30 56 C22 34 46 22 58 34 C66 16 96 24 92 44 C112 50 104 82 60 86 Z" fill="#8E9A5E" stroke="{C}" stroke-width="2.2"/>
<path d="M38 60 q8 -6 14 0 M66 50 q8 -6 14 0 M54 72 q8 -6 14 0" stroke="#6B7740" stroke-width="2" fill="none"/>
<g fill="#4E3A52">{"".join(f'<circle cx="{x}" cy="{y}" r="2.4"/>' for x,y in [(44,52),(72,40),(84,62),(56,66),(36,70)])}</g>
''' + hierba(60, 120, 70))

DEFS = """<defs>
<linearGradient id="pi" x1="0" x2="1"><stop offset="0" stop-color="#F6E6C0"/><stop offset=".55" stop-color="#E8CF98"/><stop offset="1" stop-color="#C9A465"/></linearGradient>
<linearGradient id="pv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3E1B6"/><stop offset="1" stop-color="#C9A465"/></linearGradient>
<linearGradient id="ma" x1="0" x2="1"><stop offset="0" stop-color="#C98B4E"/><stop offset=".6" stop-color="#A86B36"/><stop offset="1" stop-color="#7E4C25"/></linearGradient>
<linearGradient id="mo" x1="0" x2="1"><stop offset="0" stop-color="#C9B08A"/><stop offset=".5" stop-color="#A88E6A"/><stop offset="1" stop-color="#7C664C"/></linearGradient>
<radialGradient id="ho" cx=".35" cy=".35" r=".8"><stop offset="0" stop-color="#AEB873"/><stop offset=".7" stop-color="#7F8C4A"/><stop offset="1" stop-color="#5E6A33"/></radialGradient>
<radialGradient id="ag" cx=".4" cy=".4" r=".8"><stop offset="0" stop-color="#B9D6EA"/><stop offset="1" stop-color="#6F9EC7"/></radialGradient>
</defs>"""
for nombre, (w, h, cuerpo) in DIB.items():
    cuerpo = (cuerpo.replace(f'fill="{PIEDRA}"', 'fill="url(#pi)"').replace(f'fill="{PIEDRA2}"', 'fill="url(#pv)"')
              .replace('fill="#B98049"', 'fill="url(#ma)"').replace('fill="#A8733F"', 'fill="url(#ma)"')
              .replace('fill="#B49A72"', 'fill="url(#mo)"').replace('fill="#8E9A5E"', 'fill="url(#ho)"')
              .replace('fill="#8FB7D3"', 'fill="url(#ag)"'))
    cuerpo += DETALLE.get(nombre, "")
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*3}" height="{h*3}" viewBox="0 0 {w} {h}">{DEFS}{cuerpo}</svg>'
    open(f"/tmp/{nombre}.svg", "w").write(svg)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={w*3},{h*3}", "--default-background-color=00000000",
                    f"--screenshot={OUT}d_{nombre}.png", f"file:///tmp/{nombre}.svg"], capture_output=True)
    print(nombre, os.path.exists(f"{OUT}d_{nombre}.png"))
