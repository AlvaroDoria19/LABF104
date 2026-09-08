# 🔵 RT-C2503-01 — Cisco 2503 (serie 2500)

> Router de acceso fijo con 2 puertos serie e ISDN BRI. Ejecuta IOS **Enterprise** multiprotocolo, pero con sólo 4 MB de DRAM.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `RT-C2503-01` |
| **Modelo** | Cisco 2503 (serie 2500) |
| **Nº de serie** | 07896628 |
| **Hostname recomendado** | `F104-RT-2503-01` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Routers Cisco»** (`RT-C2503-01/02` · `RT-C2620-01/02`).

| Dato | Valor |
|---|---|
| Usuario (si hay `login local`) | `<rellenar>` |
| Contraseña de consola (`line console 0`) | `<rellenar>` |
| Contraseña de `enable secret` | `<rellenar>` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **Cisco IOS 11.2(17)**, RELEASE SOFTWARE (fc1) |
| Feature set | **Enterprise** (`C2500-J-L`) — multiprotocolo |
| Imagen en flash | `c2500-j-l_112-17.bin` (7 992 252 bytes) |
| ROM / Bootstrap | System Bootstrap 11.0(10c) |
| BOOTFLASH (RXBOOT) | `IGS-BOOT-R` 11.0(10c) ✅ — permite rescate por TFTP |
| Config register | `0x2102` ✅ (arranque normal) |
| Compilada | 04-Ene-1999 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| CPU | Motorola 68030, revisión N |
| DRAM |  **4 MB** (2 048 K principal + 2 048 K de paquetes) |
| Flash | **8 MB**, marcada `Read ONLY` · **sólo 396 KB libres** |
| NVRAM | 32 KB |
| Processor board ID | 07896628 (hw rev 00000001) |
| LAN | 1 × Ethernet 10 Mbps **AUI DB-15** |
| WAN | 2 × Serial **DB-60** (`Serial0`, `Serial1`) |
| RDSI | 1 × ISDN BRI (`BRI0`) |
| Consola / AUX | RJ-45 · `9600 8N1` |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2500-j-l_112-17.bin` (7 992 252 bytes)

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | [IMAGEN CISCO RTC2503-1](https://drive.google.com/drive/folders/1eTSwyY2_riDC88RjWgUmnFxhjjJlx2BP?usp=sharing) | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `PC-1 · Ruta: `D:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

---

## 📂 Documentación de este equipo

| Documento | Contenido |
|---|---|
| ⭐ [Características y protocolos](caracteristicas.md) | Qué lo hace destacar, qué protocolos soporta y qué **no**, comandos de verificación |
| ⚡ [Chuleta de comandos](chuleta-comandos.md) | Diagnóstico y configuración de este equipo, listos para copiar |
| 🚨 [Plan de contingencia](plan-contingencia.md) | Recuperar contraseña, recuperar el OS y respaldar la configuración |
---


[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
