# 🟠 RT-MR3420-02 — TP-Link TL-MR3420 (OpenWRT / LEDE)

> Router inalámbrico con OpenWRT/LEDE. Los únicos equipos con WiFi del laboratorio y el único router Linux: enseña por dentro lo que los Cisco y Juniper hacen por CLI propietaria.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `RT-MR3420-02` |
| **Modelo** | TP-Link TL-MR3420 (OpenWRT / LEDE) |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname actual** | `⚠️ Por confirmar` |
| **Hostname recomendado** | `F104-RT-MR3420-02` |
| **IP de gestión** | `192.168.1.1/24` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |
| **Dirección IP (LAN)** | `192.168.1.1/24` — ⚠️ es la **dirección por defecto de OpenWRT**, y también la del SRX300 con configuración de fábrica: si ambos se conectan a la misma red hay conflicto de IP |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Routers TP-Link (OpenWRT)»** (`RT-MR3420-02/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario (SSH y LuCI) | `<rellenar>` |
| Contraseña de `root` | `<rellenar>` |
| SSID de la WiFi | `<rellenar>` |
| Contraseña WiFi (WPA2) | `<rellenar>` |

**Sin puerto de consola externo.** El UART está dentro de la carcasa (requiere abrirla y un
adaptador USB-TTL de 3,3 V a `115200 8N1`). El acceso normal es **SSH** y **LuCI** (web);
para recuperar la contraseña se usa el **modo failsafe** por telnet.

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **OpenWRT / LEDE** — rama `lede-17.01`, build `git-19.167.54478-71e2af4` |
| Versión | Corresponde a **LEDE 17.01.7** (junio de 2019) — ⚠️ confirmar con `cat /etc/openwrt_release` |
| Interfaz web | **LuCI** |
| Kernel | ⚠️ Linux 4.4.x (rama 17.01) — confirmar con `uname -a` |
| Gestor de paquetes | `opkg` |
| Configuración | Texto plano en `/etc/config/*`, gestionada con **UCI** |
| Gestor de arranque | **U-Boot** de TP-Link (con recuperación TFTP en algunas revisiones) |
| Soporte | ⚠️ **Fuera de soporte.** LEDE 17.01 terminó en 2019 y OpenWRT dejó de soportar los equipos de 4/32 MB a partir de la 19.07 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Modelo | **TP-Link TL-MR3420** · ⚠️ revisión **v1** (deducida del firmware `TL-MR3420_V1_121123.zip` que hay en el PC del laboratorio) — confirmar con `ubus call system board` |
| SoC | ⚠️ Atheros AR7241 a 400 MHz (revisión v1) |
| RAM | ⚠️ 32 MB |
| Flash | ⚠️ **4 MB** ← la limitación más importante de este equipo |
| LAN | 4 × `10/100` RJ-45 |
| WAN | 1 × `10/100` RJ-45 |
| USB | 1 × USB 2.0 (módem 3G/4G o almacenamiento) |
| WiFi | 802.11 b/g/n en 2,4 GHz · 2×2 MIMO · hasta 300 Mbps · 2 antenas desmontables |
| Botones | Reset / WPS-QSS (se usa para entrar en *failsafe*) |
| Consola | UART interno — hay que abrir la carcasa |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ ⚠️ **La revisión del hardware debe coincidir exactamente** (`-v1-` en el nombre). Confírmala con `ubus call system board`. El PC del laboratorio tiene también el firmware original `TL-MR3420_V1_121123.zip`.

---

## 📂 Documentación de este equipo

| Documento | Contenido |
|---|---|
| ⭐ [Características y protocolos](caracteristicas.md) | Qué lo hace destacar, qué protocolos soporta y qué **no**, comandos de verificación |
| ⚡ [Chuleta de comandos](chuleta-comandos.md) | Diagnóstico y configuración de este equipo, listos para copiar |
| 🚨 [Plan de contingencia](plan-contingencia.md) | Recuperar contraseña, recuperar el OS y respaldar la configuración |

---

## 📝 Notas e historial de este equipo

| Fecha | Tipo | Descripción | Por |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> Tipos: `🔧 CONFIG` · `🔴 FALLO` · `🚨 RESCATE` · `⬆️ UPGRADE` · `🧹 MANT` · `📦 PRÉSTAMO`
> El histórico completo del laboratorio queda repartido entre las notas de cada equipo.

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
