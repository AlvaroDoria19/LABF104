# 🚨 SW-PC7024-03 — Plan de contingencia

**Dell PowerConnect 7024**

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

> ⚠️ Falta la versión de firmware y el nombre del `.stk`: ejecuta **`show version`**.

---

## 🔐 A) Contraseña perdida

**Método: Boot Menu → «Password Recovery Procedure».** Conserva la configuración.

1. Consola a `9600 8N1`.
2. Reinicia. Cuando aparezca
   `Select an option. If no selection in 2 seconds then operational code will start.`
   pulsa **`2`** para entrar en el **Boot Menu**.
3. Elige **«Password Recovery Procedure»** (⚠️ suele ser la opción **`12`**, pero el número depende
   de la versión de *boot code* — **lee el menú real**).
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

6. Reinicia y comprueba que las nuevas credenciales funcionan:

```text
console# reload
```

7. Anota las nuevas credenciales en [Acceso](README.md#-acceso) y en el [README](../README.md).

> 💡 Si necesitas dejarlo **de fábrica**, el mismo Boot Menu ofrece
> «Restore Configuration to Factory Defaults» — ⚠️ borra la configuración completa.

---

## 📀 B) Sistema operativo borrado o corrupto

Este switch es el **mejor protegido del laboratorio** gracias a su **doble imagen**: casi siempre
basta con arrancar la copia buena.

**Caso 1 — el switch arranca:**

```text
show bootvar
show version
```

Sube una imagen buena a la ranura libre y arranca desde ella:

```text
copy tftp://192.168.104.10/PC7000vX.X.X.X.stk image2
boot system image2
reload
```

> [!TIP]
> **Regla de oro con este equipo: nunca actualices `image1` e `image2` a la vez.** Deja siempre una
> con una versión verificada y arrancable. Es tu red de seguridad y no cuesta nada mantenerla.

**Caso 2 — el switch no arranca:**

1. Consola a `9600 8N1`, pulsa **`2`** durante el arranque → **Boot Menu**.
2. Usa **«Activate Backup Image»** para arrancar con la imagen alternativa. Esta es la vía rápida y
   resuelve el 95 % de los casos.
3. Si **ambas** imágenes están corruptas, usa
   **«Load new operational code using XMODEM»** (o la opción TFTP si tu *boot code* la ofrece) y
   envía el fichero `.stk` desde el terminal.
4. **«Reset the system»** para reiniciar.
5. Verifica al arrancar:

```text
show version
show bootvar
```

> ⚠️ **Consigue el `.stk` antes de necesitarlo.** Si no se puede extraer del switch (comprueba con
> `copy ?`), descárgalo del soporte de Dell para el PowerConnect 7024 y guárdalo en el Google Drive
> y en la PC del laboratorio.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/SW-PC7024-03_AAAA-MM-DD.cfg
```

También por FTP:

```text
copy running-config ftp://labftp:<clave>@192.168.104.10/imagenes/SW-PC7024-03_AAAA-MM-DD.cfg
```

Intentar extraer la imagen (comprueba primero si tu firmware lo permite):

```text
copy ?
copy image1 ftp://labftp:<clave>@192.168.104.10/imagenes/SW-PC7024-03_PC7024.stk
```

Restaurar configuración:

```text
copy tftp://192.168.104.10/SW-PC7024-03_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — SW-PC7024-03 — AAAA-MM-DD

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
