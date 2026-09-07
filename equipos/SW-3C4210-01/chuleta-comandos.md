# ⚡ SW-3C4210-01 — Chuleta de comandos

**3Com Switch 4210 26-Port**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> **Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo
> Credenciales en la [ficha del equipo](README.md#-acceso).
> Para comparar la sintaxis con las otras familias de CLI del laboratorio, ve a la
> [chuleta general](../../docs/03-chuleta-comandos.md).

---

### Básico y navegación

```text
system-view
 sysname F104-SW-4210-01
 quit
save
```

> **`save` es obligatorio.** Sin él, todo se pierde al reiniciar.

### Diagnóstico

```text
display version
display device
display current-configuration
display saved-configuration
display interface brief
display vlan all
display mac-address
display arp
display stp brief
display link-aggregation summary
display logbuffer
```

### VLAN, acceso y trunk

> ⚠️ En el 4210 los puertos de acceso son **`Ethernet 1/0/1`** (Fast Ethernet) y los uplinks
> suelen ser **`GigabitEthernet 1/0/25-26`**. Confírmalo con `display interface brief`.

```text
system-view
 vlan 10
  name PRACTICA-A
  quit
 interface Ethernet 1/0/1
  port link-type access
  port access vlan 10
  quit
 interface GigabitEthernet 1/0/25
  port link-type trunk
  port trunk permit vlan 1 10 20 104
  quit
 quit
save
```

### Interfaz de gestión y gateway

```text
system-view
 interface Vlan-interface 104
  ip address 192.168.104.13 255.255.255.0
  quit
 ip route-static 0.0.0.0 0.0.0.0 192.168.104.1
 quit
save
```

### MSTP

```text
system-view
 stp mode mstp
 stp enable
 interface Ethernet 1/0/1
  stp edged-port enable
```

### Agregación de enlaces

```text
system-view
 link-aggregation group 1 mode static
 interface GigabitEthernet 1/0/25
  port link-aggregation group 1
  quit
 interface GigabitEthernet 1/0/26
  port link-aggregation group 1
```

> ⚠️ La sintaxis de agregación cambia entre Comware v3 y v5. Usa `link-aggregation ?` para ver la
> forma exacta que acepta tu versión.

### Usuarios

```text
system-view
 local-user admin
  password simple <clave>
  service-type telnet terminal
  authorization-attribute level 3
  quit
 super password level 3 simple <clave>
 user-interface vty 0 4
  authentication-mode scheme
  quit
 quit
save
```

### 802.1X

```text
system-view
 radius scheme F104
  primary authentication 192.168.104.10
  key authentication <clave>
  quit
 dot1x
 interface Ethernet 1/0/1
  dot1x
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
