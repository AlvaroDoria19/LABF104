# 🔵 RT-C2620-02 — Cisco 2620 (serie 2600)

> Router modular de acceso con FastEthernet y múltiples puertos serie. El equipo más versátil del laboratorio para prácticas de enrutamiento y WAN.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `RT-C2620-02` |
| **Modelo** | Cisco 2620 (serie 2600) |
| **Nº de serie** | JAD061905Y7 (420459228) |
| **Hostname actual** | `RS` |
| **Hostname recomendado** | `F104-RT-2620-02` |
| **IP de gestión** | `192.168.104.44` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |
| **Interfaces detectadas** | 1 × FastEthernet · 1 × Serial · **6 × serie de baja velocidad** (sync/async) |
| **Flash libre** | ⚠️ Por confirmar con `show flash:` |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Routers Cisco»** (`RT-C2503-01/02` · `RT-C2620-02/02`).
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
| Sistema operativo | **Cisco IOS 12.2(27)**, RELEASE SOFTWARE (fc3) |
| Feature set | **IP Plus** (`C2600-IS-M`) — ⚠️ sin criptografía |
| Imagen en flash | `c2600-is-mz.122-27.bin` |
| ROM / Bootstrap | System Bootstrap 12.2(6r) |
| Config register | `0x2102` ✅ (arranque normal) |
| Compilada | 02-Nov-2004 |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| CPU | Motorola MPC860 |
| DRAM | **64 MB** (61 440 K principal + 4 096 K de paquetes) |
| Flash | **16 MB** (16 384 K), lectura/escritura |
| NVRAM | 32 KB |
| LAN | 1 × FastEthernet 10/100 (`FastEthernet0/0`) |
| Consola / AUX | RJ-45 · `9600 8N1` |
| Slots | 2 × WIC + 1 × Network Module + 1 × AIM |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2600-is-mz.122-27`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ ⚠️ En este router el `show version` reporta la imagen como `flash:c2600-is-mz.122-27` **sin la extensión `.bin`** (a diferencia de su gemelo). Confirma el nombre exacto con `show flash:` y cópialo tal cual, o el arranque fallará.

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
