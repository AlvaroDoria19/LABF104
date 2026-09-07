# 📝 Bitácora del Laboratorio F104

[⬅️ Volver al índice](../README.md)

> Registro histórico de cambios, incidencias, préstamos y mantenimiento.
> **Añade las entradas nuevas arriba** (orden cronológico inverso) y haz commit al repositorio.

---

## 🧭 Cómo usar esta bitácora

| Tipo | Etiqueta | Cuándo se usa |
|---|---|---|
| Configuración | `🔧 CONFIG` | Cambio de configuración que se queda en el equipo |
| Incidencia | `🔴 FALLO` | Avería, equipo caído, comportamiento anómalo |
| Recuperación | `🚨 RESCATE` | Recuperación de contraseña o de imagen de sistema |
| Actualización | `⬆️ UPGRADE` | Cambio de versión de SO/firmware |
| Mantenimiento | `🧹 MANT` | Limpieza, respaldo, revisión rutinaria |
| Préstamo | `📦 PRÉSTAMO` | Equipo sacado del rack para una práctica o clase |
| Inventario | `🏷️ INVENTARIO` | Alta, baja o traslado de equipo |

---

## 📊 Estado actual del laboratorio

| Última revisión general | Equipos operativos | Con incidencia | Fuera de servicio |
|---|:--:|:--:|:--:|
| `2026-09-04` | 17 / 17 | 0 | 0 |

### Incidencias abiertas

| ID | Equipo | Fecha | Descripción | Prioridad | Responsable |
|---|---|---|---|:--:|---|
| — | — | — | *(sin incidencias abiertas)* | — | — |

---

## 🗓️ Registro de entradas

<!-- ▼▼▼ AÑADE LAS ENTRADAS NUEVAS AQUÍ, ARRIBA ▼▼▼ -->

### `2026-09-04` · 🏷️ INVENTARIO · Todos los equipos

- **Qué se hizo:** creación de la documentación técnica del laboratorio (fichas, plan de
  contingencia y chuleta de comandos).
- **Pendiente:** completar en sitio los campos marcados con ⚠️ (modelo exacto, nº de serie y
  versión de SO real de cada equipo) y hacer el primer respaldo de configuraciones.
- **Realizado por:** `<tu nombre>`

---

## 📋 Plantillas

### Plantilla — cambio de configuración

````markdown
### `AAAA-MM-DD` · 🔧 CONFIG · <ID equipo>

- **Motivo:** ...
- **Cambio realizado:** ...
- **Comandos aplicados:**
  ```text
  ...
  ```
- **Verificación:** ...
- **Respaldo actualizado:** backups/configs/<ID>_AAAA-MM-DD.cfg — sí / no
- **Realizado por:** ...
````

### Plantilla — incidencia

```markdown
### `AAAA-MM-DD` · 🔴 FALLO · <ID equipo>

- **Síntoma:** ...
- **Detectado por:** ...
- **Diagnóstico:** (salida de `show ...` relevante)
- **Acción tomada:** ...
- **Estado:** 🟢 resuelto / 🟡 mitigado / 🔴 abierto
- **Tiempo fuera de servicio:** ... min
```

### Plantilla — recuperación (contraseña o imagen)

```markdown
### `AAAA-MM-DD` · 🚨 RESCATE · <ID equipo>

- **Problema:** contraseña perdida / imagen corrupta / configuración borrada
- **Procedimiento usado:** (enlace a 02-plan-contingencia.md#seccion)
- **Imagen utilizada:** <nombre exacto del fichero>
- **Credenciales nuevas anotadas en README:** sí / no
- **config-register / boot system / snapshot restaurados:** sí / no
- **Tiempo total:** ... min
- **Notas para la próxima vez:** ...
```

### Plantilla — actualización de software

```markdown
### `AAAA-MM-DD` · ⬆️ UPGRADE · <ID equipo>

- **Versión anterior:** ...
- **Versión nueva:** ...
- **Imagen:** <nombre del fichero> (respaldada en backups/imagenes/ — sí / no)
- **Método:** TFTP / XMODEM / USB / request system software add
- **Snapshot / imagen de respaldo conservada:** sí / no
- **Problemas encontrados:** ...
```

### Plantilla — préstamo de equipo

```markdown
### `AAAA-MM-DD` · 📦 PRÉSTAMO · <ID equipo>

- **Solicitante:** ... (asignatura / grupo)
- **Fecha de salida:** ... · **Devolución prevista:** ...
- **Accesorios incluidos:** cable de consola / transceptor AUI / cable serie DB-60 / SFP / fuente
- **Estado a la salida:** ...
- **Devuelto el:** ... · **Estado a la devolución:** ...
- **Configuración base restaurada:** sí / no
```

---

## ✅ Control mensual de respaldos

| Mes | Configs respaldadas | Commit en Git | Imágenes verificadas | Firmado por |
|---|:--:|:--:|:--:|---|
| 2026-09 | ☐ | ☐ | ☐ | |
| 2026-10 | ☐ | ☐ | ☐ | |
| 2026-11 | ☐ | ☐ | ☐ | |
| 2026-12 | ☐ | ☐ | ☐ | |

---

## 📦 Control de accesorios críticos

Los accesorios se pierden más que los equipos. Contar al inicio y al final de cada semestre.

| Accesorio | Necesario para | Cantidad | Verificado |
|---|---|:--:|:--:|
| Cable de consola RJ-45 rollover | Todos los equipos | | ☐ |
| Adaptador USB → serie (DB-9) | Todos los equipos | | ☐ |
| Transceptor AUI → RJ-45 | Cisco 2503 (obligatorio) | | ☐ |
| Cable serie DB-60 DTE/DCE | Cisco 2503 / 2620 (WIC-1T) | | ☐ |
| Módulos WIC-1T / WIC-2T | Cisco 2620 | | ☐ |
| SFP 1000Base-T / SX | 4500G · PC7024 · EX2300 | | ☐ |
| SFP+ 10G / cables DAC | EX2300 (uplinks y Virtual Chassis) | | ☐ |
| SFP 1GbE | SRX300 (puertos ge-0/0/6-7) | | ☐ |
| Módulos 10G para bahías | Dell PowerConnect 7024 | | ☐ |
| Memoria USB de rescate (FAT32, 8–16 GB) | EX2300 · SRX300 — **única vía de rescate** | | ☐ |
| Antenas WiFi desmontables (2 por router) | TP-Link TL-MR3420 | | ☐ |
| Adaptador USB-TTL de **3,3 V** | TL-MR3420 — rescate por UART (⚠️ nunca de 5 V) | | ☐ |
| Módem USB 3G/4G | TL-MR3420 — prácticas de respaldo por red móvil | | ☐ |

---

[⬅️ Volver al índice](../README.md) · [🚨 Plan de contingencia](02-plan-contingencia.md)
