# 🔵 SW-C2900XL-01 — Cisco Catalyst WS-C2924-XL-EN

> Switch de 24 puertos 10/100, sólo Capa 2, con **Enterprise Edition Software**. Equipo histórico ideal para prácticas de VLAN, VTP y STP clásico.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `SW-C2900XL-01` |
| **Modelo** | Cisco Catalyst WS-C2924-XL-EN |
| **Nº de serie** | FOC0509Z04U |
| **Hostname actual** | `SW_servers` |
| **Hostname recomendado** | `F104-SW-2924XL-01` |
| **IP de gestión** | `192.168.104.15` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Switches Cisco»** (`SW-C2900XL-01` · `SW-C2950-01`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario (si hay `login local`) | `<rellenar>` |
| Contraseña de consola (`line console 0`) | `<rellenar>` |
| Contraseña de Telnet (`line vty`) | `<rellenar>` |
| Contraseña de `enable secret` | `<rellenar>` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **Cisco IOS 11.2(8.11)SA6** — MAINTENANCE INTERIM SOFTWARE |
| Feature set | **Enterprise Edition** (`C2900XL-HS-M`) |
| Imagen en flash | `c2900xl-hs-mz-112.8.11-SA6.bin` |
| ROM / Bootstrap | C2900XL boot loader |
| Config register | `0xF` (valor normal en esta plataforma) |
| Compilada | 17-Jul-2003 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Modelo exacto | **WS-C2924-XL-EN** (revisión de modelo N0) |
| Nº de serie del sistema | `FOC0509Z04U` |
| Nº de serie de placa base | `FOC050803X3` |
| MAC base | `00:05:32:29:0F:80` |
| CPU | PowerPC 403GA (revisión 0x11) |
| DRAM | **8 MB** (8 192 K + 1 024 K) |
| Flash | ⚠️ Por confirmar con `dir flash:` (típicamente 4 MB en este modelo) |
| NVRAM | 32 KB simulada en flash |
| Puertos | **24 × 10/100** Ethernet |
| Nº de placa base | 73-3382-08 |
| Fuente de alimentación | P/N 34-0834-01 · S/N PHI0452056Y |
| Consola | RJ-45 · `9600 8N1` |
| Botón MODE | ✅ Sí (frontal) → recuperación de contraseña |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2900xl-hs-mz-112.8.11-SA6.bin`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
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
