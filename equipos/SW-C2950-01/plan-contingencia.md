# 🚨 SW-C2950-01 — Plan de contingencia

**Cisco Catalyst WS-C2950-24**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2950-i6q4l2-mz.121-22.EA13.bin`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

---

## 🔐 A) Contraseña perdida

**Método: botón `MODE`.** No necesita red ni servidor y conserva la configuración.

1. Conecta la consola a `9600 8N1`.
2. **Desconecta la alimentación.**
3. **Mantén pulsado `MODE`** y **vuelve a conectar la alimentación**. Suelta cuando el LED sobre el
   puerto `1X` se apague.
4. Prompt del gestor de arranque: `switch:`
5. Inicializa la flash y **renombra** la configuración (no la borres):

```text
switch: flash_init
switch: load_helper
switch: dir flash:
switch: rename flash:config.text flash:config.old
switch: boot
```

6. Arranca sin configuración. Rechaza el asistente (`no`) y recupera tu config:

```text
Switch> enable
Switch# rename flash:config.old flash:config.text
Switch# copy flash:config.text system:running-config
```

7. Cambia las contraseñas:

```text
Switch# configure terminal
Switch(config)# enable secret <nueva-clave>
Switch(config)# line console 0
Switch(config-line)#  password <nueva-clave>
Switch(config-line)#  login
Switch(config-line)# exit
Switch(config)# line vty 0 4
Switch(config-line)#  password <nueva-clave>
Switch(config-line)#  login
Switch(config-line)# end
Switch# write memory
```

8. Anota las nuevas credenciales en [Acceso](README.md#-acceso) y en el [README](../README.md).

> 💡 Para dejarlo de fábrica: `delete flash:config.text` + `delete flash:vlan.dat` en el paso 5.

---

## 📀 B) Sistema operativo borrado o corrupto

1. Entra al prompt `switch:` con el botón `MODE` (pasos 1-4 del apartado anterior).
2. Inicializa la flash y comprueba el espacio:

```text
switch: flash_init
switch: load_helper
switch: dir flash:
```

3. **TFTP** (rápido, recomendado):

```text
switch: set IP_ADDR 192.168.104.16
switch: set NETMASK 255.255.255.0
switch: set DEFAULT_ROUTER 192.168.104.1
switch: set TFTP_SERVER 192.168.104.10
switch: copy tftp: flash:c2950-i6q4l2-mz.121-22.EA13.bin
```

4. **XMODEM** si no hay red disponible:

```text
switch: copy xmodem: flash:c2950-i6q4l2-mz.121-22.EA13.bin
```

5. Arranca con la imagen recuperada:

```text
switch: boot flash:c2950-i6q4l2-mz.121-22.EA13.bin
```

6. Fija la variable de arranque de forma permanente:

```text
Switch# configure terminal
Switch(config)# boot system flash:c2950-i6q4l2-mz.121-22.EA13.bin
Switch(config)# end
Switch# write memory
Switch# show boot
```

> 💡 Con ~8 MB de flash puede que quepan **dos imágenes** (la actual ocupa ≈ 3,5 MB). Compruébalo
> con `dir flash:`: si hay sitio, copia una segunda copia como `respaldo.bin` y añade
> `boot system flash:respaldo.bin` como segunda opción de arranque. Es la mejor protección posible.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/SW-C2950-01_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema por FTP:

```text
dir flash:
configure terminal
 ip ftp username labftp
 ip ftp password <clave>
 end
copy flash:c2950-i6q4l2-mz.121-22.EA13.bin ftp://192.168.104.10/SW-C2950-01_c2950-i6q4l2-mz.121-22.EA13.bin
```

Restaurar configuración:

```text
copy tftp://192.168.104.10/SW-C2950-01_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — SW-C2950-01 — AAAA-MM-DD

- [ ] Aviso previo: no había práctica en curso
- [ ] Síntoma observado: ...
- [ ] Acceso preparado (consola / SSH / failsafe): ...
- [ ] Configuración anterior recuperada / disponible en backups: sí / no
- [ ] Procedimiento aplicado: contraseña / restauración de imagen / reset de fábrica
- [ ] Imagen usada (nombre exacto): ...
- [ ] Fuente de la imagen: Google Drive / PC del laboratorio / repositorio
- [ ] Credenciales nuevas anotadas en la ficha y en el README: sí / no
- [ ] Respaldo de la configuración final subido a backups/configs/: sí / no
- [ ] Verificación final OK: sí / no
- Tiempo total: ... min · Realizado por: ...
````

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
