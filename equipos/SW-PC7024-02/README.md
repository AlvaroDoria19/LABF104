# 🟡 SW-PC7024-02 — Dell PowerConnect 7024

> Switch Gigabit gestionable de 24 puertos con **Capa 3 completa** (OSPF, VRRP, multicast) y apilamiento. CLI casi idéntica a Cisco IOS.

📱 *Esta página es el destino del código QR pegado en el chasis.*

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## 📇 Identificación

| Dato | Valor |
|---|---|
| **ID de inventario** | `SW-PC7024-02` |
| **Modelo** | Dell PowerConnect 7024 |
| **Nº de serie** | ⚠️ Por confirmar |
| **Hostname actual** | `L3Switch` |
| **Hostname recomendado** | `F104-SW-PC7024-02` |
| **IP de gestión** | `192.168.104.22` |
| **Ubicación (rack / posición)** | `<rellenar>` |
| **Estado** | 🟢 Operativo |

---

## 🔑 Acceso

> Credenciales **compartidas por toda la familia «Switches Dell»** (`SW-PC7024-02…04`).
> Si las cambias, actualiza también los demás ficheros de la familia y el [README](../../README.md).

| Dato | Valor |
|---|---|
| Usuario (`username`) | `<rellenar>` |
| Contraseña del usuario | `<rellenar>` |
| Contraseña de `enable` | `<rellenar>` |

**Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo

---

## 💿 Sistema operativo instalado

| Dato | Valor |
|---|---|
| Firmware | ⚠️ **Por confirmar** — ejecuta `show version` (se espera la serie `5.1.x.x`) |
| Boot code | ⚠️ Por confirmar con `show version` |
| Imagen | ⚠️ Por confirmar — fichero `.stk` (p. ej. `PC7000vX.X.X.X.stk`) |
| Doble imagen | ✅ `image1` / `image2` — permite actualizar sin perder la imagen buena |
| Configuración | `startup-config` en NVRAM |
| Menú de arranque | ✅ Boot Menu por consola (pulsa `2` durante el arranque) |

---

## 🔧 Hardware

| Dato | Valor |
|---|---|
| System Model ID | **PCT7024** |
| Machine Type | **PowerConnect 7024** |
| System Description | Dell Ethernet Switch |
| System Object ID | `1.3.6.1.4.1.674.10895.3034` |
| MAC base | ⚠️ Anotar la de *este* chasis con `show system` (una de las unidades: `F8B1.5610.FBEC`) |
| Nº de serie | ⚠️ Por confirmar con `show version` |
| Puertos de cobre | **24 × 10/100/1000** RJ-45 |
| Puertos combo | 4 × SFP 1000Base-X (combo con 4 de los RJ-45) |
| Bahías de expansión | 2 bahías para módulos 10 Gb — ⚠️ confirmar si están pobladas |
| Gestión dedicada | ✅ Puerto **Out-of-Band (OOB)** independiente + consola RJ-45 + USB |
| Consola | RJ-45 · `9600 8N1` |
| PoE | ❌ No (sería el modelo `7024P`) |

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

> ⚠️ Falta la versión de firmware y el nombre del `.stk`: ejecuta **`show version`**.

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
