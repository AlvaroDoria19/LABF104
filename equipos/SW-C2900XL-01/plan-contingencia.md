# 🚨 SW-C2900XL-01 — Plan de contingencia

**Cisco Catalyst WS-C2924-XL-EN**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2900xl-hs-mz-112.8.11-SA6.bin`

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

**Método: botón `MODE`.** No necesita red ni servidor. Es rápido y no pierde la configuración.

1. Conecta la consola a `9600 8N1`.
2. **Desconecta la alimentación.**
3. **Mantén pulsado el botón `MODE`** (frontal, junto a los LEDs) y **vuelve a conectar la
   alimentación**. Suelta el botón cuando el LED sobre el puerto `1X` se apague.
4. Aparece el gestor de arranque: `switch:`
5. Inicializa la flash y **renombra** el fichero de configuración (no lo borres):

```text
switch: flash_init
switch: load_helper
switch: dir flash:
switch: rename flash:config.text flash:config.old
switch: boot
```

6. Arranca sin configuración. Rechaza el asistente (`no`) y recupera tu config original:

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

8. Anota las nuevas credenciales en la sección [Acceso](README.md#-acceso) de este fichero y en el
   [README](../README.md).

> 💡 Para dejarlo **limpio de fábrica**, en el paso 5 usa `delete flash:config.text` y
> `delete flash:vlan.dat` en lugar de `rename` (⚠️ pierdes la configuración).

---

## 📀 B) Sistema operativo borrado o corrupto

> [!CAUTION]
> **Es el equipo más delicado del laboratorio en este aspecto.** Con ~4 MB de flash **no caben dos
> imágenes**: para poner una nueva hay que borrar la actual, y durante ese hueco el switch no tiene
> sistema. No inicies el proceso sin: (a) la imagen respaldada y verificada, (b) la consola
> conectada, y (c) el servidor TFTP probado.

1. Entra al prompt `switch:` con el botón `MODE` (pasos 1-4 del apartado anterior).
2. Inicializa la flash y mira qué hay y cuánto espacio queda:

```text
switch: flash_init
switch: load_helper
switch: dir flash:
```

3. **XMODEM por consola** (no necesita red, es la vía más segura en esta plataforma):

```text
switch: copy xmodem: flash:c2900xl-hs-mz-112.8.11-SA6.bin
```

Desde el terminal, envía el fichero por XMODEM (`Ctrl+A S` → *xmodem* en `minicom`; en PuTTY usa
Tera Term o `sx` si no lo soporta).

4. **TFTP** si el gestor de arranque lo admite (compruébalo con `?` en el prompt `switch:`):

```text
switch: set IP_ADDR 192.168.104.15
switch: set NETMASK 255.255.255.0
switch: set DEFAULT_ROUTER 192.168.104.1
switch: set TFTP_SERVER 192.168.104.10
switch: copy tftp: flash:c2900xl-hs-mz-112.8.11-SA6.bin
```

5. Arranca con la imagen recuperada:

```text
switch: boot flash:c2900xl-hs-mz-112.8.11-SA6.bin
```

6. Fija la variable de arranque de forma permanente:

```text
Switch# configure terminal
Switch(config)# boot system flash:c2900xl-hs-mz-112.8.11-SA6.bin
Switch(config)# end
Switch# write memory
Switch# show boot
```

> 💡 Este switch guarda además el directorio `flash:html/` que usa su interfaz web. Si quieres una
> copia **completa** de la flash (imagen + web + config), prueba:
> ```text
> archive tar /create tftp://192.168.104.10/SW-C2900XL-01_flash.tar flash:
> ```
> ⚠️ Verifica primero que el comando existe con `archive ?`.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/SW-C2900XL-01_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema (en esta plataforma **usa TFTP**, el cliente FTP puede no existir):

```text
dir flash:
copy flash:c2900xl-hs-mz-112.8.11-SA6.bin tftp://192.168.104.10/SW-C2900XL-01_c2900xl-hs-mz-112.8.11-SA6.bin
```

Restaurar configuración:

```text
copy tftp://192.168.104.10/SW-C2900XL-01_base.cfg flash:config.text
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

````markdown
### Intervención — SW-C2900XL-01 — AAAA-MM-DD

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
