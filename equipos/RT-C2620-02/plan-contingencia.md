# 🚨 RT-C2620-02 — Plan de contingencia

**Cisco 2620 (serie 2600)**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2600-is-mz.122-27`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ ⚠️ En este router el `show version` reporta la imagen como `flash:c2600-is-mz.122-27` **sin la extensión `.bin`** (a diferencia de su gemelo). Confirma el nombre exacto con `show flash:` y cópialo tal cual, o el arranque fallará.

---

## 🔐 A) Contraseña perdida

**Método: `config-register 0x2142` (ignorar NVRAM).** Necesita consola y reinicio.

1. Conecta la consola a `9600 8N1`.
2. Apaga y enciende el router y **envía `Break` en los primeros 60 segundos**
   (`Ctrl+Break` en PuTTY · `Ctrl+A Ctrl+B` en `screen` · `Ctrl+A F` en `minicom`).
3. Aparece el ROM Monitor → `rommon 1 >`:

```text
rommon 1 > confreg 0x2142
rommon 2 > reset
```

4. Arranca sin configuración. Rechaza el asistente con `no` y **carga la config guardada en RAM**:

```text
Router> enable
Router# copy startup-config running-config
```

> [!CAUTION]
> **Nunca al revés.** `copy running-config startup-config` aquí **borraría** la configuración.

5. Cambia contraseñas y **restaura el registro**:

```text
Router# configure terminal
Router(config)# enable secret <nueva-clave>
Router(config)# line console 0
Router(config-line)#  password <nueva-clave>
Router(config-line)#  login
Router(config-line)# exit
Router(config)# line vty 0 4
Router(config-line)#  password <nueva-clave>
Router(config-line)#  login
Router(config-line)# exit
Router(config)# config-register 0x2102
Router(config)# end
Router# write memory
Router# reload
```

6. Verifica con `show version` que dice `Configuration register is 0x2102`.

---

## 📀 B) Sistema operativo borrado o corrupto

Este router tiene **6,4 MB libres en flash**, así que lo primero es aprovecharlo:

> [!TIP]
> **Medida preventiva recomendada.** Copia una segunda imagen a la propia flash. Si la principal se
> corrompe, el rescate es un simple `boot system` sin cables ni servidores:
> ```text
> copy tftp://192.168.104.10/c2600-is-mz.122-27.bin flash:respaldo.bin
> configure terminal
>  boot system flash:c2600-is-mz.122-27.bin
>  boot system flash:respaldo.bin
> end
> write memory
> ```

**Si el router ya no arranca — ROM Monitor + TFTP (rápido):**

1. Consola a `9600 8N1`, `Break` durante el arranque → `rommon 1 >`.
2. Conecta el cable a `FastEthernet0/0` y la PC del laboratorio con el servidor TFTP en `192.168.104.10`.

```text
rommon 1 > IP_ADDRESS=192.168.104.44
rommon 2 > IP_SUBNET_MASK=255.255.255.0
rommon 3 > DEFAULT_GATEWAY=192.168.104.1
rommon 4 > TFTP_SERVER=192.168.104.10
rommon 5 > TFTP_FILE=c2600-is-mz.122-27.bin
rommon 6 > set
rommon 7 > tftpdnld
```

Confirma con `y` cuando avise de que **borrará la flash**.

3. Arranca y fija la imagen:

```text
rommon 8 > reset
Router# configure terminal
Router(config)# boot system flash:c2600-is-mz.122-27.bin
Router(config)# config-register 0x2102
Router(config)# end
Router# write memory
```

**Si no hay red — XMODEM por consola:**

```text
rommon 1 > xmodem -c c2600-is-mz.122-27.bin
```

Para acelerar, antes sube la velocidad con `confreg` (responde `y` a *change console baud rate*,
elige `115200`) y **reconecta el terminal a 115200**. Al terminar, vuelve a `9600` y `0x2102`.
A 9600 bps una imagen de 10 MB tarda unas 3 horas; a 115200 unos 15 minutos.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/RT-C2620-02_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema al servidor (FTP es más fiable que TFTP):

```text
configure terminal
 ip ftp username labftp
 ip ftp password <clave>
 end
copy flash:c2600-is-mz.122-27.bin ftp://192.168.104.10/RT-C2620-02_c2600-is-mz.122-27.bin
```

Restaurar:

```text
copy tftp://192.168.104.10/RT-C2620-02_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — RT-C2620-02 — AAAA-MM-DD

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
