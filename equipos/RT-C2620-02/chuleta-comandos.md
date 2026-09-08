# ⚡ RT-C2620-02 — Chuleta de comandos

**Cisco 2620 (serie 2600)**

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
 hostname F104-RT-2620-01
 no ip domain-lookup
 line console 0
  logging synchronous
  exec-timeout 15 0
 end
write memory
```

### Diagnóstico

```text
show version
show diag
show ip interface brief
show interfaces
show controllers Serial 0/0
show ip route
show ip protocols
show processes cpu sorted
show flash:
show logging
```

### Interfaces

```text
configure terminal
 interface FastEthernet0/0
  ip address 192.168.104.44 255.255.255.0
  no shutdown
  exit
 interface Serial0/0
  ip address 172.16.104.2 255.255.255.252
  encapsulation ppp
  clock rate 2000000
  no shutdown
 end
```

> `clock rate` **sólo** en el extremo DCE. Compruébalo con `show controllers Serial 0/0`.

### Inter-VLAN (router-on-a-stick)

```text
interface FastEthernet0/0
 no ip address
 no shutdown
 exit
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.104.10.1 255.255.255.0
 exit
interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.104.20.1 255.255.255.0
```

### OSPF y ruta por defecto

```text
router ospf 1
 network 10.104.0.0 0.0.255.255 area 0
 network 172.16.104.0 0.0.0.3 area 0
 exit
ip route 0.0.0.0 0.0.0.0 172.16.104.1
```

### NAT/PAT y DHCP

```text
access-list 1 permit 10.104.0.0 0.0.255.255
ip nat inside source list 1 interface FastEthernet0/0 overload
interface FastEthernet0/0
 ip nat outside
 exit
interface FastEthernet0/1
 ip nat inside
 exit
ip dhcp excluded-address 10.104.10.1 10.104.10.10
ip dhcp pool LAB
 network 10.104.10.0 255.255.255.0
 default-router 10.104.10.1
```

Verificar: `show ip nat translations` · `show ip nat statistics` · `show ip dhcp binding`

### Frame Relay

```text
interface Serial0/0
 encapsulation frame-relay
 frame-relay lmi-type cisco
 exit
interface Serial0/0.102 point-to-point
 ip address 172.16.104.5 255.255.255.252
 frame-relay interface-dlci 102
```

Verificar: `show frame-relay pvc` · `show frame-relay map` · `show frame-relay lmi`

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
