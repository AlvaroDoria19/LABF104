# 🟢 SW-3C4210-02 — 3Com Switch 4210 26-Port

> Switch Fast Ethernet gestionable de 24 puertos + 2 uplinks, **sólo Capa 2**. Switch de acceso ideal para prácticas de VLAN y 802.1X.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `SW-3C4210-02` |
| **Modelo** | 3Com Switch 4210 26-Port |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname actual** | `⚠️ Por confirmar` |
| **Hostname recomendado** | `F104-SW-4210-02` |
| **IP de gestión** | `192.168.104.14` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Switches 3Com»** (`SW-3C4500G-01/02` · `SW-3C4210-02/02`).
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
| Sistema operativo | ⚠️ **Por confirmar** — `display version` (se espera Comware v3, «3Com OS V3.x») |
| Familia de CLI | Comware v3 — `system-view` / `display` / `save` |
| Imagen en flash | ⚠️ Por confirmar con `dir flash:/` |
| Fichero de configuración | ⚠️ `config.cfg` o `startup.cfg` según versión |
| Bootrom | ⚠️ Por confirmar con `display version` |
| Gestor de arranque | BootROM — menú con `Ctrl+B` al arrancar |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Referencia | ⚠️ Por confirmar (habitual: `3CR17333-91`) |
| Nº de serie | ⚠️ Por confirmar (etiqueta física del chasis) |
| SDRAM / Flash | ⚠️ Por confirmar con `display version` |
| Puertos de acceso | **24 × 10/100** RJ-45 |
| Uplinks | ⚠️ 2 × 10/100/1000 RJ-45 o combo con SFP — confirmar con `display interface brief` |
| Consola | RJ-45 · `9600 8N1` |
| PoE | ❌ No |

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

> ⚠️ **No hay datos capturados de este equipo.** Ejecuta `display version` y `dir flash:/` y rellena esta ficha.

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
