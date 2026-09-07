# 🚨 SW-EX2300-02 — Plan de contingencia

**Juniper EX2300-24T**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `junos-arm-32-18.1R3.3.tgz`

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

**Método: modo *single-user* del cargador → `recovery`.** No pierde la configuración.

1. Consola a `9600 8N1`.
2. Reinicia el switch. Cuando aparezca
   `Hit [Enter] to boot immediately, or space bar for command prompt.`
   pulsa la **barra espaciadora**. (Si se te pasa, reinicia y repite.)
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

6. Aprovecha para recrear el usuario nominal si también se perdió:

```text
root# set system login user lab-admin class super-user authentication plain-text-password
root# commit
```

7. Anota las nuevas credenciales en [Acceso](README.md#-acceso) y en el [README](../README.md).

> [!TIP]
> **La configuración no se pierde** con este procedimiento: `recovery` sólo permite editar y
> confirmar. Si necesitaras dejar el equipo de fábrica: `request system zeroize`
> (⚠️ borra configuración, licencias locales y logs).

---

## 📀 B) Sistema operativo borrado o corrupto

> [!CAUTION]
> **Antes de tocar el software, comprueba el espacio libre.** Es la causa nº 1 de fallos en el
> EX2300:
> ```text
> show system storage
> request system storage cleanup
> ```

**Medida preventiva imprescindible — el *snapshot*:**

```text
request system snapshot slice alternate
show system snapshot media internal
```

Esto guarda una copia arrancable del software actual en la partición alternativa. **Hazlo después
de cada cambio de versión exitoso.** Si el arranque principal falla, el switch puede arrancar de
la copia.

**Caso 1 — el equipo arranca (reinstalar o actualizar):**

```text
request system storage cleanup
show system storage
request system software add /var/tmp/junos-arm-32-18.1R3.3.tgz no-copy no-validate
request system reboot
```

Al terminar y verificar que todo funciona:

```text
request system snapshot
```

**Caso 2 — el equipo no arranca (instalación limpia desde USB):**

1. Formatea un USB de **8–16 GB en FAT32** y copia el `.tgz` a la **raíz**.
2. Consola a `9600 8N1`, inserta el USB, reinicia y pulsa **espacio** para llegar a `loader>`.
3. Lanza la instalación con formateo del disco (⚠️ **borra la configuración**):

```text
loader> install --format --external file:///junos-arm-32-18.1R3.3.tgz
```

> ⚠️ **La sintaxis exacta depende del modelo y de la versión del cargador** (presencia de
> `--format`, de `--external`, y la forma de la ruta `file:///`). Consulta la KB de recuperación de
> Juniper para el EX2300 antes de ejecutarlo, y **anota aquí el comando que funcionó en tu equipo**:
>
> `Comando verificado en este switch: ______________________________________`

4. Al terminar el switch arranca de fábrica. Pon contraseña de `root`, restaura la configuración y
   crea el snapshot:

```text
configure
load override /var/tmp/SW-EX2300-02_base.conf
commit confirmed 5
commit
exit
request system snapshot
```

---

## 💾 Respaldo de configuración

**Configuración en formato `set` (el más práctico para el repositorio):**

```text
show configuration | display set | no-more
```

Copia la salida a `backups/configs/SW-EX2300-02_AAAA-MM-DD.conf`.

**Traer el fichero de configuración a la PC del laboratorio** — lo más simple es tirar de él desde
Windows con `scp` (el cliente viene incluido y el switch ya es servidor SSH):

```text
scp lab-admin@192.168.104.32:/config/juniper.conf.gz C:\LabF104\imagenes\SW-EX2300-02_juniper.conf.gz
```

**A un USB, desde el propio switch:**

```text
start shell user root
```

```text
ls /dev/da*
mkdir -p /var/tmp/usb
mount_msdosfs /dev/da0s1 /var/tmp/usb
cp /config/juniper.conf.gz /var/tmp/usb/SW-EX2300-02_juniper.conf.gz
ls -lh /var/tmp/usb
umount /var/tmp/usb
exit
```

**Restaurar:**

```text
configure
load override /var/tmp/SW-EX2300-02_base.conf
commit confirmed 5
commit
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — SW-EX2300-02 — AAAA-MM-DD

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
