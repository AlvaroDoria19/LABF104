# 🧪 Laboratorio de Redes **F104** — Documentación Técnica

> Inventario, fichas por equipo, planes de contingencia y BItacoras de comandos del laboratorio F104
> · Ingeniería en Telecomunicaciones.

![Equipos](https://img.shields.io/badge/Equipos-19-blue) ![Fabricantes](https://img.shields.io/badge/Fabricantes-6-orange) ![Carpetas](https://img.shields.io/badge/Carpetas%20por%20chasis-19-green) ![Docs](https://img.shields.io/badge/Formato-Markdown-black)

| Campo | Valor |
|---|---|
| **Laboratorio** | F104 |
| **Auxiliar** | `Alvaro Doria Medina` |
| **Última actualización** | 2026-09-06 |
| **Versión del documento** | 4.1 |

---

## 📑 Índice

| Documento | Contenido |
|---|---|
| 🔑 [Credenciales](#-credenciales-de-acceso) | Usuarios y contraseñas por familia (en esta página) |
| 📦 [Imágenes de sistema](#-imágenes-de-sistema-google-drive-y-pc-del-laboratorio) | Enlace de Google Drive y PC del laboratorio |
| **📇 [Equipos](equipos/README.md)** | **Una carpeta por chasis — destino de los códigos QR** |
| 📊 [Comparativa](docs/01-comparativa.md) | Vista de conjunto, memoria, riesgos y qué usar para qué |
| 🚨 [Contingencia general](docs/02-plan-contingencia.md) | Procedimientos comunes y servidor de rescate |
| ⚡ [Chuleta general](docs/03-chuleta-comandos.md) | «Piedra Rosetta»: el mismo comando en las 4 CLI |
| 📝 [Bitácora](docs/04-bitacora.md) | Incidencias, préstamos y mantenimiento |
| 🏷️ [Etiquetas QR](etiquetas/README.md) | Hoja A4 lista para imprimir con los 19 códigos QR |

---

## 📇 Equipos

**Cada chasis tiene su propia carpeta** con cuatro documentos: ficha, características, chuleta de
comandos y plan de contingencia. El **código QR** de cada equipo apunta a su carpeta.

| 🟢 3Com | 🔵 Cisco | 🟡 Dell | 🟣 Juniper | 🟠 TP-Link |
|---|---|---|---|---|
| [`SW-3C4500G-01`](equipos/SW-3C4500G-01/) | [`SW-C2900XL-01`](equipos/SW-C2900XL-01/) | [`SW-PC7024-01`](equipos/SW-PC7024-01/) | [`SW-EX2300-01`](equipos/SW-EX2300-01/) | [`RT-MR3420-01`](equipos/RT-MR3420-01/) |
| [`SW-3C4500G-02`](equipos/SW-3C4500G-02/) | [`SW-C2950-01`](equipos/SW-C2950-01/) | [`SW-PC7024-02`](equipos/SW-PC7024-02/) | [`SW-EX2300-02`](equipos/SW-EX2300-02/) | [`RT-MR3420-02`](equipos/RT-MR3420-02/) |
| [`SW-3C4210-01`](equipos/SW-3C4210-01/) | [`RT-C2503-01`](equipos/RT-C2503-01/) | [`SW-PC7024-03`](equipos/SW-PC7024-03/) | [`FW-SRX300-01`](equipos/FW-SRX300-01/) | |
| [`SW-3C4210-02`](equipos/SW-3C4210-02/) | [`RT-C2503-02`](equipos/RT-C2503-02/) | | [`FW-SRX300-02`](equipos/FW-SRX300-02/) | |
| | [`RT-C2620-01`](equipos/RT-C2620-01/) | | | |
| | [`RT-C2620-02`](equipos/RT-C2620-02/) | | | |

➡️ [Índice completo con modelo, SO e IP de cada equipo](equipos/README.md)

**Qué hay dentro de cada carpeta**

| Fichero | Contenido |
|---|---|
| `README.md` | Ficha: identificación, credenciales, SO instalado, hardware y **dónde conseguir la imagen** |
| `caracteristicas.md` | Características destacadas, protocolos soportados y **no** soportados, limitaciones |
| `chuleta-comandos.md` | Comandos de diagnóstico y configuración de ese equipo |
| `plan-contingencia.md` | Recuperar contraseña, recuperar el OS, respaldo y checklist |

---

## 📦 Imágenes de sistema: Google Drive y PC del laboratorio

Las imágenes de la mayoría de estos equipos **ya no son descargables del fabricante**. Las copias
del laboratorio son la única fuente.

| Fuente | Ubicación |
|---|---|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA COMPARTIDA --> `` |
| 💻 **PC del laboratorio F104** | Equipo: `PC1` · Ruta: `D:\LabF104\imagenes\` |
| 🗂️ Repositorio Git | [`backups/imagenes/`](backups/imagenes/README.md) (inventario y checksums) |

> 💡 **La PC del laboratorio tiene todas las imágenes descargadas.** Es la primera fuente a la que
> ir cuando un equipo se queda sin OS. El Google Drive es la copia externa por si esa PC falla o se
> reinstala. **Mantén siempre las dos** — una sola copia no es una copia de seguridad.

Este mismo bloque está repetido en la **ficha** y en el **plan de contingencia** de cada equipo,
con el nombre del fichero exacto que necesita ese chasis.

📀 Prepara además un **USB de rescate en FAT32 (8–16 GB)** con los `.tgz` de Junos: los EX2300 y
los SRX300 sólo se recuperan por USB si dejan de arrancar.

---

## 🔑 Credenciales de acceso

Las credenciales son **comunes por familia**: todos los equipos de una misma familia comparten
usuario y contraseña. La tabla también está en la ficha de cada equipo.

| Familia | Equipos | Enable / Root | Acceso |
|---|---|---|---|
| 🔵 **Routers Cisco** | `RT-C2503-01/02` · `RT-C2620-01/02` | `<enable secret>` | Consola · Telnet |
| 🔵 **Switches Cisco** | `SW-C2900XL-01` · `SW-C2950-01` | `<enable secret>` | Consola · Telnet |
| 🟢 **Switches 3Com** | `SW-3C4500G-01/02` · `SW-3C4210-01/02` | `<super nivel 3>` | Consola · Telnet · SSH¹ · Web |
| 🟡 **Switches Dell** | `SW-PC7024-01…03` | `<enable>` | Consola · SSH · Web |
| 🟣 **Switches Juniper** | `SW-EX2300-01/02` | `<root>` | Consola · SSH · J-Web |
| 🟣 **Firewalls Juniper** | `FW-SRX300-01/02` | `<root>` | Consola · SSH · J-Web |
| 🟠 **Routers TP-Link (OpenWRT)** | `RT-MR3420-01/02` | — (`root` es ya el superusuario) | SSH · LuCI (web) · telnet en *failsafe* |

¹ SSH disponible en el 4500G (Comware v5). En el 4210 ⚠️ por confirmar.

### Contraseñas de gestor de arranque

Se pierden y **dejan el equipo irrecuperable**.

| Equipo | Qué protege | Valor |
|---|---|---|
| `SW-3C4500G-01/02` | Menú BootROM (`Ctrl+B`) | `<rellenar>` |
| `SW-3C4210-01/02` | Menú BootROM (`Ctrl+B`) | `<rellenar>` |

> [!CAUTION]
> **En los 3Com, si se pierde la contraseña del BootROM además de la del sistema, el switch no es
> recuperable por consola.** Es el único punto del laboratorio sin vía de rescate.

> [!WARNING]
> **Ningún equipo Cisco del laboratorio tiene SSH** (confirmado con `show version`: el 2950 corre
> `Standard Image` y los 2620 la imagen `C2600-IS-M`, ambas sin criptografía). Todo el acceso
> remoto a los Cisco es **Telnet*.  Ver [avisos transversales](docs/01-comparativa.md#️-avisos-transversales-del-laboratorio).

### Servidor de apoyo

| Servicio | IP | Notas |
|---|---|---|
| TFTP / FTP (respaldos e imágenes) | `192.168.104.10` | Ver [servidor de rescate](docs/02-plan-contingencia.md#-servidor-tftp-de-rescate) |

---

## 📋 Inventario general

| Cant. | Equipo | Tipo | Capa | SO instalado | Carpetas |
|:--:|---|---|:--:|---|---|
| 2 | 3Com Switch 4500G 24-Port | Switch gestionable | L2/L3 | 3Com OS V5.01.03s56 | [01](equipos/SW-3C4500G-01/) · [02](equipos/SW-3C4500G-02/) |
| 2 | 3Com Switch 4210 26-Port | Switch gestionable | L2 | ⚠️ pendiente | [01](equipos/SW-3C4210-01/) · [02](equipos/SW-3C4210-02/) |
| 1 | Cisco Catalyst WS-C2924-XL-EN | Switch gestionable | L2 | IOS 11.2(8.11)SA6 | [01](equipos/SW-C2900XL-01/) |
| 1 | Cisco Catalyst WS-C2950-24 | Switch gestionable | L2 | IOS 12.1(22)EA13 SI | [01](equipos/SW-C2950-01/) |
| 2 | Cisco 2503 | Router WAN / ISDN | L3 | IOS 11.2(17) Ent · IOS 11.1(17) | [01](equipos/RT-C2503-01/) · [02](equipos/RT-C2503-02/) |
| 2 | Cisco 2620 | Router modular | L3 | IOS 12.2(27) IP Plus | [01](equipos/RT-C2620-01/) · [02](equipos/RT-C2620-02/) |
| 3 | Dell PowerConnect 7024 | Switch gestionable | L2/L3 | ⚠️ pendiente | [01](equipos/SW-PC7024-01/) · [02](equipos/SW-PC7024-02/) · [03](equipos/SW-PC7024-03/) |
| 2 | Juniper EX2300-24T | Switch gestionable | L2/L3 | Junos 18.1R3.3 | [01](equipos/SW-EX2300-01/) · [02](equipos/SW-EX2300-02/) |
| 2 | TP-Link TL-MR3420 | Router inalámbrico (OpenWRT) | L3 | LEDE 17.01 `git-19.167…` | [01](equipos/RT-MR3420-01/) · [02](equipos/RT-MR3420-02/) |
| 2 | Juniper SRX300 | Firewall / Router de servicios | L3–L7 | ⚠️ pendiente | [01](equipos/FW-SRX300-01/) · [02](equipos/FW-SRX300-02/) |
| **19** | **Total de equipos** | | | | |

---

## 🔌 Conexión por consola

Todos los equipos del laboratorio usan los mismos parámetros:

| Parámetro | Valor |
|---|---|
| Velocidad | `9600` baudios (Los 3com usan `115200` baudios) |
| Bits de datos | 8 |
| Paridad | Ninguna |
| Bits de stop | 1 |
| Control de flujo | Ninguno |
| Cable | RJ-45 rollover + adaptador USB-serie |

> ⚠️ Si la consola muestra caracteres corruptos, prueba `115200`: algunos gestores de arranque y el
> ROMmon de Cisco cambian de velocidad.

> ⚠️ **Los dos TP-Link TL-MR3420 no tienen consola externa**: su UART está dentro de la carcasa.
> Se acceden por **SSH** y **LuCI**, y para recuperar la contraseña se usa el
> [modo *failsafe*](equipos/RT-MR3420-01/plan-contingencia.md) por telnet.

**Desde Windows 11** — usa PuTTY o Tera Term. Para encontrar el puerto COM:

```powershell
Get-PnpDevice -Class Ports -Status OK | Select-Object FriendlyName, Status
```

**Desde Linux:**

```bash
sudo screen /dev/ttyUSB0 9600
```

| Acción | `screen` | `minicom` | PuTTY |
|---|---|---|---|
| Salir | `Ctrl+A` `K` | `Ctrl+A` `X` | Cerrar ventana |
| Enviar **Break** (ROMmon Cisco) | `Ctrl+A` `Ctrl+B` | `Ctrl+A` `F` | `Ctrl+Break` |
| Registrar sesión en fichero | `Ctrl+A` `H` | `Ctrl+A` `L` | *Session → Logging* |

---

## 🏷️ Convenciones del laboratorio

**Nomenclatura de hostname:** `F104-<TIPO>-<MODELO>-<NN>`
Ejemplos: `F104-SW-4500G-01`, `F104-RT-2620-02`, `F104-FW-SRX300-01`

⚠️ Varios equipos aún tienen hostnames por defecto o duplicados —
ver [la tabla de renombrado](docs/01-comparativa.md#️-avisos-transversales-del-laboratorio).

**Direccionamiento**

| Rango | Uso |
|---|---|
| `172.16.10.0/24` · `192.168.1.0/24` | ⚠️ Routers TP-Link, **fuera** del esquema de gestión |

**Etiquetado físico:** cada equipo lleva etiqueta visible con `ID` + **código QR**
que apunta a su carpeta en `equipos/`. Las etiquetas están generadas y listas para imprimir en
[`etiquetas/`](etiquetas/README.md).

---

## 🗂️ Estructura del repositorio

```text
CiscoLabs/
├── README.md                       ← estás aquí (credenciales, imágenes, inventario)
├── equipos/                        ← UNA CARPETA POR CHASIS (destino de los QR)
│   ├── README.md                   ← índice de equipos
│   ├── SW-3C4500G-01/
│   │   ├── README.md               ← ficha: identificación, acceso, SO, hardware, imágenes
│   │   ├── caracteristicas.md      ← características y protocolos
│   │   ├── chuleta-comandos.md     ← comandos de ese equipo
│   │   └── plan-contingencia.md    ← contraseña, OS, respaldo, checklist
│   ├── SW-3C4500G-02/  …           ← misma estructura en las 19 carpetas
│   └── FW-SRX300-02/
├── docs/
│   ├── 01-comparativa.md           ← vista de conjunto, memoria, riesgos
│   ├── 02-plan-contingencia.md     ← procedimientos comunes y servidor de rescate
│   ├── 03-chuleta-comandos.md      ← «Piedra Rosetta» de las 4 CLI
│   └── 04-bitacora.md              ← registro de incidencias
├── etiquetas/                      ← CÓDIGOS QR PARA EL CHASIS
│   ├── etiquetas-QR-F104.pdf       ← hoja A4 lista para imprimir (2 páginas)
│   ├── qr/<ID>.png                 ← los 19 QR por separado
│   ├── logo/EMBLEMA-USFX-logo.png  ← emblema de la universidad
│   └── generar-etiquetas.py        ← script para regenerarlos
└── backups/
    ├── configs/                    ← respaldos de configuración (versionados)
    └── imagenes/                   ← inventario y checksums de las imágenes
```

---

## 🎯 Tareas pendientes

- [x] Pegar el enlace del **Google Drive** en este README y en las fichas y planes de contingencia
- [x] Anotar el **nombre de la PC del laboratorio** que guarda las imágenes
- [ ] Rellenar las **credenciales por familia** (arriba y en cada ficha)
- [ ] Capturar los [datos que faltan](docs/01-comparativa.md#-datos-pendientes-de-capturar): 4210 (todo), PowerConnect (firmware), SRX300 (versión de Junos), TL-MR3420 (revisión de hardware)
- [ ] Respaldar las imágenes de los equipos 🔴 de [prioridad 1](docs/01-comparativa.md#riesgo-de-pérdida-de-imagen)
- [x] Renombrar los hostnames duplicados (`L3Switch` ×3, `Router` ×2, `SW_servers`/`SW_SERVERS`)
