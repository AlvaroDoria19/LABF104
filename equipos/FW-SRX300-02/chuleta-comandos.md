# ⚡ FW-SRX300-02 — Chuleta de comandos

**Juniper SRX300**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> **Consola:** `9600` baudios · 8 bits · sin paridad · 1 bit de stop · sin control de flujo
> Credenciales en la [ficha del equipo](README.md#-acceso).
> Para comparar la sintaxis con las otras familias de CLI del laboratorio, ve a la
> [chuleta general](../../docs/03-chuleta-comandos.md).

---

### Los dos modos de Junos

```text
root> ...            modo OPERACIONAL — sólo consulta
root# ...            modo CONFIGURACIÓN — config candidata, nada se aplica hasta 'commit'
```

### Ciclo de vida de la configuración

```text
configure
show | compare
commit check
commit confirmed 5
commit
rollback 1
exit
show configuration | display set
```

### Diagnóstico general

```text
show version
show system information
show chassis hardware
show system firmware
show system license
show system uptime
show system storage
show system alarms
show interfaces terse
show route
show log messages | last 50
show system commit
monitor traffic interface ge-0/0/0
```

### Zonas e interfaces

```text
configure
set interfaces ge-0/0/0 unit 0 family inet address 200.1.1.2/30
set interfaces ge-0/0/1 unit 0 family inet address 10.104.1.1/24

set security zones security-zone untrust interfaces ge-0/0/0.0
set security zones security-zone trust interfaces ge-0/0/1.0

# Permitir gestionar el equipo desde la zona trust — EL PASO QUE TODOS OLVIDAN
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
commit
```

### NAT de salida (source NAT / PAT)

```text
set security nat source rule-set SALIDA from zone trust
set security nat source rule-set SALIDA to zone untrust
set security nat source rule-set SALIDA rule PAT match source-address 10.104.0.0/16
set security nat source rule-set SALIDA rule PAT then source-nat interface
commit
```

### NAT de entrada (publicar un servidor)

```text
set security nat destination pool SRV-WEB address 10.104.1.50/32 port 80
set security nat destination rule-set ENTRADA from zone untrust
set security nat destination rule-set ENTRADA rule WEB match destination-address 200.1.1.2/32
set security nat destination rule-set ENTRADA rule WEB match destination-port 80
set security nat destination rule-set ENTRADA rule WEB then destination-nat pool SRV-WEB
commit
```

### VPN IPsec *route-based* (la práctica estrella con los dos SRX300)

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

### Verificación de seguridad, NAT y VPN

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
clear security flow session all
```

> `show security policies hit-count` te dice qué políticas se están usando de verdad — perfecto
> para depurar por qué el tráfico no pasa.

### Chassis Cluster (los dos SRX300 en alta disponibilidad)

```text
set chassis cluster cluster-id 1 node 0 reboot      ! en el nodo 0
set chassis cluster cluster-id 1 node 1 reboot      ! en el nodo 1
```

Verificar: `show chassis cluster status` · `show chassis cluster interfaces` ·
`show chassis cluster statistics`

### Usuarios y servicios

```text
set system root-authentication plain-text-password
set system login user lab-admin class super-user authentication plain-text-password
set system services ssh
set system services web-management https system-generated-certificate
set system ntp server 192.168.104.10
set system syslog host 192.168.104.10 any info
commit
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
