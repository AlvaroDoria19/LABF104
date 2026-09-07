# 🚨 RT-C2503-01 — Plan de contingencia

**Cisco 2503 (serie 2500)**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `c2500-j-l_112-17.bin` (7 992 252 bytes)

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

**Método: registro de configuración `0x2142` desde el ROM Monitor del 2500.**

1. Consola a `9600 8N1`.
2. Apaga y enciende, y **envía `Break` en los primeros 60 segundos**.
3. Obtendrás el monitor del 2500, con prompt `>`:

```text
> o/r 0x2142
> i
```

4. Arranca sin configuración. Rechaza el asistente (`no`) y carga la config guardada:

```text
Router> enable
Router# copy startup-config running-config
```

> [!CAUTION]
> **Nunca `copy running-config startup-config` en este punto** — borrarías la configuración.

5. Cambia las contraseñas y restaura el registro:

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

---

## 📀 B) Sistema operativo borrado o corrupto

Este router ejecuta el IOS **desde la flash** (*run-from-flash*): si la imagen se corrompe, no
arranca. Su salvación es la **imagen RXBOOT que vive en la ROM** (`IGS-BOOT-R 11.0(10c)`), que
`show version` confirma que está presente.

> [!CAUTION]
> Con **396 KB libres** en flash **no cabe una segunda imagen**. Cualquier cambio de IOS obliga a
> borrar la actual primero. No lo intentes sin la imagen respaldada y la consola conectada.

**Rescate por RXBOOT + TFTP:**

1. Consola a `9600 8N1`. `Break` durante el arranque → prompt `>`.
2. Arranca desde la ROM:

```text
> o/r 0x2101
> i
```

3. Obtendrás `Router(boot)>`. Configura la LAN y descarga la imagen:

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

Responde: servidor `192.168.104.10`, fichero `c2500-j-l_112-17.bin`, y confirma **borrar la flash**.

4. Restaura el arranque normal:

```text
Router(boot)# configure terminal
Router(boot)(config)# config-register 0x2102
Router(boot)(config)# end
Router(boot)# write memory
Router(boot)# reload
```

> ⚠️ **El transceptor AUI→RJ-45 es imprescindible** para este procedimiento: sin LAN no hay TFTP.
> Si no lo tienes, la alternativa es sacar/meter la imagen a través del `Serial0` conectado a un
> Cisco 2620 que haga de pasarela hacia la LAN.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/RT-C2503-01_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema (necesita el transceptor AUI, o la ruta por `Serial0` vía 2620):

```text
show flash
copy flash ftp
```

Responde a los prompts: fichero `c2500-j-l_112-17.bin`, servidor `192.168.104.10`,
destino `RT-C2503-01_c2500-j-l_112-17.bin`.

Restaurar configuración:

```text
copy tftp://192.168.104.10/RT-C2503-01_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — RT-C2503-01 — AAAA-MM-DD

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
