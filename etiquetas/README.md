# 🏷️ Etiquetas QR del Laboratorio F104

[⬅️ Volver al inicio](../README.md)

Códigos QR para pegar en el chasis de cada equipo. Al escanearlos se abre la **carpeta del equipo**
en GitHub, con su ficha, características, chuleta de comandos y plan de contingencia.

| Fichero | Qué es |
|---|---|
| **[`etiquetas-QR-F104.pdf`](etiquetas-QR-F104.pdf)** | **Hoja A4 lista para imprimir** — 4 páginas |
| `etiquetas-QR-F104.html` | La misma hoja en HTML, para imprimir desde el navegador si el PDF falla |
| `qr/<ID>.png` | Los 17 QR por separado (1272 × 1272 px), por si necesitas uno suelto |
| `logo/Telecom.png` | Logo de la carrera, ya recortado y optimizado |
| `generar-etiquetas.py` | Script que regenera todo |

---

## 🖨️ Cómo imprimir

> [!IMPORTANT]
> **Imprime al 100 %.** En el diálogo de impresión elige «Tamaño real» / «Escala: 100 %» y
> **desactiva** «Ajustar a la página». Si el PDF se escala, los QR pierden resolución y dejan
> de leerse.

- **Papel:** A4 adhesivo **mate**. Evita el satinado: el brillo produce reflejos que impiden el
  escaneo con el flash del móvil.
- **Impresora:** láser preferiblemente. Con inyección de tinta, deja secar antes de cortar.
- **Corte:** por la línea de puntos.
- Si no tienes papel adhesivo: imprime en papel normal, corta y pega con cinta adhesiva
  transparente por encima (protege el QR del polvo y del roce).

## 📄 Qué hay en cada página

| Página | Formato | Etiqueta | QR | Dónde usarlo |
|:--:|---|---|---|---|
| 1 | **A — Frontal vertical** ⭐ | 34 × 40 mm | 28 mm | **Recomendado.** Cabe en el frontal de **cualquier** equipo. ID debajo del QR |
| 2 | **B — Frontal horizontal** | 60 × 34 mm | 30 mm | Frontales anchos con poca altura libre. ID a la derecha y más grande, con modelo e IP |
| 3 | **C — Grande** | 38 × 46 mm | 32 mm | Tapa superior, carril del rack, cajas de accesorios, USB de rescate. La más fácil de escanear |
| 4 | Verificación | — | — | Tabla ID → URL para comprobar cada QR antes de pegarlo |

### Por qué el formato A es el recomendado

**Todos los equipos del laboratorio son de 1U**, incluidos los routers y firewalls de sobremesa:

| Equipo | Altura del chasis |
|---|---|
| Switches en rack (4500G, 4210, 2924-XL, 2950, PC7024, EX2300) | 44,5 mm (1U) |
| Cisco 2503 y 2620 | ≈ 43 mm |
| Juniper SRX300 | ≈ 44 mm |

Es decir, **no hay ningún frontal donde quepa una etiqueta de 46 mm**. El formato A (40 mm de alto)
deja unos 2 mm de margen arriba y abajo, y mantiene el ID debajo del QR. El formato C se queda para
superficies sin esa restricción.

## 📌 Dónde pegar cada etiqueta

| Equipo | Sitio recomendado |
|---|---|
| Switches de 24 puertos (todos) | Franja izquierda del frontal, **antes del puerto 1**, sin tapar los LED de estado |
| Cisco 2503 / 2620 | Zona lisa del frontal, a la derecha de los LED |
| Juniper SRX300 | Frontal, junto a los puertos SFP |

**Antes de pegar:**

1. Limpia la superficie con alcohol isopropílico y deja secar (el polvo del rack impide que agarre).
2. **No tapes** LED de estado, puertos, tornillos de rack ni **rejillas de ventilación**.
3. Pega el QR **a la misma altura en todos los equipos**: escanear una fila entera del rack es
   mucho más rápido si están alineados.
4. Escanea la etiqueta **ya pegada** antes de pasar al siguiente equipo.

## 🔍 Detalles técnicos

| Parámetro | Valor |
|---|---|
| Contenido | `https://github.com/AlvaroDoria19/LABF104/tree/main/equipos/<ID>` (72 caracteres) |
| Versión QR | 8 — **49 × 49 módulos** |
| Corrección de errores | **H (30 %)**, la más alta del estándar |
| Logo central | 13 × 13 módulos → **7 % del área** (el límite seguro con H está en torno al 25 %) |
| Tamaño de módulo | 0,53 mm (formato A) · 0,57 mm (B) · 0,60 mm (C) |
| Resolución del PNG | 1272 × 1272 px → más de 1000 ppp a 32 mm |

**Los 17 QR se han verificado por decodificación automática** (OpenCV) tras incrustar el logo,
simulando la impresión a 600, 300 y 203 ppp, y a tamaños desde 32 mm hasta 25 mm: **17/17 correctos
en todos los casos**. El margen es amplio.

## ♻️ Regenerar las etiquetas

Necesario si cambian los IDs, las IPs o la URL del repositorio. Edita la lista `EQUIPOS` o
`BASE_URL` en el script y ejecuta:

```bash
python3 -m venv --system-site-packages .venv && .venv/bin/pip install qrcode
```

```bash
.venv/bin/python generar-etiquetas.py
```

Dependencias: `qrcode`, `Pillow` y `weasyprint`. En Debian/Ubuntu, Pillow y WeasyPrint vienen en
`python3-pil` y `weasyprint`; sólo `qrcode` hace falta instalarlo con `pip`.

## 🩹 Si un QR no se lee

| Síntoma | Causa | Solución |
|---|---|---|
| No detecta nada | Se imprimió escalado | Reimprime al **100 %**, sin «ajustar a la página» |
| Reflejos al enfocar | Papel satinado o cinta brillante | Papel mate; si ya está pegado, ilumina en ángulo |
| Detecta pero abre error 404 | La URL del repositorio cambió | Actualiza `BASE_URL` y regenera |
| Sólo falla de cerca | El móvil no enfoca a menos de 10 cm | Escanea a 15–20 cm |
| Borroso o con bandas | Tóner bajo o cabezal sucio | Cambia el tóner y reimprime |

---

[⬅️ Volver al inicio](../README.md) · [📇 Equipos](../equipos/README.md)
