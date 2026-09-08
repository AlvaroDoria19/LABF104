# 🚨 SW-3C4210-01 — Plan de contingencia

**3Com Switch 4210 26-Port**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

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

## 🔐 A) Contraseña perdida

**Método: menú BootROM → «Skip Current System Configuration».**

1. Consola a `9600 8N1`.
2. Reinicia y pulsa **`Ctrl+B`** cuando aparezca `Press Ctrl-B to enter Boot Menu...`
   (primeros ~5 segundos).
3. Si pide contraseña de BootROM, usa la anotada en [Acceso](README.md#-acceso).

> [!CAUTION]
> **Si la contraseña de BootROM también se ha perdido, el switch no es recuperable por consola.**

4. Elige la opción **«Skip Current System Configuration»** (⚠️ el número varía en Comware v3 —
   **lee el menú real**, no lo asumas).
5. Reinicia desde el menú (opción `0`). Arranca sin aplicar la configuración.
6. **Lee primero la configuración guardada:**

```text
<Switch> display saved-configuration
```

> [!WARNING]
> La configuración en ejecución está **vacía**. Un `save` en este momento **borra la configuración
> del switch**.

7. Cambia las contraseñas y guarda:

```text
<Switch> system-view
[Switch] local-user admin
[Switch-luser-admin]  password simple <nueva-clave>
[Switch-luser-admin]  service-type telnet terminal
[Switch-luser-admin]  authorization-attribute level 3
[Switch-luser-admin] quit
[Switch] super password level 3 simple <nueva-clave>
[Switch] quit
<Switch> save
```

8. Restaura la configuración completa desde el respaldo si el paso 7 sobrescribió `startup.cfg`.

---

## 📀 B) Sistema operativo borrado o corrupto

**Rescate desde el menú BootROM:**

1. `Ctrl+B` durante el arranque para entrar al menú.
2. Elige **«Download application file to flash»** y el método: **TFTP**, **FTP** o **XMODEM**.
3. Con TFTP el menú pide: IP del switch (`192.168.104.13`), máscara (`255.255.255.0`),
   gateway (`192.168.104.1`), IP del servidor (`192.168.104.10`) y nombre del fichero.
4. Marca el fichero como **`main`** cuando lo pregunte.
5. Si la flash está llena, usa antes **«Delete file from flash»** — ⚠️ sólo tras confirmar que
   tienes la imagen nueva lista.
6. Reinicia (opción `0`) y verifica:

```text
<Switch> dir flash:/
<Switch> display boot-loader
<Switch> display version
```

**Reset de fábrica** (⚠️ borra toda la configuración):

```text
<Switch> reset saved-configuration
<Switch> reboot
```

> ⚠️ La flash de este modelo es pequeña: es probable que **no quepan dos imágenes**. Comprueba el
> espacio con `dir flash:/` antes de cualquier actualización y no borres la imagen actual sin tener
> la nueva verificada y el servidor TFTP probado.

---

## 💾 Respaldo de configuración

```text
display current-configuration
tftp 192.168.104.10 put flash:/startup.cfg SW-3C4210-01_AAAA-MM-DD.cfg
```

> ⚠️ En Comware v3 el fichero puede llamarse `config.cfg`. Confírmalo con `dir flash:/`.

Sacar la imagen de sistema por FTP — **`binary` es obligatorio**:

```text
dir flash:/
ftp 192.168.104.10
```

```text
binary
cd imagenes
put flash:/<imagen>.bin SW-3C4210-01_<imagen>.bin
bye
```

Restaurar configuración:

```text
tftp 192.168.104.10 get SW-3C4210-01_base.cfg flash:/startup.cfg
reboot
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

````markdown
### Intervención — SW-3C4210-01 — AAAA-MM-DD

- [ ] Aviso previo: no había práctica en curso
- [ ] Síntoma observado: ...
- [ ] Acceso preparado (consola / SSH / failsafe): ...
- [ ] Configuración anterior recuperada / disponible en backups: sí / no
- [ ] Procedimiento aplicado: contraseña / restauración de imagen / reset de fábrica
- [ ] Imagen usada (nombre exacto): ...
- [ ] Fuente de la imagen: Google Drive / PC del laboratorio / repositorio
- [ ] Credenciales nuevas anotadas en la ficha y en el README: sí / no
- [ ] Respaldo de la configuración final subido al servidor TFTP (PC-1): sí / no
- [ ] Verificación final OK: sí / no
- Tiempo total: ... min · Realizado por: ...
````

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
