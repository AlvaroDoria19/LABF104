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

**Tienes tres vías. Usa la B.2 mientras no consigas el transceptor AUI** — es tan fiable como la
Ethernet y con el material que ya tienes en el laboratorio.

| Vía | Necesita | Velocidad | Cuándo usarla |
|---|---|:--:|---|
| **B.1 — TFTP por Ethernet** | Transceptor AUI→RJ-45 | Rápida (red) | Si consigues el transceptor |
| **B.2 — TFTP por enlace serie** ⭐ | Un router libre con puerto serie + cable V.35 | Rápida (red) | **Recomendada ahora**: no necesitas el transceptor |
| **B.3 — XMODEM por consola** | Sólo el cable de consola | Muy lenta (horas) | Último recurso, sin ningún router disponible |

### B.1 — TFTP por Ethernet (con transceptor AUI)

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

---

### B.2 — TFTP por enlace serie, usando otro router como pasarela ⭐

Sin el transceptor AUI, `Ethernet0` no sirve. Pero el `Serial0` del 2503 es una interfaz IP
normal: si lo conectas a un router que sí llega a la LAN (uno de los dos **Cisco 2620**), ese
router hace de pasarela y el `copy tftp flash` de RXBOOT funciona exactamente igual, sólo que por
el enlace serie en vez de por Ethernet.

```text
PC-1 (TFTP)                    RT-C2620-01                          RT-C2503-01
192.168.104.10 ── LAN ──  Fa0/0 192.168.104.43
                          Serial0/0 172.16.104.2/30 ══serie══ Serial0 172.16.104.1/30
```

**Cables.** Necesitas la pareja V.35 que une el DB-60 del 2503 con el Smart Serial del 2620:

| Extremo | Cable | Rol |
|---|---|---|
| 2503 (DB-60) | `CAB-V35FC` (V.35 hembra) | Normalmente **DCE** |
| RT-C2620-01 (Serial0/0, Smart Serial) | `CAB-SS-V35MT` (V.35 macho) | Normalmente **DTE** |

> ⚠️ **Confírmalo con la etiqueta del propio cable** (los conectores V.35 llevan `DCE`/`DTE`
> moldeados). No puedes usar `show controllers` en el 2503 para verificarlo porque está en
> RXBOOT — así que la etiqueta física es tu única fuente aquí. El `clock rate` va **sólo** en el
> extremo que sea DCE.

**Paso 1 — Configura el RT-C2620-01** (arranca con su IOS normal, no hace falta tocarlo):

```text
enable
configure terminal
 interface FastEthernet0/0
  ip address 192.168.104.43 255.255.255.0
  no shutdown
  exit
 interface Serial0/0
  ip address 172.16.104.2 255.255.255.252
  clock rate 2000000
  no shutdown
 end
write memory
```

> El `clock rate` sólo hace falta si **este** extremo resultó ser el DCE. Si el DCE es el del 2503,
> quítalo de aquí (RXBOOT no necesita ponerlo del otro lado; ver el aviso al final del paso 3).

**Paso 2 — Añade la ruta de vuelta en la PC-1** (el TFTP de SolarWinds corre en Windows). Sin esto,
la PC-1 no sabe devolver los paquetes a la red temporal del enlace serie. Abre PowerShell **como
Administrador**:

```powershell
route -p add 172.16.104.0 mask 255.255.255.252 192.168.104.43
```

Verifica que llega:

```text
RT-C2620-01# ping 192.168.104.10
```

**Paso 3 — En el RT-C2503-01, entra a RXBOOT y configura el `Serial0`** en vez de `Ethernet0`:

```text
> o/r 0x2101
> i
```

```text
Router(boot)> enable
Router(boot)# configure terminal
Router(boot)(config)# interface Serial0
Router(boot)(config-if)#  ip address 172.16.104.1 255.255.255.252
Router(boot)(config-if)#  no shutdown
Router(boot)(config-if)# exit
Router(boot)(config)# ip route 0.0.0.0 0.0.0.0 172.16.104.2
Router(boot)(config)# end
Router(boot)# ping 192.168.104.10
Router(boot)# copy tftp flash
```

Responde: servidor `192.168.104.10`, fichero `c2500-j-l_112-17.bin`, y confirma **borrar la flash**.

> ⚠️ **Si `Router(boot)(config)# ip route ...` da error de sintaxis**, prueba con
> `ip default-gateway 172.16.104.2` en su lugar — según la versión exacta de RXBOOT, uno de los
> dos está disponible. Y si el `Serial0` no levanta a `up/up`, es casi siempre que falta el
> `clock rate` en el extremo DCE: revisa la etiqueta del cable y ponlo en el router que corresponda.

**Paso 4 — Restaura el arranque normal:**

```text
Router(boot)# configure terminal
Router(boot)(config)# config-register 0x2102
Router(boot)(config)# end
Router(boot)# write memory
Router(boot)# reload
```

**Paso 5 — Limpieza.** Cuando el RT-C2503-01 vuelva a arrancar con su IOS completo, decide:

- **Si quieres dejar el enlace serie montado** (te sirve además como banco de pruebas de WAN con
  el RT-C2620-01), no toques nada más.
- **Si el `Serial0` del RT-C2620-01 lo necesitas para otra práctica**, quita la IP temporal y la
  ruta añadida:

```text
RT-C2620-01# configure terminal
RT-C2620-01(config)# interface Serial0/0
RT-C2620-01(config-if)#  no ip address
RT-C2620-01(config-if)#  shutdown
RT-C2620-01(config-if)# end
RT-C2620-01# write memory
```

Y en la PC-1, quita la ruta:

```powershell
route delete 172.16.104.0
```

---

### B.3 — XMODEM por consola (último recurso, sin ningún router libre)

> [!WARNING]
> Método documentado por Cisco para esta familia de routers (`copy console flash` desde el
> **monitor de ROM real**, no desde RXBOOT), pero es **extremadamente lento** — a `9600` baudios
> una imagen de este tamaño puede tardar **varias horas** — y **cualquier ruido en la línea
> corrompe la transferencia** sin posibilidad de reanudarla. Úsalo sólo si no tienes forma de
> montar la vía B.2 (por ejemplo, si los dos Cisco 2620 están ocupados en otra práctica).

1. Consola a `9600 8N1`. Reinicia el router y envía **`Break` de inmediato**, antes de que cargue
   RXBOOT — necesitas caer en el **monitor de ROM real** (prompt `>` más primitivo, distinto del
   `Router(boot)>` de RXBOOT; en la práctica es el mismo prompt `>` pero **sin** haber hecho
   `o/r 0x2101` todavía).
2. En ese prompt:

```text
> copy console flash
```

3. El router queda a la espera de recibir el fichero por el puerto de consola. Cambia tu emulador
   de terminal a modo **XMODEM** y envía `c2500-j-l_112-17.bin`:
   - **Tera Term** (recomendado en Windows 11): *File → Transfer → XMODEM → Send...*
   - **minicom** (Linux): `Ctrl+A` luego `S` → elige `xmodem`
   - PuTTY **no** soporta XMODEM nativo — usa Tera Term en su lugar.
4. No toques el cable ni el terminal hasta que termine. Al acabar, verifica y reinicia:

```text
> i
```

> ⚠️ **Confirma el prompt y el comando exactos en tu equipo antes de depender de este método.**
> Algunas revisiones de ROM de este monitor difieren en la sintaxis; si `copy console flash` no
> existe en el tuyo, es señal de que tu ROM sólo soporta el camino RXBOOT+TFTP (B.1/B.2) y este
> método no está disponible — motivo de más para dejar montada la vía B.2.

---

## 💾 Respaldo de configuración

```text
show running-config
copy running-config tftp://192.168.104.10/RT-C2503-01_AAAA-MM-DD.cfg
```

Sacar la imagen de sistema:

- **Con transceptor AUI** → por Ethernet, con FTP:

```text
show flash
copy flash ftp
```

Responde a los prompts: fichero `c2500-j-l_112-17.bin`, servidor `192.168.104.10`,
destino `RT-C2503-01_c2500-j-l_112-17.bin`.

- **Sin transceptor AUI** → monta el mismo enlace serie de la [vía B.2](#b2--tftp-por-enlace-serie-usando-otro-router-como-pasarela-) y repite el `copy flash ftp` (o `copy flash tftp`) apuntando al servidor por esa ruta. Si dejaste el enlace montado tras un rescate, este paso no necesita reconfigurar nada.

Restaurar configuración:

```text
copy tftp://192.168.104.10/RT-C2503-01_base.cfg startup-config
reload
```

---

## 🧾 Checklist de intervención

Copia este bloque en las [notas del equipo](README.md#-notas-e-historial-de-este-equipo) cada vez
que intervengas:

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
- [ ] Respaldo de la configuración final subido al servidor TFTP (PC-1): sí / no
- [ ] Verificación final OK: sí / no
- Tiempo total: ... min · Realizado por: ...
````

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
