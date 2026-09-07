# ⚡ SW-PC7024-02 — Chuleta de comandos

**Dell PowerConnect 7024**

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
configure
 hostname F104-SW-PC7024-02
 exit
copy running-config startup-config
```

### Diagnóstico

```text
show version
show system
show switch
show bootvar
show running-config
show interfaces status
show interfaces gigabitethernet 1/0/1
show mac address-table
show vlan
show ip route
show arp
show spanning-tree
show port-channel
show lldp remote-device all
show logging
show users
```

### VLAN, acceso y trunk

```text
configure
 vlan 10
  name PRACTICA-A
  exit
 interface Gi1/0/1
  switchport mode access
  switchport access vlan 10
  spanning-tree portfast
  exit
 interface Gi1/0/24
  switchport mode trunk
  switchport trunk allowed vlan add 10,20,104
  exit
 exit
copy running-config startup-config
```

### Gestión Out-of-Band (recomendado)

```text
configure
 interface out-of-band
  ip address 192.168.104.22 255.255.255.0 192.168.104.1
  exit
 exit
copy running-config startup-config
```

### Enrutamiento inter-VLAN

```text
configure
 ip routing
 interface vlan 10
  ip address 10.104.10.1 255.255.255.0
  exit
 interface vlan 20
  ip address 10.104.20.1 255.255.255.0
  exit
 ip route 0.0.0.0 0.0.0.0 192.168.104.1
```

### OSPF

```text
configure
 router ospf
  router-id 1.1.1.1
  network 10.104.10.0 0.0.0.255 area 0
  network 10.104.20.0 0.0.0.255 area 0
```

Verificar: `show ip ospf neighbor` · `show ip route ospf`

### VRRP (redundancia de gateway entre dos PowerConnect)

```text
configure
 interface vlan 10
  vrrp 1
  vrrp 1 ip 10.104.10.254
  vrrp 1 priority 200
  vrrp 1 mode
```

Verificar: `show vrrp`

### Agregación de enlaces (LACP)

```text
configure
 interface port-channel 1
  switchport mode trunk
  exit
 interface range Gi1/0/23-24
  channel-group 1 mode active
```

### Usuarios y SSH

```text
configure
 username admin password <clave> privilege 15
 enable password <clave>
 crypto key generate rsa
 ip ssh server
 line ssh
  exec-timeout 15
```

### Seguridad de capa 2

```text
configure
 ip dhcp snooping
 ip dhcp snooping vlan 10
 ip arp inspection vlan 10
 interface Gi1/0/24
  ip dhcp snooping trust
  ip arp inspection trust
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
