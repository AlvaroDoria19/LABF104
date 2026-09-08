# 🟣 SW-EX2300-02 — Juniper EX2300-24T

> Switch Gigabit de acceso con 4 uplinks 10 GbE y Junos. Capa 2 completa + enrutamiento básico, Virtual Chassis y 802.1X.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `SW-EX2300-02` |
| **Modelo** | Juniper EX2300-24T |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname actual** | `SW-LAB2` |
| **Hostname recomendado** | `F104-SW-EX2300-02` |
| **IP de gestión** | `192.168.104.32` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Switches Juniper»** (`SW-EX2300-01/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario `root` — contraseña | `<rellenar>` |
| Usuario de laboratorio (p. ej. `lab-admin`) | `<rellenar>` |
| Contraseña del usuario de laboratorio | `<rellenar>` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **Junos OS 18.1R3.3** |
| Familia | `junos` |
| Modelo reportado | `ex2300-24t` |
| Imagen de recuperación | `junos-arm-32-18.1R3.3.tgz` ⚠️ (confirmar si es la variante `-limited`) |
| Arquitectura de config | *Candidate config* + `commit`, con `rollback` de hasta 49 versiones |
| Gestor de arranque | Loader FreeBSD → modo *single-user* y `recovery`; instalación por USB |
| Soporte | ⚠️ Junos 18.1 está fuera de soporte. Ramas posteriores: `18.2R3-S`, `20.4R3-S`, `21.4R3-S` |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Modelo | **EX2300-24T** (sin PoE) |
| Nº de serie | ⚠️ Por confirmar con `show chassis hardware` |
| Puertos de acceso | **24 × 10/100/1000** RJ-45 |
| Uplinks | **4 × SFP+** (1 GbE / 10 GbE) — también usados como puertos de Virtual Chassis |
| Virtual Chassis | ✅ Hasta 4 miembros |
| Gestión dedicada | ✅ Puerto **MGMT** out-of-band (`me0`) |
| Consola | RJ-45 · `9600 8N1` |
| Almacenamiento | ⚠️ Flash reducida — **crítico** antes de actualizar (ver contingencia) |
| PoE | ❌ No (sería el modelo `EX2300-24P`) |

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `junos-arm-32-18.1R3.3.tgz`

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
