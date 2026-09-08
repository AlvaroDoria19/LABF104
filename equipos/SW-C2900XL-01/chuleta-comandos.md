# ⚡ SW-C2900XL-01 — Chuleta de comandos

**Cisco Catalyst WS-C2924-XL-EN**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> **Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo
> Credenciales en la [ficha del equipo](README.md#-acceso).
> Para comparar la sintaxis con las otras familias de CLI del laboratorio, ve a la
> [chuleta general](../../docs/03-chuleta-comandos.md).

---

### Básico

```text
enable
configure terminal
 hostname F104-SW-2924XL-01
 ip default-gateway 192.168.104.1
 interface VLAN1
  ip address 192.168.104.15 255.255.255.0
  exit
 end
write memory
```

### Diagnóstico

```text
show version
show running-config
show interfaces status
show vlan
show vtp status
show spanning-tree
show mac-address-table
show cdp neighbors detail
dir flash:
show logging
```

> ⚠️ En este IOS antiguo algunos comandos cambian: es `show mac-address-table` (con guiones) y
> `show vlan`, no `show vlan brief`. Usa `?` si algo no existe.

### VLAN y puertos de acceso

```text
configure terminal
 vlan database
  vlan 10 name PRACTICA-A
  exit
 interface FastEthernet0/1
  switchport mode access
  switchport access vlan 10
  spanning-tree portfast
 end
write memory
```

### Trunk

```text
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 1,10,20,104
```

### VTP

```text
configure terminal
 vtp domain F104
 vtp mode server
 vtp password <clave>
 end
```

### Port security básica

```text
interface FastEthernet0/1
 port security max-mac-count 2
```

### Monitorización de puerto (SPAN)

```text
interface FastEthernet0/24
 port monitor FastEthernet0/1
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
