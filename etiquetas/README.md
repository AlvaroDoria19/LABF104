# 🏷️ Etiquetas QR del Laboratorio F104

[⬅️ Volver al inicio](../README.md)

Códigos QR con el **emblema de la Universidad Mayor Real y Pontificia de San Francisco Xavier de
Chuquisaca** para pegar en el frontal de cada equipo. Al escanearlos se abre la **carpeta del
equipo** en GitHub, con su ficha, características, chuleta de comandos y plan de contingencia.

| Fichero | Qué es |
|---|---|
| **[`etiquetas-QR-F104.pdf`](etiquetas-QR-F104.pdf)** | **Hoja A4 lista para imprimir** — página 1: las 19 etiquetas · página 2: instrucciones y verificación |
| `etiquetas-QR-F104.html` | La misma hoja en HTML, para imprimir desde el navegador si el PDF falla |
| `qr/<ID>.png` | Los 19 QR por separado (1272 × 1272 px), por si necesitas uno suelto |
| `logo/EMBLEMA-USFX-logo.png` | Emblema de la USFX |
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

Las **19 etiquetas caben en una sola hoja A4**.

## 📐 Formato

Un único formato, **frontal horizontal**:

| Parámetro | Valor |
|---|---|
| Etiqueta | **60 × 34 mm** |
| QR | **30 × 30 mm**, a la izquierda |
| Texto | `LAB F104 · USFX` · **ID del equipo** · modelo, a la derecha |
| Distribución | 3 etiquetas por fila, 7 filas |

**Cabe en el frontal de cualquier equipo del laboratorio.** Todos los chasis son de 1U
(≈ 44,5 mm de alto), incluidos los routers y firewalls de sobremesa, así que una etiqueta de 34 mm
deja unos 5 mm de margen arriba y abajo.

### La IP sólo aparece en dos etiquetas

Las direcciones de gestión cambian entre prácticas, así que **no van impresas**: se consultan en la
ficha del equipo a la que lleva el QR. Las dos excepciones son los routers TP-Link, que tienen
dirección fija y quedan fuera de la VLAN de gestión:

| Etiqueta | IP impresa |
|---|---|
| `RT-MR3420-01` | `172.16.10.1/24` |
| `RT-MR3420-02` | `192.168.1.1/24` |

## 📌 Dónde pegar cada etiqueta

| Equipo | Sitio recomendado |
|---|---|
| Switches de 24 puertos (todos) | Franja izquierda del frontal, **antes del puerto 1**, sin tapar los LED de estado |
| Cisco 2503 / 2620 | Zona lisa del frontal, a la derecha de los LED |
| Juniper SRX300 | Frontal, junto a los puertos SFP |
| TP-Link TL-MR3420 | Tapa superior o frontal, **sin tapar las rejillas de ventilación** |

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
| Emblema central | 17 módulos de alto → **12 % del área** (el recuadro blanco se ajusta a la proporción del emblema para tapar el mínimo posible) |
| Tamaño de módulo | 0,57 mm a 30 mm de QR |
| Resolución del PNG | 1272 × 1272 px → más de 1000 ppp al tamaño impreso |

**Los 19 QR se han verificado por decodificación automática** (OpenCV) tras incrustar el emblema,
simulando la impresión a 600, 300 y 203 ppp y a tamaños desde 30 mm hasta **22 mm**: 19/19
correctos en todos los casos. Al tamaño real de 30 mm el margen es muy amplio.

> 💡 El tamaño del emblema está ajustado a 17 módulos precisamente por esto: a 19 módulos (14 % del
> área) empezaba a fallar alguna lectura al reducir a 26 mm, y a 23 módulos (20 %) fallaba
> directamente. Si cambias `LOGO_ALTO_MOD` en el script, vuelve a verificar la decodificación.

## ♻️ Regenerar las etiquetas

Necesario si cambian los IDs, las IPs o la URL del repositorio. Edita la lista `EQUIPOS` o
`BASE_URL` en el script y ejecuta:

```bash
python3 -m venv --system-site-packages .venv && .venv/bin/pip install qrcode
```

```bash
.venv/bin/python generar-etiquetas.py
```

Para que un equipo **no** muestre IP en su etiqueta, deja la cadena vacía en la tercera columna de
`EQUIPOS`. Dependencias: `qrcode`, `Pillow` y `weasyprint`. En Debian/Ubuntu, Pillow y WeasyPrint
vienen en `python3-pil` y `weasyprint`; sólo `qrcode` hace falta instalarlo con `pip`.

## 🩹 Si un QR no se lee

| Síntoma | Causa | Solución |
|---|---|---|
| No detecta nada | Se imprimió escalado | Reimprime al **100 %**, sin «ajustar a la página» |
| Reflejos al enfocar | Papel satinado o cinta brillante | Papel mate; si ya está pegado, ilumina en ángulo |
| Detecta pero abre error 404 | La URL del repositorio cambió, o el repositorio aún no se ha subido | Comprueba que el `push` se hizo; si cambió la URL, actualiza `BASE_URL` y regenera |
| Sólo falla de cerca | El móvil no enfoca a menos de 10 cm | Escanea a 15–20 cm |
| Borroso o con bandas | Tóner bajo o cabezal sucio | Cambia el tóner y reimprime |

---

[⬅️ Volver al inicio](../README.md) · [📇 Equipos](../equipos/README.md)
