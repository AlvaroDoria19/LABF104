# ⚡ SW-C2950-01 — Chuleta de comandos

**Cisco Catalyst WS-C2950-24**

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
 hostname F104-SW-2950-01
 no ip domain-lookup
 interface Vlan1
  ip address 192.168.104.16 255.255.255.0
  no shutdown
  exit
 ip default-gateway 192.168.104.1
 line console 0
  logging synchronous
 end
write memory
```

### Diagnóstico

```text
show version
show running-config
show interfaces status
show interfaces FastEthernet0/1
show vlan brief
show spanning-tree vlan 10
show mac address-table
show etherchannel summary
show cdp neighbors detail
dir flash:
show logging
```

### VLAN y puertos de acceso

```text
configure terminal
 vlan 10
  name PRACTICA-A
  exit
 interface range FastEthernet0/1 - 8
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
 switchport trunk allowed vlan 1,10,20,104
 switchport trunk native vlan 1
```

### RSTP / MSTP

```text
configure terminal
 spanning-tree mode rapid-pvst
 spanning-tree vlan 10 priority 4096
 spanning-tree portfast bpduguard default
 end
```

### EtherChannel (LACP)

```text
interface range FastEthernet0/23 - 24
 channel-group 1 mode active
 exit
interface Port-channel1
 switchport mode trunk
```

### Port security

```text
interface FastEthernet0/1
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

### SPAN (captura para Wireshark)

```text
monitor session 1 source interface FastEthernet0/1
monitor session 1 destination interface FastEthernet0/24
```

Verificar: `show monitor session 1`

### 802.1X

```text
configure terminal
 aaa new-model
 radius-server host 192.168.104.10 key <clave>
 aaa authentication dot1x default group radius
 dot1x system-auth-control
 interface FastEthernet0/1
  dot1x port-control auto
 end
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
