#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los códigos QR con el emblema de la USFX y la hoja A4 lista para imprimir.

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
LOGO = os.path.join(AQUI, "logo", "EMBLEMA-USFX-logo.png")
QR_DIR = os.path.join(AQUI, "qr")

BORDE = 2          # módulos de margen blanco (quiet zone)
PX = 24            # píxeles por módulo al renderizar
LOGO_ALTO_MOD = 17 # alto del emblema en módulos (12 % del área; verificado hasta 25 mm)

# ID, modelo corto, IP (cadena vacía = no se imprime en la etiqueta)
EQUIPOS = [
    ("SW-3C4500G-01", "3Com 4500G",       ""),
    ("SW-3C4500G-02", "3Com 4500G",       ""),
    ("SW-3C4210-01",  "3Com 4210",        ""),
    ("SW-3C4210-02",  "3Com 4210",        ""),
    ("SW-C2900XL-01", "Catalyst 2924-XL", ""),
    ("SW-C2950-01",   "Catalyst 2950",    ""),
    ("SW-PC7024-01",  "Dell PC7024",      ""),
    ("SW-PC7024-02",  "Dell PC7024",      ""),
    ("SW-PC7024-03",  "Dell PC7024",      ""),
    ("SW-EX2300-01",  "Juniper EX2300",   ""),
    ("SW-EX2300-02",  "Juniper EX2300",   ""),
    ("RT-C2503-01",   "Cisco 2503",       ""),
    ("RT-C2503-02",   "Cisco 2503",       ""),
    ("RT-C2620-01",   "Cisco 2620",       ""),
    ("RT-C2620-02",   "Cisco 2620",       ""),
    ("RT-MR3420-01",  "TL-MR3420 OpenWRT", "172.16.10.1/24"),
    ("RT-MR3420-02",  "TL-MR3420 OpenWRT", "192.168.1.1/24"),
    ("FW-SRX300-01",  "Juniper SRX300",   ""),
    ("FW-SRX300-02",  "Juniper SRX300",   ""),
]


def preparar_logo():
    """Recorta el borde transparente y devuelve el emblema y su relación de aspecto."""
    im = Image.open(LOGO).convert("RGBA")
    caja = im.split()[3].getbbox()
    if caja:
        im = im.crop(caja)
    return im, im.width / im.height


def hacer_qr(url, logo, ratio):
    """QR con corrección de errores H y el emblema incrustado en el centro.

    El recuadro blanco se ajusta a la proporción del emblema para tapar el mínimo
    número de módulos posible.
    """
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=BORDE)
    q.add_data(url)
    q.make(fit=True)
    n = q.modules_count
    total = (n + 2 * BORDE) * PX
    img = q.make_image(fill_color="black", back_color="white") \
           .convert("RGBA").resize((total, total), Image.NEAREST)

    alto_mod = LOGO_ALTO_MOD
    ancho_mod = max(1, round(alto_mod * ratio))
    ph, pw = (alto_mod + 2) * PX, (ancho_mod + 2) * PX      # +1 módulo de margen por lado
    ImageDraw.Draw(img).rounded_rectangle(
        [(total - pw) // 2, (total - ph) // 2,
         (total - pw) // 2 + pw, (total - ph) // 2 + ph], radius=PX, fill="white")

    lw, lh = ancho_mod * PX, alto_mod * PX
    img.alpha_composite(logo.resize((lw, lh), Image.LANCZOS),
                        ((total - lw) // 2, (total - lh) // 2))
    area = ((ancho_mod + 2) * (alto_mod + 2)) / (n * n)
    return img, q.version, n, area


CSS = """
  @page { size: A4; margin: 9mm; }
  * { box-sizing: border-box; }
  body { font-family: "DejaVu Sans", Arial, sans-serif; margin: 0; color: #000; }
  h1 { font-size: 11pt; margin: 0 0 1mm; }
  .aviso { font-size: 7.4pt; color: #333; margin: 0 0 3mm; line-height: 1.4; }
  .aviso b { color: #000; }
  .pagina { page-break-after: always; }
  .pagina:last-child { page-break-after: auto; }
  .hoja { font-size: 0; line-height: 0; }
  .fila-et { font-size: 0; line-height: 0; white-space: nowrap; }

  /* etiqueta frontal horizontal: 60 x 34 mm, QR 30 mm */
  .et { display: inline-block; vertical-align: top; width: 60mm; height: 34mm;
        margin: 0 2mm 2mm 0; border: 0.2mm dashed #999; border-radius: 1.5mm;
        padding: 2mm 1.5mm; background: #fff; overflow: hidden; line-height: normal; }
  .et .fila { display: table; width: 100%; height: 30mm; }
  .et .cq { display: table-cell; width: 30mm; vertical-align: middle; }
  .et .ct { display: table-cell; vertical-align: middle; padding-left: 1.5mm;
            overflow: hidden; }
  .et img { width: 30mm; height: 30mm; display: block; image-rendering: pixelated; }
  .et .lab { font-size: 5.5pt; letter-spacing: 0.6pt; color: #666; }
  .et .id { font-size: 8.2pt; font-weight: bold; line-height: 1.2;
            letter-spacing: -0.3pt; white-space: nowrap; }
  .et .mod { font-size: 6pt; color: #222; margin-top: 0.6mm; white-space: nowrap; }
  .et .ip { font-size: 6pt; color: #444; font-family: "DejaVu Sans Mono", monospace;
            margin-top: 0.3mm; white-space: nowrap; }

  table { width: 100%; border-collapse: collapse; font-size: 7pt; }
  th, td { border: 0.2mm solid #bbb; padding: 1mm 1.4mm; text-align: left; }
  th { background: #eee; }
  td.m { font-family: "DejaVu Sans Mono", monospace; white-space: nowrap; }
  td.u { font-family: "DejaVu Sans Mono", monospace; font-size: 5.8pt;
         word-break: break-all; }
"""


def construir_html(datos, mod, area):
    tot = mod + 2 * BORDE
    def una(eid, modelo, ip):
        linea_ip = f'<div class="ip">{ip}</div>' if ip else ""
        return f"""
        <div class="et"><div class="fila">
          <div class="cq"><img src="qr/{eid}.png" alt="{eid}"></div>
          <div class="ct">
            <div class="lab">LAB F104 · USFX</div>
            <div class="id">{eid}</div>
            <div class="mod">{modelo}</div>
            {linea_ip}
          </div>
        </div></div>"""

    POR_FILA = 3
    etiquetas = "".join(
        '<div class="fila-et">' +
        "".join(una(eid, modelo, ip) for eid, modelo, ip, _ in datos[i:i + POR_FILA]) +
        "</div>"
        for i in range(0, len(datos), POR_FILA))

    filas = "".join(
        f'<tr><td class="m">{eid}</td><td>{modelo}</td>'
        f'<td class="m">{ip or "—"}</td><td class="u">{url}</td></tr>'
        for eid, modelo, ip, url in datos)

    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<title>Etiquetas QR — Laboratorio F104</title>
<style>{CSS}</style></head><body>

<div class="pagina">
  <h1>Etiquetas QR — Laboratorio F104 · Universidad San Francisco Xavier</h1>
  <p class="aviso">
    <b>IMPRIMIR AL 100 %</b> — «Tamaño real», con «Ajustar a la página» <b>desactivado</b>.
    Papel A4 adhesivo <b>mate</b>. Corta por la línea de puntos.
    <b>Etiqueta</b> 60 × 34 mm · <b>QR</b> 30 mm · instrucciones completas en la página 2.
  </p>
  <div class="hoja">{etiquetas}</div>
</div>

<div class="pagina">
  <h1>Verificación de destinos</h1>
  <p class="aviso">
    <b>Cómo imprimir.</b> Elige «Tamaño real» / «Escala: 100 %» y <b>desactiva</b> «Ajustar a la
    página»: si se escala, los QR pierden resolución y dejan de leerse. Papel A4, preferiblemente
    adhesivo <b>mate</b> — el brillo produce reflejos que impiden el escaneo con el flash del móvil.<br>
    <b>Dimensiones.</b> Etiqueta 60 × 34 mm · QR 30 mm ({mod}×{mod} módulos, {30/tot:.2f} mm por
    módulo, corrección de errores H al 30 %; el emblema de la USFX tapa el {area*100:.0f} % del
    área). Cabe en el frontal de cualquier equipo del laboratorio: todos son de 1U (44,5 mm de alto).<br>
    <b>IP impresa sólo en los dos TP-Link</b>, que son los únicos con dirección fija fuera de la
    VLAN de gestión. En el resto la IP puede cambiar, así que se consulta en la ficha del equipo
    a la que lleva el QR.<br>
    <b>Antes de pegar:</b> escanea cada QR con el móvil y comprueba que abre la carpeta correcta.
  </p>
  <table>
    <thead><tr><th>ID</th><th>Modelo</th><th>IP en la etiqueta</th><th>Destino del QR</th></tr></thead>
    <tbody>{filas}</tbody>
  </table>
</div>

</body></html>"""


def main():
    os.makedirs(QR_DIR, exist_ok=True)
    logo, ratio = preparar_logo()
    datos, ver, mod, area = [], 0, 0, 0.0
    for eid, modelo, ip in EQUIPOS:
        url = f"{BASE_URL}/{eid}"
        img, ver, mod, area = hacer_qr(url, logo, ratio)
        img.convert("RGB").save(os.path.join(QR_DIR, eid + ".png"), optimize=True)
        datos.append((eid, modelo, ip, url))
        print(f"  {eid:<15} v{ver} {mod}x{mod}  →  qr/{eid}.png")

    html = construir_html(datos, mod, area)
    open(os.path.join(AQUI, "etiquetas-QR-F104.html"), "w").write(html)

    from weasyprint import HTML
    ruta = os.path.join(AQUI, "etiquetas-QR-F104.pdf")
    HTML(string=html, base_url=AQUI).write_pdf(ruta)
    print(f"\nPDF: {ruta}")
    print(f"QR: versión {ver} · {mod}x{mod} módulos · corrección H (30 %) · "
          f"emblema {LOGO_ALTO_MOD} módulos de alto ({area*100:.1f} % del área)")


if __name__ == "__main__":
    main()
