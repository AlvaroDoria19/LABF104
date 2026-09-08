# 🚨 FW-SRX300-02 — Plan de contingencia

**Juniper SRX300**

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

> ⚠️ Falta la **versión de Junos**: ejecuta `show system information`. Sin ella no sabes qué `.tgz` descargar del portal de Juniper.

---

## 🔐 A) Contraseña perdida

**Método: modo *single-user* del cargador → `recovery`.** No pierde la configuración.

1. Consola a `9600 8N1` (RJ-45 o micro-USB).
2. Reinicia el equipo. Cuando aparezca
   `Hit [Enter] to boot immediately, or space bar for command prompt.`
   pulsa la **barra espaciadora**. (Si se te pasa, reinicia y repite.)
3. Arranca en modo single-user:

```text
loader> boot -s
```

4. Cuando pregunte
   `Enter full pathname of shell or 'recovery' for root password recovery:`
   escribe:

```text
recovery
```

5. Fija la contraseña de `root`:

```text
root> configure
root# set system root-authentication plain-text-password
New password: <nueva-clave>
Retype new password: <nueva-clave>
root# commit
root# exit
root> request system reboot
```

6. Recrea el usuario nominal si también se perdió:

```text
root# set system login user lab-admin class super-user authentication plain-text-password
root# commit
```

7. Anota las nuevas credenciales en [Acceso](README.md#-acceso) y en el [README](../README.md).

> ⚠️ **Si el equipo está en Chassis Cluster**, hazlo en el nodo correspondiente y verifica el
> estado del clúster al terminar con `show chassis cluster status`.

> [!TIP]
> Para dejarlo de fábrica: `request system zeroize`. El SRX volverá a su configuración por defecto
> (`ge-0/0/0` como *untrust* cliente DHCP, `ge-0/0/1…7` en VLAN *trust* con `192.168.1.1/24` y
> servidor DHCP activo). Recuerda que `root` **debe** tener contraseña antes del primer `commit`.

---

## 📀 B) Sistema operativo borrado o corrupto

**Medida preventiva imprescindible — el *snapshot*:**

```text
request system snapshot slice alternate
show system snapshot media internal
```

**Caso 1 — el equipo arranca (reinstalar o actualizar):**

```text
show system storage
request system storage cleanup
request system software add /var/tmp/junos-srxsme-<version>.tgz no-copy no-validate
request system reboot
```

Al verificar que todo funciona:

```text
request system snapshot
```

**Caso 2 — el equipo no arranca (instalación limpia desde USB):**

1. Formatea un USB de **8–16 GB en FAT32** y copia el `.tgz` a la **raíz**.
2. Consola a `9600 8N1`, inserta el USB, reinicia y pulsa **espacio** para llegar a `loader>`.
3. Lanza la instalación con formateo (⚠️ **borra la configuración**):

```text
loader> install --format --external file:///junos-srxsme-<version>.tgz
```

> ⚠️ **La sintaxis exacta depende del modelo y del cargador.** Consulta la KB de recuperación de
> Juniper para la serie SRX300 antes de ejecutarlo y **anota aquí el comando que funcionó**:
>
> `Comando verificado en este equipo: ______________________________________`

4. Al terminar, pon contraseña de `root`, restaura la configuración y crea el snapshot:

```text
configure
load override /var/tmp/FW-SRX300-02_base.conf
commit confirmed 5
commit
exit
request system snapshot
```

**Actualización opcional del BIOS del Routing Engine** (tienes 3.1, hay 3.6 disponible):

```text
show system firmware
request system firmware upgrade re bios
```

> ⚠️ No es urgente. Si lo haces: configuración respaldada primero, y **no interrumpas la
> alimentación** durante el proceso.

---

## 💾 Respaldo de configuración

**Configuración en formato `set` (el más práctico para el repositorio):**

```text
show configuration | display set | no-more
```

Copia la salida a `backups/configs/FW-SRX300-02_AAAA-MM-DD.conf`.

**Traer el fichero a la PC del laboratorio** con `scp` desde Windows:

```text
scp lab-admin@192.168.104.52:/config/juniper.conf.gz C:\LabF104\imagenes\FW-SRX300-02_juniper.conf.gz
```

**A un USB, desde el propio equipo:**

```text
start shell user root
```

```text
ls /dev/da*
mkdir -p /var/tmp/usb
mount_msdosfs /dev/da0s1 /var/tmp/usb
cp /config/juniper.conf.gz /var/tmp/usb/FW-SRX300-02_juniper.conf.gz
ls -lh /var/tmp/usb
umount /var/tmp/usb
exit
```

**Restaurar:**

```text
configure
load override /var/tmp/FW-SRX300-02_base.conf
commit confirmed 5
commit
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

````markdown
### Intervención — FW-SRX300-02 — AAAA-MM-DD

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
