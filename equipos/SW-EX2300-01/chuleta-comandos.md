# ⚡ SW-EX2300-01 — Chuleta de comandos

**Juniper EX2300-24T**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> **Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo
> Credenciales en la [ficha del equipo](README.md#-acceso).
> Para comparar la sintaxis con las otras familias de CLI del laboratorio, ve a la
> [chuleta general](../../docs/03-chuleta-comandos.md).

---

### Los dos modos de Junos

```text
user@sw> ...            modo OPERACIONAL — sólo consulta
user@sw# ...            modo CONFIGURACIÓN — editas una config candidata
```

**Nada se aplica hasta que haces `commit`.**

### Ciclo de vida de la configuración

```text
configure
set system host-name F104-SW-EX2300-01
show | compare              ! ver SÓLO lo que vas a cambiar
commit check                ! validar sin aplicar
commit confirmed 5          ! aplica y revierte en 5 min si no confirmas
commit                      ! confirmar definitivamente
rollback 1                  ! volver a la configuración anterior
rollback 0                  ! descartar los cambios candidatos
exit
```

> [!TIP]
> **`commit confirmed 5` es tu red de seguridad.** Si trabajas por SSH y te dejas fuera, el switch
> se recupera solo en 5 minutos. Enséñaselo a los alumnos el primer día.

### Diagnóstico

```text
show version
show system information
show chassis hardware
show chassis routing-engine
show system uptime
show system storage
show system alarms
show system license
show interfaces terse
show interfaces ge-0/0/1 extensive
show ethernet-switching table
show vlans
show arp
show route
show lldp neighbors
show spanning-tree bridge
show virtual-chassis
show log messages | last 50
show system commit
show configuration | display set
monitor interface traffic
monitor traffic interface ge-0/0/1
```

> `| no-more` evita la paginación. `| display set` traduce la configuración a comandos `set`
> copiables — es la forma más rápida de documentar o replicar una configuración.

### VLAN, acceso y trunk

```text
configure
set vlans PRACTICA-A vlan-id 10
set vlans PRACTICA-B vlan-id 20
set vlans MGMT vlan-id 104

set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access
set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members PRACTICA-A

set interfaces ge-0/0/23 unit 0 family ethernet-switching interface-mode trunk
set interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members [ PRACTICA-A PRACTICA-B MGMT ]
commit
```

### Enrutamiento inter-VLAN (IRB)

```text
set vlans PRACTICA-A l3-interface irb.10
set interfaces irb unit 10 family inet address 10.104.10.1/24
set vlans MGMT l3-interface irb.104
set interfaces irb unit 104 family inet address 192.168.104.31/24
set routing-options static route 0.0.0.0/0 next-hop 192.168.104.1
commit
```

### Gestión out-of-band por el puerto MGMT

```text
set interfaces me0 unit 0 family inet address 192.168.104.31/24
commit
```

### Agregación de enlaces (LACP)

```text
set chassis aggregated-devices ethernet device-count 2
set interfaces ae0 aggregated-ether-options lacp active
set interfaces ae0 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae0 unit 0 family ethernet-switching vlan members all
set interfaces ge-0/0/22 ether-options 802.3ad ae0
set interfaces ge-0/0/23 ether-options 802.3ad ae0
commit
```

Verificar: `show lacp interfaces` · `show interfaces ae0 terse`

### RSTP y protección

```text
set protocols rstp interface ge-0/0/1 edge
set protocols rstp bpdu-block-on-edge
set protocols rstp bridge-priority 4k
commit
```

### Usuarios y servicios

```text
set system root-authentication plain-text-password
set system login user lab-admin class super-user authentication plain-text-password
set system services ssh
set system services web-management https system-generated-certificate
set system name-server 8.8.8.8
set system ntp server 192.168.104.10
set system syslog host 192.168.104.10 any info
commit
```

### 802.1X

```text
set access radius-server 192.168.104.10 secret <clave>
set access profile DOT1X authentication-order radius
set access profile DOT1X radius authentication-server 192.168.104.10
set protocols dot1x authenticator authentication-profile-name DOT1X
set protocols dot1x authenticator interface ge-0/0/1 supplicant single
commit
```

Verificar: `show dot1x interface` · `show dot1x authentication-failed-users`

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
