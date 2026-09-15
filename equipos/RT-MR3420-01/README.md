# 🟠 RT-MR3420-01 — TP-Link TL-MR3420 (OpenWRT / LEDE)

> Router inalámbrico con OpenWRT/LEDE. Los únicos equipos con WiFi del laboratorio y el único router Linux: enseña por dentro lo que los Cisco y Juniper hacen por CLI propietaria.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `RT-MR3420-01` |
| **Modelo** | TP-Link TL-MR3420 (OpenWRT / LEDE) |
| **Hostname recomendado** | `F104-RT-MR3420-01` |
| **IP de gestión** | `172.16.10.1/24` |
| **Estado** | 🟢 Operativo |
| **Dirección IP (LAN)** | `172.16.10.1/24`  |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Routers TP-Link (OpenWRT)»** (`RT-MR3420-01/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

> [!IMPORTANT]  
> Las credenciales y acceso WI-FI son exclusivas de los docentes y auxiliares, la red está oculta, se debe agregar manualmente.
| Dato | Valor |
|---|---|
| Usuario (SSH y LuCI) | `root` |
| Contraseña de `root` | `REDACTED` |
| SSID de la WiFi | `LABF104` |
| Contraseña WiFi (WPA2) | `REDACTED` |

El acceso normal es **SSH** y **LuCI** (web);
para recuperar la contraseña se usa el **modo failsafe** por telnet.

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **OpenWRT / LEDE** — rama `lede-17.01`, build `git-19.167.54478-71e2af4` |
| Versión | Corresponde a **LEDE 17.01.7** (junio de 2019) |
| Interfaz web | **LuCI** |
| Kernel | Linux 4.4.x (rama 17.01)  |
| Gestor de paquetes | `opkg` |
| Configuración | Texto plano en `/etc/config/*`, gestionada con **UCI** |
| Gestor de arranque | **U-Boot** de TP-Link (con recuperación TFTP en algunas revisiones) |
| Soporte |  **Fuera de soporte.** LEDE 17.01 terminó en 2019 y OpenWRT dejó de soportar los equipos de 4/32 MB a partir de la 19.07 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Modelo | **TP-Link TL-MR3420** ·revisión **v1.2** |
| SoC |  Atheros AR7241 a 400 MHz (revisión v1.2) |
| RAM | 32 MB |
| Flash | 4 MB|
| LAN | 4 × `10/100` RJ-45  (EL PUERTO 4 NO FUNCIONA)|
| WAN | 1 × `10/100` RJ-45  (EL PUERTO WAN NO FUNCIONA, REEMPLAZADO POR EL 3)|
| USB | 1 × USB 2.0 (módem 3G/4G o almacenamiento) |
| WiFi | 802.11 b/g/n en 2,4 GHz · 2×2 MIMO · hasta 300 Mbps · 2 antenas desmontables |
| Botones | Reset / WPS-QSS (se usa para entrar en *failsafe*) |
| Consola | UART interno — hay que abrir la carcasa |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** |  | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `PC-1` · Ruta: `D:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️  El PC del laboratorio tiene además el firmware original de TP-Link `TL-MR3420_V1_121123.zip`, por si hiciera falta volver a él.

---

## 📂 Documentación de este equipo

| Documento | Contenido |
|---|---|
| ⭐ [Características y protocolos](caracteristicas.md) | Qué lo hace destacar, qué protocolos soporta y qué **no**, comandos de verificación |
| ⚡ [Chuleta de comandos](chuleta-comandos.md) | Diagnóstico y configuración de este equipo, listos para copiar |
| 🚨 [Plan de contingencia](plan-contingencia.md) | Recuperar contraseña, recuperar el OS y respaldar la configuración |

---
[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
