# 🚨 SW-3C4500G-01 — Plan de contingencia

**3Com Switch 4500G 24-Port**

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

> ⚠️ El nombre del fichero `.bin` no consta en la captura de datos. Ejecuta `dir flash:/` y anótalo aquí — sin ese dato el rescate se complica.

---

## 🔐 A) Contraseña perdida

**Método: menú BootROM → «Skip Current System Configuration».**

1. Consola a `9600 8N1`.
2. Reinicia el switch y, cuando aparezca `Press Ctrl-B to enter Boot Menu...`, pulsa **`Ctrl+B`**
   en los primeros ~5 segundos.
3. Si pide contraseña de BootROM, introduce la anotada en [Acceso](README.md#-acceso).

> [!CAUTION]
> **Si la contraseña de BootROM también se ha perdido, el switch no es recuperable por consola.**
> Requeriría servicio técnico o programación JTAG. Mantén esa contraseña documentada.

4. Elige la opción **«Skip Current System Configuration»** (normalmente la **`7`** en Comware v5;
   ⚠️ el número cambia según la versión de BootWare — **lee el menú real**).
5. Selecciona `0` (Reboot). El switch arranca **sin aplicar** `startup.cfg`, con acceso libre.
6. **Primero lee la configuración guardada**, antes de tocar nada:

```text
<Switch> display saved-configuration
```

> [!WARNING]
> Al arrancar con «skip configuration», la configuración en ejecución está **vacía**. Si haces
> `save` sin más, **sobrescribes `startup.cfg` y pierdes toda la configuración del switch.**

7. Cambia las contraseñas y guarda:

```text
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

8. Reinicia y **vuelve a aplicar la configuración desde tu respaldo TFTP/FTP** si el paso 7
   sobrescribió el `startup.cfg`.

**Alternativa más segura:** no hagas `save`. Cambia la contraseña, guarda, reinicia y restaura la
configuración completa desde el respaldo del repositorio.

---

## 📀 B) Sistema operativo borrado o corrupto

Este switch tiene **16 MB de flash** con margen suficiente, así que la primera medida es
preventiva:

> [!TIP]
> **Guarda una segunda imagen en la propia flash.** Si la principal se corrompe, el rescate es
> inmediato desde el menú BootROM sin necesidad de servidor:
> ```text
> dir flash:/
> display boot-loader
> ```
> Si hay espacio, sube una copia por FTP y déjala como imagen de respaldo.

**Rescate desde el menú BootROM:**

1. `Ctrl+B` durante el arranque para entrar al menú.
2. Elige **«Download application file to flash»** (normalmente la opción `1`) y luego el método:
   **TFTP**, **FTP** o **XMODEM**.
3. Con TFTP el menú pide: IP del switch (`192.168.104.11`), máscara (`255.255.255.0`),
   gateway (`192.168.104.1`), IP del servidor (`192.168.104.10`) y nombre del fichero.
4. Cuando lo pregunte, marca el fichero como **`main`** (imagen principal de arranque).
5. Si la flash está llena, usa antes **«Delete file from flash»** — ⚠️ **sólo** después de
   confirmar que tienes la imagen nueva lista para subir.
6. Reinicia (opción `0`) y verifica:

```text
<Switch> dir flash:/
<Switch> display boot-loader
<Switch> display version
```

7. Si hiciera falta cambiar la imagen de arranque desde la CLI:

```text
<Switch> boot-loader file flash:/<imagen>.bin main
```

**Reset de fábrica** (⚠️ borra toda la configuración):

```text
<Switch> reset saved-configuration
<Switch> reboot
```

---

## 💾 Respaldo de configuración

```text
display current-configuration
tftp 192.168.104.10 put flash:/startup.cfg SW-3C4500G-01_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema por FTP — ⚠️ **`binary` es obligatorio** o llegará corrupta:

```text
dir flash:/
ftp 192.168.104.10
```

Dentro del cliente FTP del switch:

```text
binary
cd imagenes
put flash:/<imagen>.bin SW-3C4500G-01_<imagen>.bin
bye
```

Restaurar configuración:

```text
tftp 192.168.104.10 get SW-3C4500G-01_base.cfg flash:/startup.cfg
reboot
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

````markdown
### Intervención — SW-3C4500G-01 — AAAA-MM-DD

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
