# 🟢 SW-3C4500G-02 — 3Com Switch 4500G 24-Port

> Switch Gigabit gestionable de 24 puertos + 4 SFP con **enrutamiento de Capa 3**. El equipo con más capacidad de conmutación del laboratorio junto al PowerConnect.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `SW-3C4500G-02` |
| **Modelo** | 3Com Switch 4500G 24-Port |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname actual** | `4500G` |
| **Hostname recomendado** | `F104-SW-4500G-02` |
| **IP de gestión** | `192.168.104.12` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Switches 3Com»** (`SW-3C4500G-02/02` · `SW-3C4210-01/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario local (`local-user`) | `<rellenar>` |
| Contraseña del usuario | `<rellenar>` |
| Contraseña de `super` (nivel 3) | `<rellenar>` |
| Contraseña del menú BootROM | `<rellenar>` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **3Com OS V5.01.03s56** (Comware v5) |
| Familia de CLI | Comware v5 — `system-view` / `display` / `save` |
| Imagen en flash | ⚠️ Por confirmar con `dir flash:/` |
| Fichero de configuración | `flash:/startup.cfg` |
| Bootrom | Versión **120** |
| CPLD | Versión 006 |
| Gestor de arranque | BootWare / BootROM — menú con `Ctrl+B` al arrancar |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Hardware Version | **REV.B** |
| Nº de serie | ⚠️ Por confirmar con `display device manuinfo` |
| Procesadores | 1 |
| SDRAM | **128 MB** |
| Flash | **16 MB** (16 384 K) |
| Placa de puertos | [SubSlot 0] **24GE + 4SFP** (REV.B) |
| Puertos de cobre | **24 × 10/100/1000** RJ-45 |
| Puertos ópticos | **4 × SFP** 1000Base-X |
| Consola | RJ-45 · `9600 8N1` |
| PoE | ❌ No (sería un modelo `PWR`) |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** ⚠️ **Por confirmar** — ejecuta los comandos de verificación

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ El nombre del fichero `.bin` no consta en la captura de datos. Ejecuta `dir flash:/` y anótalo aquí.

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
> El histórico completo del laboratorio está en la [bitácora](../../docs/04-bitacora.md).

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
