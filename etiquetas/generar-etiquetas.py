#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los códigos QR con el logo de la carrera y la hoja A4 lista para imprimir.

Uso:      python3 generar-etiquetas.py
Requiere: qrcode, Pillow, weasyprint
Salida:   qr/<ID>.png · etiquetas-QR-F104.html · etiquetas-QR-F104.pdf
"""
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw

BASE_URL = "https://github.com/AlvaroDoria19/LABF104/tree/main/equipos"
AQUI = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(AQUI, "logo", "Telecom.png")
QR_DIR = os.path.join(AQUI, "qr")

BORDE = 2          # módulos de margen blanco (quiet zone) — el mínimo del estándar es 4,
                   # pero el borde de la etiqueta ya aporta zona blanca adicional
PX = 24            # píxeles por módulo al renderizar
LOGO_MOD = 13      # ancho del logo en módulos
PAD_MOD = 15       # ancho del recuadro blanco bajo el logo

# ID, modelo corto, IP de gestión
EQUIPOS = [
    ("SW-3C4500G-01", "3Com 4500G",       "192.168.104.11"),
    ("SW-3C4500G-02", "3Com 4500G",       "192.168.104.12"),
    ("SW-3C4210-01",  "3Com 4210",        "192.168.104.13"),
    ("SW-3C4210-02",  "3Com 4210",        "192.168.104.14"),
    ("SW-C2900XL-01", "Catalyst 2924-XL", "192.168.104.15"),
    ("SW-C2950-01",   "Catalyst 2950",    "192.168.104.16"),
    ("SW-PC7024-01",  "Dell PC7024",      "192.168.104.21"),
    ("SW-PC7024-02",  "Dell PC7024",      "192.168.104.22"),
    ("SW-PC7024-03",  "Dell PC7024",      "192.168.104.23"),
    ("SW-EX2300-01",  "Juniper EX2300",   "192.168.104.31"),
    ("SW-EX2300-02",  "Juniper EX2300",   "192.168.104.32"),
    ("RT-C2503-01",   "Cisco 2503",       "192.168.104.41"),
    ("RT-C2503-02",   "Cisco 2503",       "192.168.104.42"),
    ("RT-C2620-01",   "Cisco 2620",       "192.168.104.43"),
    ("RT-C2620-02",   "Cisco 2620",       "192.168.104.44"),
    ("FW-SRX300-01",  "Juniper SRX300",   "192.168.104.51"),
    ("FW-SRX300-02",  "Juniper SRX300",   "192.168.104.52"),
]


def preparar_logo():
    """Recorta el borde transparente y devuelve el logo cuadrado."""
    im = Image.open(LOGO).convert("RGBA")
    caja = im.split()[3].getbbox()
    if caja:
        im = im.crop(caja)
    lado = max(im.size)
    lienzo = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    lienzo.paste(im, ((lado - im.width) // 2, (lado - im.height) // 2))
    return lienzo.resize((600, 600), Image.LANCZOS)


def hacer_qr(url, logo):
    """QR con corrección de errores H y el logo incrustado en el centro."""
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=BORDE)
    q.add_data(url)
    q.make(fit=True)
    n = q.modules_count
    total = (n + 2 * BORDE) * PX
    img = q.make_image(fill_color="black", back_color="white") \
           .convert("RGBA").resize((total, total), Image.NEAREST)

    pad_px = PAD_MOD * PX
    x0 = (total - pad_px) // 2
    ImageDraw.Draw(img).rounded_rectangle(
        [x0, x0, x0 + pad_px, x0 + pad_px], radius=PX, fill="white")

    logo_px = LOGO_MOD * PX
    off = (total - logo_px) // 2
    img.alpha_composite(logo.resize((logo_px, logo_px), Image.LANCZOS), (off, off))
    return img, q.version, n


CSS = """
  @page {{ size: A4; margin: 9mm; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: "DejaVu Sans", Arial, sans-serif; margin: 0; color: #000; }}
  h1 {{ font-size: 11pt; margin: 0 0 1mm; }}
  .aviso {{ font-size: 7.4pt; color: #333; margin: 0 0 3mm; line-height: 1.4; }}
  .aviso b {{ color: #000; }}
  .pagina {{ page-break-after: always; }}
  .pagina:last-child {{ page-break-after: auto; }}
  .hoja {{ font-size: 0; }}
  .cel {{ display: inline-block; vertical-align: top; margin: 0 2mm 2mm 0;
          border: 0.2mm dashed #999; border-radius: 1.5mm; background: #fff;
          overflow: hidden; text-align: center; }}
  .cel img {{ display: block; margin: 0 auto; image-rendering: pixelated; }}
  .id {{ font-weight: bold; letter-spacing: -0.15pt; white-space: nowrap; }}
  .sub {{ color: #444; }}

  /* --- A) frontal vertical: 34 x 40 mm, QR 28 mm --- */
  .A {{ width: 34mm; height: 40mm; padding: 1.5mm 0.5mm; }}
  .A img {{ width: 28mm; height: 28mm; }}
  .A .id {{ font-size: 8.2pt; margin-top: 1.2mm; }}
  .A .sub {{ font-size: 5.4pt; margin-top: 0.3mm; }}

  /* --- B) frontal horizontal: 60 x 34 mm, QR 30 mm --- */
  .B {{ width: 60mm; height: 34mm; padding: 2mm 1.5mm; text-align: left; }}
  .B .fila {{ display: table; width: 100%; height: 30mm; }}
  .B .cq {{ display: table-cell; width: 30mm; vertical-align: middle; }}
  .B .ct {{ display: table-cell; vertical-align: middle; padding-left: 2mm;
            overflow: hidden; }}
  .B img {{ width: 30mm; height: 30mm; }}
  .B .lab {{ font-size: 5.5pt; letter-spacing: 0.6pt; color: #666; }}
  .B .id {{ font-size: 8.6pt; line-height: 1.2; letter-spacing: -0.25pt; }}
  .B .mod {{ font-size: 6pt; color: #222; margin-top: 0.6mm; white-space: nowrap; }}
  .B .sub {{ font-size: 6pt; font-family: "DejaVu Sans Mono", monospace; }}

  /* --- C) grande: 38 x 46 mm, QR 32 mm --- */
  .C {{ width: 38mm; height: 46mm; padding: 1.5mm 1mm; }}
  .C img {{ width: 32mm; height: 32mm; }}
  .C .id {{ font-size: 9.2pt; margin-top: 1.2mm; }}
  .C .sub {{ font-size: 6pt; margin-top: 0.4mm; }}

  table {{ width: 100%; border-collapse: collapse; font-size: 7pt; }}
  th, td {{ border: 0.2mm solid #bbb; padding: 1mm 1.4mm; text-align: left; }}
  th {{ background: #eee; }}
  td.m {{ font-family: "DejaVu Sans Mono", monospace; white-space: nowrap; }}
  td.u {{ font-family: "DejaVu Sans Mono", monospace; font-size: 5.8pt;
          word-break: break-all; }}
"""

AVISO_IMPRESION = """<b>IMPRIMIR AL 100 %.</b> En el diálogo de impresión elige «Tamaño real» /
    «Escala: 100 %» y <b>desactiva</b> «Ajustar a la página»: si se escala, los QR pierden
    resolución y dejan de leerse. Papel A4, preferiblemente adhesivo <b>mate</b> (el brillo
    produce reflejos que impiden el escaneo). Corta por la línea de puntos."""


def vertical(datos, clase):
    return "".join(f"""
      <div class="cel {clase}">
        <img src="qr/{eid}.png" alt="{eid}">
        <div class="id">{eid}</div>
        <div class="sub">F104 · {ip}</div>
      </div>""" for eid, modelo, ip, url in datos)


def horizontal(datos):
    return "".join(f"""
      <div class="cel B"><div class="fila">
        <div class="cq"><img src="qr/{eid}.png" alt="{eid}"></div>
        <div class="ct">
          <div class="lab">LAB F104</div>
          <div class="id">{eid}</div>
          <div class="mod">{modelo}</div>
          <div class="sub">{ip}</div>
        </div>
      </div></div>""" for eid, modelo, ip, url in datos)


def construir_html(datos, mod):
    tot = mod + 2 * BORDE
    filas = "".join(
        f'<tr><td class="m">{eid}</td><td>{modelo}</td>'
        f'<td class="m">{ip}</td><td class="u">{url}</td></tr>'
        for eid, modelo, ip, url in datos)

    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<title>Etiquetas QR — Laboratorio F104</title>
<style>{CSS.format()}</style></head><body>

<div class="pagina">
  <h1>Etiquetas QR F104 — A) Frontal vertical <span style="font-weight:normal">(recomendado)</span></h1>
  <p class="aviso">
    {AVISO_IMPRESION}<br>
    <b>Etiqueta:</b> 34 × 40 mm · <b>QR:</b> 28 mm ({mod}×{mod} módulos,
    {28/tot:.2f} mm por módulo, corrección de errores H al 30 %).<br>
    <b>Cabe en el frontal de cualquier equipo del laboratorio</b>: todos son de 1U
    (44,5 mm de alto), así que la etiqueta deja unos 2 mm de margen arriba y abajo.
    El ID va debajo del QR.
  </p>
  <div class="hoja">{vertical(datos, 'A')}</div>
</div>

<div class="pagina">
  <h1>Etiquetas QR F104 — B) Frontal horizontal</h1>
  <p class="aviso">
    {AVISO_IMPRESION}<br>
    <b>Etiqueta:</b> 60 × 34 mm · <b>QR:</b> 30 mm ({mod}×{mod} módulos,
    {30/tot:.2f} mm por módulo, corrección de errores H al 30 %).<br>
    Alternativa para frontales <b>anchos y con poca altura libre</b> (por ejemplo, la franja
    sobre los puertos de los switches). Aquí el ID va a la derecha del QR y con más tamaño,
    además del modelo y la IP. Úsala si prefieres leer el ID a distancia sin escanear.
  </p>
  <div class="hoja">{horizontal(datos)}</div>
</div>

<div class="pagina">
  <h1>Etiquetas QR F104 — C) Grande</h1>
  <p class="aviso">
    {AVISO_IMPRESION}<br>
    <b>Etiqueta:</b> 38 × 46 mm · <b>QR:</b> 32 mm ({mod}×{mod} módulos,
    {32/tot:.2f} mm por módulo, corrección de errores H al 30 %).<br>
    <b>No cabe en un frontal de 1U</b> (mide 46 mm de alto). Úsala en la <b>tapa superior</b>
    del chasis, en el carril del rack, en las cajas de accesorios (transceptores AUI, cables
    DB-60, SFP) o en el USB de rescate. Es la más fácil de escanear.
  </p>
  <div class="hoja">{vertical(datos, 'C')}</div>
</div>

<div class="pagina">
  <h1>Verificación de destinos</h1>
  <p class="aviso">
    Escanea cada QR con el móvil y comprueba que abre la carpeta correcta <b>antes</b> de pegar
    las etiquetas. Todos llevan corrección de errores <b>H (30 %)</b> y el logo central ocupa
    un 7 % del área, muy por debajo del límite: la lectura no se ve afectada.
  </p>
  <table>
    <thead><tr><th>ID</th><th>Modelo</th><th>IP de gestión</th><th>Destino del QR</th></tr></thead>
    <tbody>{filas}</tbody>
  </table>
</div>

</body></html>"""


def main():
    os.makedirs(QR_DIR, exist_ok=True)
    logo = preparar_logo()
    datos, ver, mod = [], 0, 0
    for eid, modelo, ip in EQUIPOS:
        url = f"{BASE_URL}/{eid}"
        img, ver, mod = hacer_qr(url, logo)
        img.convert("RGB").save(os.path.join(QR_DIR, eid + ".png"), optimize=True)
        datos.append((eid, modelo, ip, url))
        print(f"  {eid:<15} v{ver} {mod}x{mod}  →  qr/{eid}.png")

    html = construir_html(datos, mod)
    open(os.path.join(AQUI, "etiquetas-QR-F104.html"), "w").write(html)

    from weasyprint import HTML
    ruta = os.path.join(AQUI, "etiquetas-QR-F104.pdf")
    HTML(string=html, base_url=AQUI).write_pdf(ruta)
    print(f"\nPDF: {ruta}")
    print(f"QR: versión {ver} · {mod}x{mod} módulos · corrección H (30 %) · "
          f"logo {LOGO_MOD} módulos ({(LOGO_MOD/mod)**2*100:.0f} % del área)")


if __name__ == "__main__":
    main()
