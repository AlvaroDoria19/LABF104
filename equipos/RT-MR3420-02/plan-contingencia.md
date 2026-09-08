# 🚨 RT-MR3420-02 — Plan de contingencia

**TP-Link TL-MR3420 (OpenWRT / LEDE)**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ ⚠️ **La revisión del hardware debe coincidir exactamente** (`-v1-` en el nombre). Confírmala con `ubus call system board`. El PC del laboratorio tiene también el firmware original `TL-MR3420_V1_121123.zip`.

---

## 🔐 A) Contraseña perdida

**Método: modo *failsafe*.** No necesita abrir el equipo. Conserva la configuración.

> ⚠️ En *failsafe* el router **siempre** responde en `192.168.1.1`, sea cual sea su IP normal.

1. Conecta el PC a un puerto **LAN** del router con cable y ponle IP fija `192.168.1.2/24`.
2. Desconecta la alimentación del router.
3. Vuelve a darle alimentación y observa el LED **SYS**: cuando empiece a **parpadear rápido**,
   pulsa varias veces el botón **Reset / QSS**. Si lo has acertado, el LED pasa a parpadear
   **aún más rápido**: ya está en *failsafe*.
4. Conéctate por **telnet** (en *failsafe* no hay contraseña y SSH no está activo):

```text
telnet 192.168.1.1
```

> En Windows 11 el cliente telnet no viene activado: `Activar o desactivar características de
> Windows` → `Cliente Telnet`. En Linux, `sudo apt install telnet`.

5. Monta la partición de sobrescritura en lectura/escritura y cambia la contraseña:

```text
mount_root
passwd root
sync
reboot -f
```

6. Anota la nueva contraseña en [Acceso](README.md#-acceso) y en el [README](../../README.md).

**Si además quieres dejarlo de fábrica** (⚠️ borra toda la configuración, incluida la IP y la WiFi):

```text
mount_root
firstboot -y
reboot -f
```

Tras el `firstboot` el router vuelve a `192.168.1.1` sin contraseña y sin WiFi configurada.

**Alternativa por hardware:** con el router encendido, mantén pulsado **Reset unos 10 segundos**
hasta que los LED parpadeen. Equivale a un `firstboot`: ⚠️ **pierdes la configuración**.

---

## 📀 B) Sistema operativo borrado o corrupto

> [!TIP]
> **La configuración de estos routers es texto plano.** Antes de tocar el firmware, saca el
> respaldo (`sysupgrade -b`, ver más abajo): restaurarlo después es inmediato y te ahorra
> reconfigurar VLANs, firewall y WiFi a mano.

### Caso 1 — el router arranca

Comprueba **primero** la revisión de hardware: instalar el firmware de otra revisión deja el
equipo inservible.

```text
ubus call system board
df -h /overlay
```

Copia la imagen al router y actualiza. Usa la imagen **`sysupgrade`** (no la `factory`, que es sólo
para venir del firmware de TP-Link):

```text
scp lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/
```

```text
sysupgrade -n /tmp/lede-17.01.7-ar71xx-generic-tl-mr3420-v1-squashfs-sysupgrade.bin
```

> `-n` **no** conserva la configuración (instalación limpia). Quita el `-n` para conservarla.

También se puede hacer desde LuCI: **System → Backup / Flash Firmware → Flash new firmware image**.

### Caso 2 — el router no arranca: recuperación TFTP de U-Boot

⚠️ **No todas las revisiones de TP-Link tienen esta función.** Si no responde, ve al caso 3.

1. Pon el PC con IP fija **`192.168.0.66/24`** y arranca un servidor TFTP en esa dirección.
2. Coloca el firmware en el directorio del TFTP renombrado al nombre que espera el U-Boot,
   del estilo **`mr3420v1_tp_recovery.bin`** — ⚠️ **confirma el nombre exacto** para tu revisión
   en la página del dispositivo en el wiki de OpenWRT y **anótalo aquí**:

   `Nombre de fichero verificado en este equipo: ______________________________`

3. Conecta el PC a un puerto **LAN** del router.
4. **Mantén pulsado Reset**, da alimentación al router y **sigue pulsando 5–10 segundos**.
5. El router pedirá el fichero al servidor TFTP. Verás la transferencia en el log del servidor.
   **No cortes la alimentación** hasta que reinicie solo (varios minutos).

### Caso 3 — U-Boot por UART (última opción)

Requiere **abrir la carcasa** y un adaptador **USB-TTL de 3,3 V** conectado al UART interno
(`115200 8N1`). Ya en el prompt de U-Boot, la secuencia es del tipo `tftpboot` → `erase` → `cp.b`.

> ⚠️ Un adaptador de 5 V destruye el SoC. Verifica que es de 3,3 V antes de conectarlo.

### Volver al firmware de fábrica de TP-Link

El PC del laboratorio tiene el firmware original **`TL-MR3420_V1_121123.zip`**. Para instalarlo
desde OpenWRT hay que **quitarle los primeros 512 bytes de cabecera**:

```text
dd if=TL-MR3420_V1_121123.bin of=stripped.bin bs=512 skip=1
```

```text
sysupgrade -n -F /tmp/stripped.bin
```

> ⚠️ Operación con riesgo real de dejar el equipo inservible: `-F` desactiva las comprobaciones de
> compatibilidad. Hazla sólo si hace falta de verdad y con la recuperación TFTP ya probada.

---

## 💾 Respaldo de configuración

**Respaldo completo de la configuración** (es un `.tar.gz` con todo `/etc/config`):

```text
sysupgrade -b /tmp/RT-MR3420-02_AAAA-MM-DD.tar.gz
```

Y tráelo al PC del laboratorio:

```text
scp root@192.168.1.1:/tmp/RT-MR3420-02_AAAA-MM-DD.tar.gz .
```

**Ver qué ficheros incluye el respaldo:**

```text
sysupgrade -l
```

**Volcado en texto plano** (cómodo para versionar en Git y ver diferencias):

```text
for f in /etc/config/*; do echo "===== $f"; cat "$f"; done
```

Guárdalo como `backups/configs/RT-MR3420-02_AAAA-MM-DD.txt`.

**Restaurar:**

```text
scp RT-MR3420-02_base.tar.gz root@192.168.1.1:/tmp/
```

```text
sysupgrade -r /tmp/RT-MR3420-02_base.tar.gz
reboot
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

````markdown
### Intervención — RT-MR3420-02 — AAAA-MM-DD

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
