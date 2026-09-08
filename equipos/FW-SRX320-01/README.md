# 🟣 FW-SRX320-01 — Juniper SRX320

> Firewall de nueva generación / router de servicios con Junos. Políticas por zonas, NAT, IPsec y alta disponibilidad en clúster de 2 nodos.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `FW-SRX320-01` |
| **Modelo** | Juniper SRX320 |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname recomendado** | `F104-FW-SRX320-01` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Firewalls Juniper»** (`FW-SRX320-01/02`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario `root` — contraseña | `admin1234` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Sistema operativo | **Junos OS** (serie SRX320) — ⚠️ **versión por confirmar** con `show system information` |
| Versión de Junos | ⚠️ **Por confirmar** (ramas habituales en esta plataforma: `15.1X49-Dxxx`, `19.4Rx`, `20.4R3-Sx`, `21.4R3-Sx`) |
| Imagen de recuperación | `junos-srxsme-<version>.tgz` — ⚠️ completar con la versión real |
| RE BIOS  | **3.1** |
| RE BIOS Backup | **3.1** — estado `OK` |
| Modo de funcionamiento | *Flow-based* (con estado) por defecto; también soporta *packet-based* |
| Arquitectura de config | *Candidate config* + `commit`, con `rollback` de hasta 49 versiones |
| Gestor de arranque | Loader FreeBSD → modo *single-user* y `recovery`; instalación por USB |
---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| Modelo | **SRX320** |
| Nº de serie | ⚠️ Por confirmar con `show chassis hardware` |
| Puertos | **6 × `10/100/1000` RJ-45** (`ge-0/0/0`…`ge-0/0/5`) + **2 × SFP** (`ge-0/0/6`, `ge-0/0/7`) |
| Slots de expansión | ✅ **2 × Mini-PIM** |
| Memoria / almacenamiento | 4 GB DRAM · ≈ 8 GB flash |
| Rendimiento | Firewall ≈ 1 Gbps · IPsec VPN ≈ 300 Mbps  | |
| Consola | RJ-45 + micro-USB · `9600 8N1` |
| USB | 2 puertos USB — para el medio de rescate en FAT32 |
| Alta disponibilidad | ✅ **Chassis Cluster** de 2 nodos (con la pareja `FW-SRX320-01/02`) |
| PoE | ❌ No en esta unidad (existe la variante `SRX320-POE`) |
---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** ⚠️ **Por confirmar** — ejecuta los comandos de verificación

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | [IMAGENES JUNIPER](https://drive.google.com/drive/folders/1T2-JxXV9dJ2aA9FMOm0UuZU8caElejkd?usp=sharing)| ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `PC-1` · Ruta: `D:\LabF104\imagenes\` | &#9724; |
| 🗂️ Repositorio Git | `backups/imagenes/` | &#9724; |

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
