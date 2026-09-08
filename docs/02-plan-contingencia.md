# 🚨 Plan de Contingencia — Laboratorio F104

[⬅️ Volver al índice](../README.md)

> Procedimientos para **recuperar el acceso** (contraseñas perdidas) y **restaurar equipos**
> (configuración borrada o imagen de sistema corrupta).

---

## 📌 Índice

- [🛡️ Prevención: lo que hay que tener hecho ANTES](#️-prevención-lo-que-hay-que-tener-hecho-antes)
- [🧯 Matriz de decisión rápida](#-matriz-de-decisión-rápida)
- [💾 Servidor TFTP de rescate](#-servidor-tftp-de-rescate)
- [🔐 Recuperación de contraseñas](#-recuperación-de-contraseñas)
  - [Cisco Catalyst 2900 XL / 2950](#cisco-catalyst-2900-xl--2950--botón-mode)
  - [Cisco 2503 / 2620](#cisco-2503--2620--config-register-0x2142)
  - [3Com 4500G / 4210](#3com-4500g--4210--menú-bootrom)
  - [Dell PowerConnect 7024](#dell-powerconnect-7024--boot-menu)
  - [Juniper EX2300 / SRX320](#juniper-ex2300--srx320--modo-single-user)
  - [TP-Link TL-MR3420 (OpenWRT)](#tp-link-tl-mr3420-openwrt--modo-failsafe)
- [📀 Recuperación de imágenes de sistema](#-recuperación-de-imágenes-de-sistema)

---

## 🛡️ Prevención: lo que hay que tener hecho ANTES

| # | Medida | Estado |
|:--:|---|:--:|
| 1 | **Copia de cada imagen de sistema** en `backups/imagenes/` (los equipos EOL ya no son descargables) | ☐ |
| 4 | Al menos **2 cables de consola** operativos + adaptador USB-serie de repuesto | &#9724; |
| 5 | **Servidor TFTP** montado y probado (`192.168.104.10`) (PC-1) | &#9724; |
| 6 | Contraseñas registradas en el [bloque de credenciales](../README.md#-credenciales-de-acceso) y verificadas cada semestre | ☐ |
| 7 | **Etiqueta física** en cada equipo con ID y Modelo exacto | &#9724; |
| 8 | En Cisco: `config-register 0x2102` guardado. En Junos: `request system snapshot` hecho | ☐ |

> [!TIP]
> **Regla del laboratorio: ** ningún equipo se apaga sin haber ejecutado antes su comando de
> guardado (`write memory`, `save`, `copy running-config startup-config`, `commit`).
> Y ninguna imagen se borra sin tener otra copia verificada. (Esto para las pruebas de seguridad en redes)

---

## 🧯 Matriz de decisión rápida

| Síntoma | Causa probable | Ir a |
|---|---|---|
| Pide contraseña y ninguna funciona | Password perdida/cambiada | [Recuperación de contraseñas](#-recuperación-de-contraseñas) |
| Arranca sin configuración (hostname por defecto) | `startup-config` borrado o `config-register 0x2142` | [Recuperación de contraseñas](#-recuperación-de-contraseñas) — restaura la config guardada en NVRAM |
| Bucle de reinicio o `boot: cannot open ...` | Imagen borrada o corrupta | [Recuperación de imágenes](#-recuperación-de-imágenes-de-sistema) |
| Se queda en `switch:` / `rommon 1 >` / `loader>` | El equipo no encuentra sistema válido | [Recuperación de imágenes](#-recuperación-de-imágenes-de-sistema) |
| Consola muestra basura o nada | Velocidad incorrecta / cable rollover mal | Probar `9600` y `115200`; cambiar cable |
| Junos: `commit` falla | Falta contraseña de `root` o error de sintaxis | `commit check` y `set system root-authentication` |
| OpenWRT: el cambio no se aplica | Falta `uci commit` | `uci commit <sección>` + reiniciar el servicio |
| No hay LEDs / no arranca | Fallo de fuente de alimentación | Fuera del alcance de este plan → **baja del equipo** |

---

## 💾 Servidor TFTP de rescate

Casi todos los procedimientos de recuperación necesitan un TFTP. Montarlo en la PC-1 del laboratorio en `192.168.104.10`:

```bash
Solo se debe levantar la aplicación TFTP Server de Solawinds en la PC1, apuntar a la carpeta de D:/Backups, y asignarle la IP 192.168.104.10
```


> ⚠️ Apagar el FIREWALL de Windows para permitir las solicitudes a la PC-1

---

## 🔐 Recuperación de contraseñas

> [!WARNING]
> **Todos estos procedimientos requieren acceso físico y consola.** Todos implican **reiniciar el
> equipo** → avisa antes si hay una práctica en curso.

---

### Cisco Catalyst 2900 XL / 2950 — botón MODE

Aplica a: `SW-C2900XL-01`, `SW-C2950-01`

1. Conecta la consola a `9600 8N1`.
2. **Desconecta la alimentación.**
3. **Mantén pulsado el botón `MODE`** (frontal, junto a los LEDs) y **vuelve a conectar la
   alimentación**. Suelta el botón cuando el LED sobre el puerto `1X` se apague (unos segundos).
4. Aparece el prompt del gestor de arranque: `switch:`
5. Inicializa la flash y renombra el fichero de configuración (**no lo borres**):

```text
switch: flash_init
switch: load_helper
switch: dir flash:
switch: rename flash:config.text flash:config.old
switch: boot
```

6. El switch arranca **sin configuración**. Rechaza el asistente inicial (`no`) y entra en modo
   privilegiado:

```text
Switch> enable
Switch# rename flash:config.old flash:config.text
Switch# copy flash:config.text system:running-config
```

7. Ahora tienes la configuración original cargada. Cambia las contraseñas:

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

8. Anota las nuevas contraseñas en el [README](../README.md#-credenciales-de-acceso).

> 💡 Si sólo quieres **dejar el switch limpio**, en el paso 5 usa `delete flash:config.text` en
> lugar de `rename` (⚠️ pierdes la configuración) y borra también `flash:vlan.dat`.

---

### Cisco 2503 / 2620 — config-register `0x2142`

Aplica a: `RT-C2503-01/02`, `RT-C2620-01/02`

1. Consola a `9600 8N1`.
2. Apaga y enciende el router. **En los primeros 60 segundos envía la señal `Break`**
   (`Ctrl+Break` en PuTTY · `Ctrl+A Ctrl+B` en `screen` · `Ctrl+A F` en `minicom`).
3. Debes obtener el ROM Monitor:
   - Cisco 2620 → `rommon 1 >`
   - Cisco 2503 → `>` (monitor del 2500)
4. Configura el registro para **ignorar la NVRAM** y reinicia:

```text
rommon 1 > confreg 0x2142
rommon 2 > reset
```

En el **2503** el equivalente es:

```text
> o/r 0x2142
> i
```

5. El router arranca sin configuración. Rechaza el asistente (`no`), entra en `enable` (sin
   contraseña) y **carga la configuración guardada en la RAM**:

```text
Router> enable
Router# copy startup-config running-config
```

> [!CAUTION]
> **Nunca al revés.** `copy running-config startup-config` en este punto **borraría** la
> configuración del equipo.

6. Cambia las contraseñas y **restaura el registro de configuración**:

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

7. Tras el reinicio, verifica con `show version` que dice
   `Configuration register is 0x2102`.

**Tabla de config-register útil**

| Valor | Efecto |
|---|---|
| `0x2102` | ✅ **Normal**: arranca imagen de flash y carga la NVRAM |
| `0x2142` | Ignora la NVRAM (recuperación de contraseña) |
| `0x2101` | Arranca desde **boot ROM / RXBOOT** (rescate de imagen en el 2500) |
| `0x2100` | Arranca directamente en ROM Monitor |

---

### 3Com 4500G / 4210 — menú BootROM

Aplica a: `SW-3C4500G-01/02`, `SW-3C4210-01/02`

1. Consola a `9600 8N1`.
2. Reinicia el switch y, cuando aparezca
   `Press Ctrl-B to enter Boot Menu...`, pulsa **`Ctrl+B`** en los primeros ~5 segundos.
3. Si pide contraseña de BootROM, prueba la del laboratorio (por defecto suele ser vacía o
   `Please input Bootrom password` → Enter).
4. En el menú de arranque, elige la opción **«Skip Current System Configuration»**
   (habitualmente la **`7`** en Comware v5; ⚠️ el número varía según versión de BootWare — **lee el
   menú real**).
5. Selecciona `0` (Reboot). El switch arranca **sin aplicar** `startup.cfg`, con acceso libre.
6. Recupera la configuración anterior y cambia las contraseñas:

```text
<Switch> display saved-configuration
<Switch> system-view
[Switch] local-user admin
[Switch-luser-admin]  password simple <nueva-clave>
[Switch-luser-admin]  service-type telnet ssh terminal
[Switch-luser-admin]  authorization-attribute level 3
[Switch-luser-admin] quit
[Switch] super password level 3 simple <nueva-clave>
[Switch] quit
<Switch> save
```

> [!IMPORTANT]
> Al arrancar con «skip configuration», la configuración en ejecución está **vacía**. Si haces
> `save` sin más, **sobrescribes `startup.cfg` y pierdes toda la configuración**.
> Primero léela con `display saved-configuration`, cópiala a un fichero, y sólo después `save`.
>
> Alternativa más segura: no hagas `save`; cambia la contraseña, guarda, reinicia y vuelve a
> aplicar la configuración desde tu respaldo TFTP.

7. Buena práctica posterior: proteger el menú con contraseña de BootROM (opción
   *«Modify bootrom password»*) y **anotarla** en el README.

---

### Dell PowerConnect 7024 — Boot Menu

Aplica a: `SW-PC7024-01..03`

1. Consola a `9600 8N1`.
2. Reinicia. Cuando aparezca
   `Select an option. If no selection in 2 seconds then operational code will start.`
   pulsa **`2`** para entrar en el **Boot Menu**.
3. En el menú, selecciona **«Password Recovery Procedure»** (⚠️ suele ser la opción `12`; el número
   depende de la versión de *boot code* — **lee el menú real**).
4. El switch arranca **ignorando las contraseñas** pero **manteniendo la configuración**.
5. Define usuario y contraseñas nuevas y guarda:

```text
console> enable
console# configure
console(config)# username admin password <nueva-clave> privilege 15
console(config)# enable password <nueva-clave>
console(config)# exit
console# copy running-config startup-config
```

6. Reinicia (`reload`) y comprueba que las nuevas credenciales funcionan.

> 💡 Si necesitas **dejar el switch de fábrica**, en el Boot Menu existe la opción
> *«Restore Configuration to Factory Defaults»* — ⚠️ borra la configuración completa.

---

### Juniper EX2300 / SRX320 — modo single-user

Aplica a: `SW-EX2300-01/02`, `FW-SRX320-01/02`

1. Consola a `9600 8N1`.
2. Reinicia el equipo. Cuando aparezca
   `Hit [Enter] to boot immediately, or space bar for command prompt.`
   pulsa la **barra espaciadora** (si se te pasa, vuelve a reiniciar).
3. En el prompt del cargador, arranca en modo single-user:

```text
loader> boot -s
```

4. Cuando pregunte
   `Enter full pathname of shell or 'recovery' for root password recovery:`
   escribe:

```text
recovery
```

5. Se abre la CLI de Junos con privilegios. Fija la contraseña de `root`:

```text
root> configure
root# set system root-authentication plain-text-password
New password: <nueva-clave>
Retype new password: <nueva-clave>
root# commit
root# exit
root> request system reboot
```

6. Si además hay usuarios de laboratorio, aprovecha para recrearlos:

```text
root# set system login user lab-admin class super-user authentication plain-text-password
```

> [!TIP]
> La configuración **no se pierde** con este procedimiento: `recovery` sólo permite editar y
> confirmar. Si necesitas dejar el equipo de fábrica: `request system zeroize`
> (⚠️ borra configuración, licencias locales y logs).

---

### TP-Link TL-MR3420 (OpenWRT) — modo failsafe

Aplica a: `RT-MR3420-01/02`

> ⚠️ Estos routers **no tienen consola externa**: el UART está dentro de la carcasa. El rescate se
> hace por red, en modo *failsafe*, donde el router **siempre** responde en `192.168.1.1`.

1. Conecta el PC a un puerto **LAN** del router y ponle IP fija `192.168.1.2/24`.
2. Desconecta la alimentación del router.
3. Vuelve a darle alimentación y observa el LED **SYS**: cuando empiece a **parpadear rápido**,
   pulsa varias veces el botón **Reset / QSS**. Si lo aciertas, el LED pasa a parpadear **aún más
   rápido**: ya está en *failsafe*.
4. Conéctate por **telnet** (en *failsafe* no hay contraseña y SSH está desactivado):

```text
telnet 192.168.1.1
```

> En Windows 11 el cliente telnet no viene activado: `Activar o desactivar características de
> Windows` → `Cliente Telnet`. En Linux, `sudo apt install telnet`.

5. Monta la partición de sobrescritura y cambia la contraseña:

```text
mount_root
passwd root
sync
reboot -f
```

6. Anota la nueva contraseña en el [README](../README.md#-credenciales-de-acceso).

**Para dejarlo de fábrica** (⚠️ borra configuración, IP y WiFi):

```text
mount_root
firstboot -y
reboot -f
```

O por hardware: con el router encendido, mantén **Reset unos 10 segundos**.

Procedimiento completo, incluida la recuperación del firmware por TFTP de U-Boot, en el
[plan de contingencia del equipo](../equipos/RT-MR3420-01/plan-contingencia.md).

---

## 📀 Recuperación de imágenes de sistema

> [!CAUTION]
> Antes de empezar: confirma que **tienes la imagen** en `backups/imagenes/` (o en `/srv/tftp/`) y
> anota su nombre exacto. Sin la imagen, ningún procedimiento sirve.

### Cisco Catalyst 2900 XL / 2950 — desde el gestor de arranque

1. Entra al prompt `switch:` con el botón `MODE` (pasos 1-4 de
   [este procedimiento](#cisco-catalyst-2900-xl--2950--botón-mode)).
2. Inicializa la flash y comprueba qué hay:

```text
switch: flash_init
switch: load_helper
switch: dir flash:
```

3. **Opción A — XMODEM por consola** (lenta pero no necesita red; sube la velocidad si puedes):

```text
switch: copy xmodem: flash:c2950-i6q4l2-mz.121-22.EA14.bin
```

Y desde el emulador de terminal, envía el fichero por XMODEM (en `minicom`: `Ctrl+A S` → *xmodem*).

4. **Opción B — TFTP** (sólo en gestores de arranque que lo soportan; en el 2950 disponible en
   versiones recientes ⚠️):

```text
switch: set IP_ADDR 192.168.104.16
switch: set NETMASK 255.255.255.0
switch: set DEFAULT_ROUTER 192.168.104.1
switch: set TFTP_SERVER 192.168.104.10
switch: copy tftp: flash:c2950-i6q4l2-mz.121-22.EA14.bin
```

5. Indica la imagen de arranque y reinicia:

```text
switch: boot flash:c2950-i6q4l2-mz.121-22.EA14.bin
```

6. Una vez arrancado, fija la variable de arranque de forma permanente:

```text
Switch# configure terminal
Switch(config)# boot system flash:c2950-i6q4l2-mz.121-22.EA14.bin
Switch(config)# end
Switch# write memory
Switch# show boot
```

> ⚠️ **2900 XL (4 MB de flash):** no caben dos imágenes. Antes de copiar hay que borrar la vieja
> (`delete flash:<imagen>`), lo que deja el switch temporalmente sin sistema. Hazlo sólo con la
> consola conectada, el TFTP probado y sin prisa.

---

### Cisco 2503 — recuperación de imagen vía RXBOOT

El 2500 ejecuta el IOS **desde la flash**: si la imagen está corrupta, el router no arranca. Se
rescata con el **IOS reducido que vive en la ROM (RXBOOT)**, entrando primero con:

```text
> o/r 0x2101
> i
```

Obtendrás un prompt `Router(boot)>`. Desde ahí, `copy tftp flash` funciona igual sobre **cualquier**
interfaz IP que le des — la diferencia entre los tres métodos siguientes es sólo qué interfaz
configuras y por dónde llega el TFTP.

**Con transceptor AUI (Ethernet)** — la vía más simple si lo tienes:

```text
Router(boot)> enable
Router(boot)# configure terminal
Router(boot)(config)# interface Ethernet0
Router(boot)(config-if)#  ip address 192.168.104.41 255.255.255.0
Router(boot)(config-if)#  no shutdown
Router(boot)(config-if)# end
Router(boot)# ping 192.168.104.10
Router(boot)# copy tftp flash
```

Responde a las preguntas: dirección del servidor TFTP (`192.168.104.10`), nombre del fichero
(`c2500-i-l.123-26.bin`) y confirma **borrar la flash** cuando lo pida.

**Sin transceptor AUI** — el `Serial0` es una interfaz IP como cualquier otra: conéctalo a un
router que sí llegue a la LAN (por ejemplo un Cisco 2620) para que haga de pasarela, y repite el
mismo `copy tftp flash` pero configurando `Serial0` en vez de `Ethernet0`. Es tan fiable como la
vía Ethernet, sólo que necesita un cable V.35 y un router libre. Procedimiento completo, con
direccionamiento, cables y la ruta de vuelta en el servidor TFTP, en el plan de contingencia de
cada equipo:
[`RT-C2503-01`](../equipos/RT-C2503-01/plan-contingencia.md#b2--tftp-por-enlace-serie-usando-otro-router-como-pasarela-) ·
[`RT-C2503-02`](../equipos/RT-C2503-02/plan-contingencia.md#b2--tftp-por-enlace-serie-usando-otro-router-como-pasarela-).

**Sin ningún router libre** — último recurso por `copy console flash` (XMODEM), muy lento y frágil;
también documentado en el plan de contingencia de cada 2503.

Cuando termines por cualquier vía, restaura el arranque normal y reinicia:

```text
Router(boot)# configure terminal
Router(boot)(config)# config-register 0x2102
Router(boot)(config)# end
Router(boot)# write memory
Router(boot)# reload
```

---

### Cisco 2620 — ROMmon `tftpdnld` / `xmodem`

1. Consola a `9600 8N1`. Entra en ROMmon con `Break` durante el arranque → `rommon 1 >`.
2. **Opción A — TFTP (rápida, recomendada):**

```text
rommon 1 > IP_ADDRESS=192.168.104.43
rommon 2 > IP_SUBNET_MASK=255.255.255.0
rommon 3 > DEFAULT_GATEWAY=192.168.104.1
rommon 4 > TFTP_SERVER=192.168.104.10
rommon 5 > TFTP_FILE=c2600-i-mz.123-26.bin
rommon 6 > set
rommon 7 > tftpdnld
```

Confirma con `y` cuando avise de que **borrará la flash**. Usa el cable en `FastEthernet0/0`.

3. **Opción B — XMODEM por consola** (si no hay red):

```text
rommon 1 > xmodem -c c2600-i-mz.123-26.bin
```

Y envía el fichero por XMODEM desde el terminal. Para acelerar, antes puedes subir la velocidad:

```text
rommon 1 > confreg
```

Responde `y` a *"change console baud rate"* y elige `115200`; **reconecta el terminal a 115200**.
Al terminar, vuelve a `9600` y a `0x2102`.

4. Arranca y fija la imagen:

```text
rommon 8 > reset
Router# configure terminal
Router(config)# boot system flash:c2600-i-mz.123-26.bin
Router(config)# config-register 0x2102
Router(config)# end
Router# write memory
```

---

### 3Com 4500G / 4210 — BootROM

1. `Ctrl+B` durante el arranque para entrar al menú de BootROM.
2. Elige **«Download application file to flash»** (normalmente opción `1`) y luego el método:
   **TFTP**, **FTP** o **XMODEM**.
3. Con TFTP, el menú pide: IP del switch, máscara, gateway, IP del servidor y nombre del fichero
   (p. ej. `4500G-CMW520-R2202.bin`). Marca el fichero como **`main`** cuando lo pregunte.
4. Si la flash está llena, usa antes **«Delete file from flash»** (⚠️ sólo tras confirmar que
   tienes la imagen nueva lista para subir).
5. Reinicia (opción `0`). Una vez arrancado, verifica y fija la imagen de arranque:

```text
<Switch> dir flash:/
<Switch> display boot-loader
<Switch> boot-loader file flash:/4500G-CMW520-R2202.bin main
<Switch> display version
```

---

### Dell PowerConnect 7024 — doble imagen y Boot Menu

Este switch guarda **dos imágenes** (`image1` / `image2`): casi siempre basta con arrancar la buena.

**Caso 1 — el switch arranca:**

```text
console# show bootvar
console# copy tftp://192.168.104.10/PC7000v5.1.9.3.stk image2
console# boot system image2
console# reload
```

**Caso 2 — el switch no arranca:**

1. Consola a `9600 8N1`, pulsa `2` durante el arranque para entrar al **Boot Menu**.
2. Usa **«Activate Backup Image»** para arrancar con la imagen alternativa (lo más rápido).
3. Si ambas están corruptas, usa **«Load new operational code using XMODEM»**
   (⚠️ o la opción TFTP si tu *boot code* la ofrece) y envía el `.stk` desde el terminal.
4. `Reset the system` para reiniciar.

---

### Juniper EX2300 / SRX320 — snapshot, USB y *format install*

**Caso 1 — el equipo arranca (recuperar/actualizar software):**

```text
user@sw> request system storage cleanup
user@sw> show system storage
user@sw> request system software add /var/tmp/junos-arm-32-21.4R3-S4.tgz no-copy no-validate
user@sw> request system reboot
```

Tras comprobar que todo funciona, **crea el punto de restauración**:

```text
user@sw> request system snapshot
```

**Caso 2 — el equipo no arranca (instalación limpia desde USB):**

1. Formatea un USB en **FAT32** y copia la imagen `.tgz` a la raíz.
2. Consola a `9600 8N1`, inserta el USB, reinicia y pulsa **espacio** para llegar a `loader>`.
3. Lanza la instalación con formateo del disco (⚠️ **borra la configuración**):

```text
loader> install --format --external file:///junos-arm-32-21.4R3-S4.tgz
```

> ⚠️ La sintaxis exacta y el nombre de la imagen dependen del modelo y de la versión del cargador
> (`file:///` para el medio externo, opción `--external`, presencia de `--format`). **Consulta la
> KB de recuperación de Juniper para tu modelo** antes de ejecutarlo y anota aquí el comando que
> funcionó en tu equipo.

4. Al terminar, el equipo arranca de fábrica: pon contraseña de `root`, restaura la configuración
   desde el respaldo y haz `request system snapshot`.

**Restaurar configuración en Junos:**

```text
user@sw# load override /var/tmp/SW-EX2300-01_base.conf
user@sw# commit confirmed 5
user@sw# commit
```


[⬅️ Volver al índice](../README.md) · [📊 Comparativa](01-comparativa.md) · [📇 Fichas por equipo](../equipos/README.md) · [⚡ Chuleta de comandos](03-chuleta-comandos.md)
