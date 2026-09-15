# 🔵 RT-C2503-02 — Cisco 2503 (serie 2500)

> Router de acceso fijo con 2 puertos serie e ISDN BRI. Tiene **16 MB de DRAM** (4× más que su gemelo) pero ejecuta un IOS más antiguo: 11.1.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `RT-C2503-02` |
| **Modelo** | Cisco 2503 (serie 2500) |
| **Nº de serie** | 06017664 |
| **Hostname actual** | `RT-C2503-02r` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Routers Cisco»** (`RT-C2503-01/02` · `RT-C2620-01/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario (si hay `login local`) | `N/A` |
| Contraseña de consola (`line console 0`) | `N/A` |
| Contraseña de Telnet (`line vty`) | `N/A` |
| Contraseña de `enable secret` | `N/A` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **Cisco IOS 11.1(17)**, RELEASE SOFTWARE (fc1) |
| Feature set | `IGS-INR-L` — IP + IPX + bridging + X.25 + ISDN |
| Imagen en flash | `igs-inr-l.111-17` |
| ROM / Bootstrap | System Bootstrap 11.0(10c) |
| BOOTFLASH (RXBOOT) | `IGS-BOOT-R` 11.0(10c) ✅ — permite rescate por TFTP |
| Config register | `0x2102` ✅ (arranque normal) |
| Compilada | 27-Ene-1998 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| CPU | Motorola 68030, revisión N |
| DRAM | **16 MB** (14 336 K principal + 2 048 K de paquetes) |
| Flash | **8 MB**, marcada `Read ONLY` |
| NVRAM | 32 KB |
| Processor board ID | 06017664 (hw rev 00000001) |
| LAN | 1 × Ethernet 10 Mbps **AUI DB-15** → requiere transceptor AUI→RJ-45 |
| WAN | 2 × Serial **DB-60** (`Serial0`, `Serial1`) |
| RDSI | 1 × ISDN BRI (`BRI0`) — requiere NT1 externo |
| Consola / AUX | RJ-45 · `9600 8N1` |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `igs-inr-l.111-17`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | `[IMAGENES ROUTERS](https://drive.google.com/drive/folders/13WPTIbHg_Qm4KvmR9UxTH6fvjwcnqQHr?usp=sharing)` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `PC-1` · Ruta: `D:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ Fíjate en que **este fichero no lleva extensión `.bin`**. Cópialo con el nombre exacto o el arranque fallará.

---

## 📂 Documentación de este equipo

| Documento | Contenido |
|---|---|
| ⭐ [Características y protocolos](caracteristicas.md) | Qué lo hace destacar, qué protocolos soporta y qué **no**, comandos de verificación |
| ⚡ [Chuleta de comandos](chuleta-comandos.md) | Diagnóstico y configuración de este equipo, listos para copiar |
| 🚨 [Plan de contingencia](plan-contingencia.md) | Recuperar contraseña, recuperar el OS y respaldar la configuración |

---


[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
