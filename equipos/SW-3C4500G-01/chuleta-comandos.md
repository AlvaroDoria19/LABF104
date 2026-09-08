# ⚡ SW-3C4500G-01 — Chuleta de comandos

**3Com Switch 4500G 24-Port**

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
 sysname F104-SW-4500G-01
 quit
save
```

> **`save` es obligatorio.** Sin él, todo se pierde al reiniciar.

### Diagnóstico

```text
display version
display device
display device manuinfo
display current-configuration
display saved-configuration
display interface brief
display vlan all
display mac-address
display arp
display ip routing-table
display stp brief
display link-aggregation summary
display lldp neighbor-information
display transceiver interface
display cpu-usage
display memory
display logbuffer
```

### VLAN, acceso y trunk

```text
system-view
 vlan 10
  name PRACTICA-A
  quit
 interface GigabitEthernet 1/0/1
  port link-type access
  port access vlan 10
  quit
 interface GigabitEthernet 1/0/24
  port link-type trunk
  port trunk permit vlan 1 10 20 104
  port trunk pvid vlan 1
  quit
 quit
save
```

### Interfaz de gestión y ruta por defecto

```text
system-view
 interface Vlan-interface 104
  ip address 192.168.104.11 255.255.255.0
  quit
 ip route-static 0.0.0.0 0.0.0.0 192.168.104.1
 quit
save
```

### Enrutamiento inter-VLAN y OSPF

```text
system-view
 interface Vlan-interface 10
  ip address 10.104.10.1 255.255.255.0
  quit
 interface Vlan-interface 20
  ip address 10.104.20.1 255.255.255.0
  quit
 ospf 1
  area 0
   network 10.104.10.0 0.0.0.255
   network 10.104.20.0 0.0.0.255
```

Verificar: `display ospf peer` · `display ip routing-table protocol ospf`

### Agregación de enlaces (LACP)

```text
system-view
 interface Bridge-Aggregation 1
  quit
 interface GigabitEthernet 1/0/23
  port link-aggregation group 1
  quit
 interface GigabitEthernet 1/0/24
  port link-aggregation group 1
```

### MSTP

```text
system-view
 stp mode mstp
 stp enable
 stp priority 4096
 interface GigabitEthernet 1/0/1
  stp edged-port enable
```

### Usuarios y SSH

```text
system-view
 local-user admin
  password simple <clave>
  service-type telnet ssh terminal
  authorization-attribute level 3
  quit
 super password level 3 simple <clave>
 user-interface vty 0 4
  authentication-mode scheme
  protocol inbound all
  idle-timeout 15 0
  quit
 public-key local create rsa
 ssh server enable
 quit
save
```

### VRRP (redundancia de gateway con el otro 4500G)

```text
system-view
 interface Vlan-interface 10
  vrrp vrid 1 virtual-ip 10.104.10.254
  vrrp vrid 1 priority 120
```

Verificar: `display vrrp verbose`

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
