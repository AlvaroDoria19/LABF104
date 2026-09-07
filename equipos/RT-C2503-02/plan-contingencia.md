# 🚨 RT-C2503-02 — Plan de contingencia

**Cisco 2503 (serie 2500)**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> [!IMPORTANT]
> **Antes de empezar:** avisa de que vas a reiniciar el equipo, ten el acceso de consola o de red
> preparado, y confirma que **tienes la imagen de sistema** localizada (ver más abajo).
> Las credenciales actuales están en la [ficha del equipo](README.md#-acceso).

---

## 📦 Dónde conseguir la imagen de este equipo

**Fichero necesario:** `igs-inr-l.111-17`

| Fuente | Ubicación | ¿Verificado? |
|---|---|:--:|
| ☁️ **Google Drive del laboratorio** | <!-- PEGAR AQUÍ EL ENLACE DE LA CARPETA --> `` | ☐ |
| 💻 **PC del laboratorio F104** | Equipo: `<nombre-del-PC>` · Ruta: `C:\LabF104\imagenes\` | ☐ |
| 🗂️ Repositorio Git | `backups/imagenes/` | ☐ |

> 💡 **La PC del laboratorio tiene todas las imágenes de sistema ya descargadas.** Es la primera
> fuente a la que ir si un equipo se queda sin OS. El Google Drive es la copia externa por si esa
> PC falla o se reinstala.

> ⚠️ Fíjate en que **este fichero no lleva extensión `.bin`**. Cópialo con el nombre exacto o el arranque fallará.

---

## 🔐 A) Contraseña perdida

**Método: registro de configuración `0x2142` desde el ROM Monitor del 2500.**

1. Consola a `9600 8N1`.
2. Apaga y enciende, y **envía `Break` en los primeros 60 segundos**.
3. En el prompt `>` del monitor:

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
> **Nunca `copy running-config startup-config` aquí** — borrarías la configuración.

5. Cambia contraseñas y restaura el registro:

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

Ejecuta el IOS **desde la flash** (*run-from-flash*). Su red de seguridad es la **imagen RXBOOT
de la ROM** (`IGS-BOOT-R 11.0(10c)`), confirmada en `show version`.

**Rescate por RXBOOT + TFTP:**

1. Consola a `9600 8N1`. `Break` durante el arranque → prompt `>`.
2. Arranca desde la ROM:

```text
> o/r 0x2101
> i
```

3. En `Router(boot)>`, configura la LAN y descarga:

```text
Router(boot)> enable
Router(boot)# configure terminal
Router(boot)(config)# interface Ethernet0
Router(boot)(config-if)#  ip address 192.168.104.42 255.255.255.0
Router(boot)(config-if)#  no shutdown
Router(boot)(config-if)# end
Router(boot)# ping 192.168.104.10
Router(boot)# copy tftp flash
```

Responde: servidor `192.168.104.10`, fichero `igs-inr-l.111-17`, y confirma **borrar la flash**.

4. Restaura el arranque normal:

```text
Router(boot)# configure terminal
Router(boot)(config)# config-register 0x2102
Router(boot)(config)# end
Router(boot)# write memory
Router(boot)# reload
```

> ⚠️ **Necesita el transceptor AUI→RJ-45.** Sin LAN no hay TFTP. Alternativa: enlazar `Serial0`
> con un Cisco 2620 que haga de pasarela hacia la LAN.

> 💡 **Nota de mejora (opcional, no urgente).** Con sus 16 MB de DRAM este router sí podría ejecutar
> una imagen de IOS 12.0 IP (`c2500-i-l.120-xx.bin`, ~7 MB, cabe en los 8 MB de flash), lo que le
> daría NAT y servidor DHCP. Es una operación con riesgo (hay que borrar la flash primero y sólo
> cabe una imagen), así que **no la hagas sin la imagen actual respaldada y verificada**.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/RT-C2503-02_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema (necesita transceptor AUI, o ruta por `Serial0` vía 2620):

```text
show flash
copy flash ftp
```

Responde: fichero `igs-inr-l.111-17`, servidor `192.168.104.10`,
destino `RT-C2503-02_igs-inr-l.111-17`.

Restaurar configuración:

```text
copy tftp://192.168.104.10/RT-C2503-02_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) o en la
[bitácora general](../../docs/04-bitacora.md) cada vez que intervengas:

````markdown
### Intervención — RT-C2503-02 — AAAA-MM-DD

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
