# ⚡ Chuleta de Comandos — Laboratorio F104

[⬅️ Volver al índice](../README.md)

> Comandos de uso diario agrupados por familia de CLI. Los `<valores>` entre ángulos se sustituyen.

---

## 📌 Índice

- [🗺️ Piedra Rosetta: el mismo comando en las 4 CLI](#️-piedra-rosetta-el-mismo-comando-en-las-4-cli)
- [🔵 Cisco IOS](#-cisco-ios--2900xl-2950-2503-2620) — 2900XL · 2950 · 2503 · 2620
- [🟢 3Com Comware](#-3com-comware--4500g-4210) — 4500G · 4210
- [🟡 Dell PowerConnect](#-dell-powerconnect--7024) — 7024
- [🟣 Juniper Junos](#-juniper-junos--ex2300-srx300) — EX2300 · SRX300
- [🟠 OpenWRT / LEDE](#-openwrt--lede--tl-mr3420) — TL-MR3420
- [🔥 Juniper SRX: firewall, NAT y VPN](#-juniper-srx-firewall-nat-y-vpn)
- [🧰 Comandos de emergencia](#-comandos-de-emergencia-los-10-imprescindibles)

---

## 🗺️ El mismo comando en las 4 CLI

| Acción | 🔵 Cisco IOS | 🟢 3Com Comware | 🟡 Dell PC 7024 | 🟣 Juniper Junos |
|---|---|---|---|---|
| Modo privilegiado | `enable` | `super 3` | `enable` | (por defecto) |
| Modo configuración | `configure terminal` | `system-view` | `configure` | `configure` / `edit` |
| Salir un nivel | `exit` | `quit` | `exit` | `up` / `exit` |
| Volver al inicio | `end` | `return` | `end` | `top` |
| Ver config activa | `show running-config` | `display current-configuration` | `show running-config` | `show configuration` |
| Ver config guardada | `show startup-config` | `display saved-configuration` | `show startup-config` | `show configuration` (commit) |
| **Guardar** | `write memory` | `save` | `copy run start` | `commit` |
| Descartar cambios | `reload` sin guardar | — | `reload` sin guardar | `rollback 0` |
| Versión de SO | `show version` | `display version` | `show version` | `show version` |
| Inventario HW | `show inventory` / `show diag` | `display device manuinfo` | `show system` | `show chassis hardware` |
| Estado de interfaces | `show ip interface brief` | `display interface brief` | `show interfaces status` | `show interfaces terse` |
| Tabla MAC | `show mac address-table` | `display mac-address` | `show mac address-table` | `show ethernet-switching table` |
| Tabla ARP | `show arp` | `display arp` | `show arp` | `show arp` |
| Tabla de rutas | `show ip route` | `display ip routing-table` | `show ip route` | `show route` |
| VLANs | `show vlan brief` | `display vlan all` | `show vlan` | `show vlans` |
| Spanning Tree | `show spanning-tree` | `display stp brief` | `show spanning-tree` | `show spanning-tree bridge` |
| Agregación de enlaces | `show etherchannel summary` | `display link-aggregation summary` | `show port-channel` | `show lacp interfaces` |
| Vecinos | `show cdp neighbors` | `display lldp neighbor-information` | `show lldp remote-device all` | `show lldp neighbors` |
| Log del sistema | `show logging` | `display logbuffer` | `show logging` | `show log messages` |
| Ping | `ping <ip>` | `ping <ip>` | `ping <ip>` | `ping <ip>` |
| Traceroute | `traceroute <ip>` | `tracert <ip>` | `traceroute <ip>` | `traceroute <ip>` |
| Reiniciar | `reload` | `reboot` | `reload` | `request system reboot` |
| Ayuda contextual | `?` · `co?` · `com <TAB>` | `?` | `?` | `?` · `<TAB>` |
| Filtrar salida | `\| include <txt>` | `\| include <txt>` | `\| include <txt>` | `\| match <txt>` |

> Los dos **TP-Link con OpenWRT** no entran en esta tabla: son Linux, con una lógica de
> configuración distinta (ficheros en `/etc/config` gestionados con `uci`). Su equivalencia está
> en [su propia sección](#-openwrt--lede--tl-mr3420).

---

## 🔵 Cisco IOS — 2900XL, 2950, 2503, 2620

### Básico y navegación

```text
enable                                  ! modo privilegiado
configure terminal                      ! modo configuración
hostname F104-SW-2950-01
no ip domain-lookup                     ! evita el retardo al escribir mal un comando
line console 0
 logging synchronous                    ! los mensajes no cortan lo que escribes
 exec-timeout 15 0
end
write memory                            ! guardar (= copy running-config startup-config)
```

### Diagnóstico

```text
show version                            ! versión de IOS, uptime, config-register, memoria
show running-config
show ip interface brief
show interfaces status                  ! sólo switches
show interfaces GigabitEthernet0/1      ! errores, CRC, colisiones, duplex
show mac address-table
show vlan brief
show spanning-tree vlan 10
show cdp neighbors detail
show logging
show processes cpu sorted
show flash:
```

### VLAN y trunking (2950 / 2900XL)

```text
configure terminal
 vlan 10
  name PRACTICA-A
 exit
 interface FastEthernet0/1
  switchport mode access
  switchport access vlan 10
  spanning-tree portfast
 exit
 interface GigabitEthernet0/1
  switchport mode trunk
  switchport trunk allowed vlan 1,10,20,104
  switchport trunk native vlan 1
 exit
 interface Vlan1
  ip address 192.168.104.16 255.255.255.0
 exit
 ip default-gateway 192.168.104.1
end
write memory
```

### EtherChannel (2950)

```text
interface range FastEthernet0/23 - 24
 channel-group 1 mode active            ! LACP  (usa 'desirable' para PAgP)
 exit
interface Port-channel1
 switchport mode trunk
```

### Seguridad de puertos (2950)

```text
interface FastEthernet0/1
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

### Enrutamiento (2503 / 2620)

```text
configure terminal
 interface FastEthernet0/0
  ip address 10.104.1.1 255.255.255.0
  no shutdown
 exit
 interface Serial0/0
  ip address 172.16.104.1 255.255.255.252
  encapsulation ppp                     ! o 'hdlc' / 'frame-relay'
  clock rate 64000                      ! SÓLO en el extremo DCE
  no shutdown
 exit
 router ospf 1
  network 10.104.1.0 0.0.0.255 area 0
  network 172.16.104.0 0.0.0.3 area 0
 exit
 ip route 0.0.0.0 0.0.0.0 172.16.104.2
end
write memory
```

### Inter-VLAN «router-on-a-stick» (2620)

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

### NAT y DHCP (2620)

```text
ip nat inside source list 1 interface FastEthernet0/0 overload
access-list 1 permit 10.104.0.0 0.0.255.255
interface FastEthernet0/0
 ip nat outside
interface FastEthernet0/1
 ip nat inside
!
ip dhcp excluded-address 10.104.10.1 10.104.10.10
ip dhcp pool LAB
 network 10.104.10.0 255.255.255.0
 default-router 10.104.10.1
 dns-server 8.8.8.8
```

Verificación:

```text
show ip nat translations
show ip nat statistics
show ip dhcp binding
```

### Serie y WAN (2503 / 2620)

```text
show controllers Serial 0               ! dice si el cable es DCE o DTE
show interfaces Serial 0
show frame-relay pvc
show frame-relay map
show ppp multilink
debug ppp authentication                ! recuerda: undebug all al terminar
```

### Respaldo y actualización

```text
copy running-config tftp:
copy tftp: flash:
copy flash: tftp:
show boot                               ! variable de arranque
configure terminal
 boot system flash:c2950-i6q4l2-mz.121-22.EA14.bin
 config-register 0x2102
end
write memory
```

### SSH (2950 con imagen k9 · 2620 con imagen k9)

```text
configure terminal
 hostname F104-RT-2620-01
 ip domain-name lab.f104
 crypto key generate rsa modulus 1024
 username admin privilege 15 secret <clave>
 line vty 0 4
  transport input ssh
  login local
 exit
 ip ssh version 2
end
write memory
```

---

## 🟢 3Com Comware — 4500G, 4210

> Recuerda: `display` en lugar de `show`, `system-view` en lugar de `configure terminal`,
> y **hay que ejecutar `save`** para persistir.

### Básico y navegación

```text
system-view                             ! entrar a configuración
 sysname F104-SW-4500G-01
 quit
save                                    ! guardar en startup.cfg
display current-configuration
display saved-configuration
display version
display device
display clock
reboot
```

### Diagnóstico

```text
display interface brief
display interface GigabitEthernet 1/0/1
display vlan all
display mac-address
display arp
display ip routing-table
display stp brief
display link-aggregation summary
display lldp neighbor-information
display logbuffer
display cpu-usage
display memory
display power                            ! sólo modelos PWR/PoE
display transceiver interface            ! diagnóstico de SFP
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
 interface Vlan-interface 104
  ip address 192.168.104.11 255.255.255.0
  quit
 ip route-static 0.0.0.0 0.0.0.0 192.168.104.1
 quit
save
```

> En el **4210** las interfaces de acceso son `Ethernet 1/0/1` (Fast Ethernet) y los uplinks
> `GigabitEthernet 1/0/25-26`.

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

### STP

```text
system-view
 stp mode mstp
 stp enable
 stp priority 4096
 interface GigabitEthernet 1/0/1
  stp edged-port enable
```

### Usuarios, SSH y Telnet

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
 telnet server enable
 quit
save
```

### Enrutamiento (sólo 4500G)

```text
system-view
 interface Vlan-interface 10
  ip address 10.104.10.1 255.255.255.0
  quit
 ospf 1
  area 0
   network 10.104.10.0 0.0.0.255
```

### Respaldo, imagen y ficheros

```text
dir flash:/
display boot-loader
tftp 192.168.104.10 put flash:/startup.cfg SW-3C4500G-01.cfg
tftp 192.168.104.10 get 4500G-CMW520-R2202.bin flash:/4500G-CMW520-R2202.bin
boot-loader file flash:/4500G-CMW520-R2202.bin main
reset saved-configuration               ! ⚠️ borra startup.cfg (factory reset)
```

---

## 🟡 Dell PowerConnect — 7024

> Sintaxis casi idéntica a Cisco IOS. Interfaces: `Gi1/0/1` (unidad/slot/puerto).

### Básico y diagnóstico

```text
enable
configure
 hostname F104-SW-PC7024-01
 exit
copy running-config startup-config
show version
show system
show switch                              ! miembros del stack
show bootvar                             ! imagen activa / de respaldo
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
show clock
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

### Interfaz de gestión y enrutamiento L3

```text
configure
 ip routing
 interface vlan 104
  ip address 192.168.104.21 255.255.255.0
  exit
 interface vlan 10
  ip address 10.104.10.1 255.255.255.0
  exit
 ip default-gateway 192.168.104.1
 ip route 0.0.0.0 0.0.0.0 192.168.104.1
 exit
```

Gestión **out-of-band** (puerto OOB dedicado, recomendado en el laboratorio):

```text
configure
 interface out-of-band
  ip address 192.168.104.21 255.255.255.0 192.168.104.1
```

### OSPF y VRRP

```text
configure
 router ospf
  router-id 1.1.1.1
  network 10.104.10.0 0.0.0.255 area 0
  exit
 interface vlan 10
  vrrp 1
  vrrp 1 ip 10.104.10.254
  vrrp 1 priority 200
  vrrp 1 mode
```

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
 ip ssh server
 crypto key generate rsa
 line ssh
  exec-timeout 15
```

### Respaldo e imagen (doble imagen)

```text
copy running-config tftp://192.168.104.10/SW-PC7024-01.cfg
copy tftp://192.168.104.10/SW-PC7024-01.cfg startup-config
copy tftp://192.168.104.10/PC7000v5.1.9.3.stk image2
boot system image2
show bootvar
clear config                             ! ⚠️ factory reset de la configuración
reload
```

---

## 🟣 Juniper Junos — EX2300, SRX300

> Junos tiene **dos modos**: *operacional* (`>`, sólo consulta) y *configuración* (`#`, editas una
> configuración candidata que **no se aplica hasta `commit`**).

### Navegación y ciclo de vida de la configuración

```text
user@sw> configure                       ! entrar a modo configuración (# )
user@sw# set system host-name F104-SW-EX2300-01
user@sw# show | compare                  ! ver SÓLO lo que vas a cambiar
user@sw# commit check                    ! validar sin aplicar
user@sw# commit confirmed 5              ! aplica y revierte en 5 min si no confirmas
user@sw# commit                          ! confirmar definitivamente
user@sw# rollback 1                       ! volver a la configuración anterior
user@sw# rollback 0                       ! descartar los cambios candidatos
user@sw# exit
user@sw> show configuration | display set ! toda la config como comandos 'set' copiables
```

> [!TIP]
> `commit confirmed 5` es tu red de seguridad cuando trabajas por SSH: si te dejas fuera, el equipo
> se recupera solo en 5 minutos.

### Diagnóstico

```text
show version
show chassis hardware
show chassis routing-engine               ! CPU y memoria
show system uptime
show system storage                       ! ⚠️ crítico en EX2300 antes de actualizar
show system alarms
show interfaces terse
show interfaces ge-0/0/1 extensive        ! errores, CRC, potencia óptica
show ethernet-switching table
show vlans
show arp
show route
show lldp neighbors
show spanning-tree bridge
show log messages | last 50
show system commit                        ! histórico de commits (quién y cuándo)
monitor interface traffic
monitor traffic interface ge-0/0/1        ! tcpdump integrado
```

### VLAN, acceso y trunk (EX2300)

```text
configure
set vlans PRACTICA-A vlan-id 10
set vlans MGMT vlan-id 104

set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access
set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members PRACTICA-A

set interfaces ge-0/0/23 unit 0 family ethernet-switching interface-mode trunk
set interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members [ PRACTICA-A MGMT ]

set vlans MGMT l3-interface irb.104
set interfaces irb unit 104 family inet address 192.168.104.31/24
set routing-options static route 0.0.0.0/0 next-hop 192.168.104.1
commit
```

Gestión out-of-band por el puerto MGMT:

```text
set interfaces me0 unit 0 family inet address 192.168.104.31/24
```

### Agregación de enlaces (LACP)

```text
set chassis aggregated-devices ethernet device-count 2
set interfaces ae0 aggregated-ether-options lacp active
set interfaces ae0 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae0 unit 0 family ethernet-switching vlan members all
set interfaces ge-0/0/22 ether-options 802.3ad ae0
set interfaces ge-0/0/23 ether-options 802.3ad ae0
```

### Usuarios, SSH y servicios

```text
set system root-authentication plain-text-password
set system login user lab-admin class super-user authentication plain-text-password
set system services ssh
set system services web-management https system-generated-certificate
set system host-name F104-SW-EX2300-01
set system name-server 8.8.8.8
set system ntp server 192.168.104.10
set system syslog host 192.168.104.10 any info
```

### RSTP y protección

```text
set protocols rstp interface ge-0/0/1 edge
set protocols rstp bpdu-block-on-edge
set protocols rstp bridge-priority 4k
```

### Respaldo, software y snapshots

```text
show configuration | display set | no-more            ! copiar y pegar a un fichero
file copy /config/juniper.conf.gz scp://user@192.168.104.10:/tmp/
request system storage cleanup
request system software add /var/tmp/junos-arm-32-21.4R3-S4.tgz no-copy no-validate
request system snapshot                               ! punto de restauración
request system reboot
request system zeroize                                ! ⚠️ factory reset total
```

Restaurar configuración:

```text
configure
load override /var/tmp/SW-EX2300-01_base.conf
commit confirmed 5
commit
```

---

## 🔥 Juniper SRX: firewall, NAT y VPN

### Zonas e interfaces

```text
configure
set interfaces ge-0/0/0 unit 0 family inet address 200.1.1.2/30
set interfaces ge-0/0/1 unit 0 family inet address 10.104.1.1/24

set security zones security-zone untrust interfaces ge-0/0/0.0
set security zones security-zone trust interfaces ge-0/0/1.0

# Permitir gestionar el equipo desde la zona trust (PASO QUE TODOS OLVIDAN)
set security zones security-zone trust host-inbound-traffic system-services ping
set security zones security-zone trust host-inbound-traffic system-services ssh
set security zones security-zone trust host-inbound-traffic system-services dhcp
set security zones security-zone untrust host-inbound-traffic system-services ping
commit
```

### Políticas de seguridad

```text
set security policies from-zone trust to-zone untrust policy PERMITIR-SALIDA match source-address any
set security policies from-zone trust to-zone untrust policy PERMITIR-SALIDA match destination-address any
set security policies from-zone trust to-zone untrust policy PERMITIR-SALIDA match application any
set security policies from-zone trust to-zone untrust policy PERMITIR-SALIDA then permit
set security policies from-zone trust to-zone untrust policy PERMITIR-SALIDA then log session-close
```

### NAT de salida (source NAT / PAT)

```text
set security nat source rule-set SALIDA from zone trust
set security nat source rule-set SALIDA to zone untrust
set security nat source rule-set SALIDA rule PAT match source-address 10.104.0.0/16
set security nat source rule-set SALIDA rule PAT then source-nat interface
```

### NAT de entrada (destination NAT — publicar un servidor)

```text
set security nat destination pool SRV-WEB address 10.104.1.50/32 port 80
set security nat destination rule-set ENTRADA from zone untrust
set security nat destination rule-set ENTRADA rule WEB match destination-address 200.1.1.2/32
set security nat destination rule-set ENTRADA rule WEB match destination-port 80
set security nat destination rule-set ENTRADA rule WEB then destination-nat pool SRV-WEB
```

### VPN IPsec basada en rutas (site-to-site)

```text
set security ike proposal P1 authentication-method pre-shared-keys dh-group group14 authentication-algorithm sha-256 encryption-algorithm aes-256-cbc
set security ike policy POL-IKE proposals P1
set security ike policy POL-IKE pre-shared-key ascii-text <clave-compartida>
set security ike gateway GW-REMOTO ike-policy POL-IKE address 200.1.2.2 external-interface ge-0/0/0.0 version v2-only

set security ipsec proposal P2 protocol esp authentication-algorithm hmac-sha-256-128 encryption-algorithm aes-256-cbc
set security ipsec policy POL-IPSEC proposals P2
set security ipsec vpn VPN-LAB ike gateway GW-REMOTO
set security ipsec vpn VPN-LAB ike ipsec-policy POL-IPSEC
set security ipsec vpn VPN-LAB bind-interface st0.0
set security ipsec vpn VPN-LAB establish-tunnels immediately

set interfaces st0 unit 0 family inet mtu 1436
set security zones security-zone vpn interfaces st0.0
set routing-options static route 10.200.0.0/16 next-hop st0.0
commit
```

### Verificación de firewall / NAT / VPN

```text
show security zones
show security policies
show security policies hit-count
show security flow session
show security flow session destination-prefix 8.8.8.8
show security nat source summary
show security nat destination rule all
show security ike security-associations
show security ipsec security-associations
show security ipsec statistics
show log messages | match RT_FLOW_SESSION_DENY
clear security flow session all           ! ⚠️ corta todas las sesiones activas
```

### Chassis Cluster (los 2 SRX300 en alta disponibilidad)

```text
set chassis cluster cluster-id 1 node 0 reboot        ! en el nodo 0
set chassis cluster cluster-id 1 node 1 reboot        ! en el nodo 1
show chassis cluster status
show chassis cluster interfaces
show chassis cluster statistics
```

---

## 🟠 OpenWRT / LEDE — TL-MR3420

> No es una CLI de red, es **Linux**. La configuración vive en ficheros de texto en `/etc/config/`
> y se manipula con **`uci`**; nada se aplica hasta que haces `uci commit` y reinicias el servicio.

### Equivalencias con el resto del laboratorio

| Acción | Equipos de red | OpenWRT |
|---|---|---|
| Ver versión y modelo | `show version` | `ubus call system board` |
| Ver configuración activa | `show running-config` | `uci show` |
| Ver cambios pendientes | — | `uci changes` |
| **Guardar** | `write memory` | `uci commit` + reiniciar el servicio |
| Descartar cambios | — | `uci revert <sección>` |
| Estado de interfaces | `show ip interface brief` | `ip -4 addr show` |
| Tabla de rutas | `show ip route` | `ip route` |
| Tabla ARP | `show arp` | `ip neigh` |
| VLANs | `show vlan brief` | `swconfig dev switch0 show` |
| Reglas de firewall | `show access-lists` | `iptables -L -v -n` |
| Traducciones NAT | `show ip nat translations` | `iptables -t nat -L -v -n` |
| Concesiones DHCP | `show ip dhcp binding` | `cat /tmp/dhcp.leases` |
| Log del sistema | `show logging` | `logread` |
| Reiniciar | `reload` | `reboot` |
| Reset de fábrica | `erase startup-config` | `firstboot -y && reboot -f` |

### Diagnóstico

```text
ubus call system board
cat /etc/openwrt_release
uname -a
df -h
df -h /overlay
free
ip -4 addr show
ip route
brctl show
swconfig dev switch0 show
iwinfo
wifi status
logread | tail -50
netstat -tulpn
```

### UCI: el ciclo de configuración

```text
uci show network
uci set network.lan.ipaddr='10.104.50.1'
uci changes
uci commit network
/etc/init.d/network restart
```

Para descartar en lugar de confirmar: `uci revert network`.

### WiFi (punto de acceso WPA2)

```text
uci set wireless.@wifi-device[0].disabled='0'
uci set wireless.@wifi-device[0].channel='6'
uci set wireless.@wifi-iface[0].ssid='F104-LAB'
uci set wireless.@wifi-iface[0].encryption='psk2'
uci set wireless.@wifi-iface[0].key='<clave-wifi>'
uci commit wireless
wifi
```

Verificar: `iwinfo` · `iwinfo wlan0 assoclist` · `iwinfo wlan0 scan`

### VLANs 802.1Q en el switch integrado

```text
swconfig dev switch0 show
uci show network | grep switch
```

> En `ports`, el sufijo `t` marca el puerto como *tagged* (trunk) y sin sufijo es *untagged*
> (acceso). El puerto `0` suele ser el interno hacia la CPU.

### Firewall por zonas (el mismo modelo del SRX, con iptables debajo)

```text
uci show firewall
/etc/init.d/firewall restart
iptables -L -v -n
iptables -t nat -L -v -n
```

### Paquetes

```text
df -h /overlay
opkg update
opkg list-installed
opkg install <paquete>
```

> ⚠️ **Comprueba `df -h /overlay` antes de instalar.** Con 4 MB de flash es muy fácil llenar el
> sistema de ficheros y dejar el router en un estado del que sólo se sale reinstalando.

### Respaldo y restauración

```text
sysupgrade -b /tmp/RT-MR3420-01_AAAA-MM-DD.tar.gz
```

```text
sysupgrade -r /tmp/RT-MR3420-01_base.tar.gz
```

### Modo failsafe (contraseña perdida)

Enciende el router y, cuando el LED SYS empiece a parpadear rápido, pulsa varias veces
Reset/QSS. Luego, con el PC en `192.168.1.2/24`:

```text
telnet 192.168.1.1
```

```text
mount_root
passwd root
sync
reboot -f
```

Detalle completo en el [plan de contingencia del equipo](../equipos/RT-MR3420-01/plan-contingencia.md).

---

## 🧰 Comandos de emergencia (los 10 imprescindibles)

| # | Situación | Comando |
|:--:|---|---|
| 1 | Ver qué versión y hardware tengo delante | `show version` · `display version` |
| 2 | Guardar antes de apagar | `write memory` · `save` · `copy run start` · `commit` |
| 3 | Un puerto no levanta | `show interfaces <if>` · `display interface <if>` · `show interfaces <if> extensive` |
| 4 | Saber si un cable serie es DCE o DTE | `show controllers Serial 0` |
| 5 | ¿Qué hay conectado al otro lado? | `show cdp neighbors` · `display lldp neighbor-information` · `show lldp neighbors` |
| 6 | Deshacer un cambio en Junos | `rollback 1` + `commit` |
| 7 | Trabajar en remoto sin quedarme fuera | Junos: `commit confirmed 5` · IOS: `reload in 10` (y `reload cancel`) |
| 8 | Espacio en disco insuficiente (EX2300) | `request system storage cleanup` |
| 9 | Ver por qué se descarta el tráfico (SRX) | `show security flow session` · `show security policies hit-count` |
| 10 | Apagar todos los debugs de IOS | `undebug all` |
| 11 | Recuperar un OpenWRT sin contraseña | *failsafe* + `mount_root` + `passwd root` |

---

## 🧑‍🎓 Errores frecuentes en el laboratorio

| Error | Síntoma | Solución |
|---|---|---|
| No guardar la configuración | Al reiniciar se pierde todo | `write memory` / `save` / `copy run start` / `commit` |
| Olvidar `no shutdown` (Cisco) | Interfaz `administratively down` | `interface X` → `no shutdown` |
| No poner `clock rate` en el DCE | Enlace serie `down/down` | `show controllers serial 0` y `clock rate 64000` en el DCE |
| VLAN no permitida en el trunk | Un host no ve a otro entre switches | `switchport trunk allowed vlan add <id>` |
| Native VLAN distinta en cada lado | Errores de STP / tráfico cruzado | Igualar `switchport trunk native vlan` |
| Olvidar `host-inbound-traffic` (SRX) | No puedes hacer ping ni SSH al firewall | Añadir `system-services ssh ping` a la zona |
| `commit` sin contraseña de root (Junos) | El commit falla | `set system root-authentication plain-text-password` |
| Mezclar Comware v3 y v5 | El comando «no existe» en el 4210 | Usar `?` para ver la sintaxis real del equipo |
| Actualizar EX2300 sin espacio | Actualización fallida a medias | `request system storage cleanup` antes |
| Borrar la imagen del 2900XL/2503 | El equipo no arranca | [Plan de contingencia](02-plan-contingencia.md) |
| Olvidar `uci commit` en OpenWRT | El cambio no se aplica y se pierde al reiniciar | `uci commit <sección>` + `/etc/init.d/<servicio> restart` |
| Llenar la flash del TL-MR3420 | El router deja de arrancar bien | `df -h /overlay` **antes** de cada `opkg install` |

---

[⬅️ Volver al índice](../README.md) · [📊 Comparativa](01-comparativa.md) · [📇 Fichas por equipo](../equipos/README.md) · [🚨 Plan de contingencia](02-plan-contingencia.md)
