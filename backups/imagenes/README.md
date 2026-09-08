# 📀 Imágenes de sistema

Copia de **cada** imagen que corre en los equipos del laboratorio. Casi todos están fuera de soporte
y sus imágenes **ya no son descargables** del fabricante: si se pierden y la flash se corrompe, el
equipo queda inservible.

## Dónde están las imágenes

| Fuente | Ubicación |
|---|---|
| ☁️ **Google Drive del laboratorio** | [`IMAGENES DE SISTEMA`](https://drive.google.com/drive/folders/1Tb2e0GKFHm_TZ4sREUhOTddM-fGJNW57?usp=sharing) |
| 💻 **PC del laboratorio F104** | Equipo: `PC-1` · Ruta: `D:\LabF104\imagenes\` |
| 📀 **USB de rescate (FAT32, 8–16 GB)** | Imprescindible para los Juniper: es su única vía de rescate |
| 🗂️ Este directorio | Solo el inventario y los checksums — los binarios están excluidos por `.gitignore` |

## Inventario de imágenes

| Equipo(s) | Fichero | Versión | Drive | PC lab | USB |
|---|---|---|---|:--:|:--:|
| `SW-3C4500G-01/02` | ⚠️ pendiente (`dir flash:/`) | 3Com OS V5.01.03s56 |  | ☐ | ☐ |
| `SW-3C4210-01/02` | ⚠️ pendiente (`dir flash:/`) | ⚠️ pendiente |  | ☐ | ☐ |
| `SW-C2900XL-01` | `c2900xl-hs-mz-112.8.11-SA6.bin` | IOS 11.2(8.11)SA6 |  | ☐ | ☐ |
| `SW-C2950-01` | `c2950-i6q4l2-mz.121-22.EA13.bin` | IOS 12.1(22)EA13 |  | ☐ | ☐ |
| `RT-C2503-01` | `c2500-j-l_112-17.bin` (7 992 252 bytes) | IOS 11.2(17) Enterprise |  | ☐ | ☐ |
| `RT-C2503-02` | `igs-inr-l.111-17` ⚠️ sin extensión | IOS 11.1(17) `INR` |  | ☐ | ☐ |
| `RT-C2620-01` | `c2600-is-mz.122-27.bin` (10 310 952 bytes) | IOS 12.2(27) IP Plus |  | ☐ | ☐ |
| `RT-C2620-02` | `c2600-is-mz.122-27` ⚠️ confirmar nombre | IOS 12.2(27) IP Plus |  | ☐ | ☐ |
| `SW-PC7024-01…03` | ⚠️ `.stk` pendiente (`show version`) | ⚠️ pendiente |  | ☐ | ☐ |
| `SW-EX2300-01/02` | `junos-arm-32-18.1R3.3.tgz` | Junos 18.1R3.3 |  | ☐ | ☐ |
| `FW-SRX320-01/02` | `junos-srxsme-<version>.tgz` | ⚠️ pendiente | | ☐ | ☐ |
| `RT-MR3420-01/02` | `lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin` | LEDE 17.01.7 | | ☐ | ☐ |
| `RT-MR3420-01/02` (fábrica) | `TL-MR3420_V1_121123.zip` | Firmware original TP-Link | | ☐ | ☐ |

### Prioridad de respaldo

| Prioridad | Equipos | Por qué |
|:--:|---|---|
| 🔴 1 | 3Com 4500G · 3Com 4210 · Cisco 2503 ×2 | EOL sin ninguna distribución posible; el 2503 #1 tiene 396 KB libres en flash |
| 🟠 2 | Catalyst 2924-XL · Catalyst 2950 · Cisco 2620 ×2 | EOL sin distribución, pero con más margen de flash |
| 🟡 3 | Dell PC7024 · EX2300 · SRX320 | Aún obtenibles del soporte de Dell / portal de Juniper |
| 🟢 4 | TL-MR3420 | Descargables del archivo de OpenWRT y del soporte de TP-Link |

---

[⬅️ Volver al inicio](../../README.md) · [🚨 Contingencia general](../../docs/02-plan-contingencia.md)
