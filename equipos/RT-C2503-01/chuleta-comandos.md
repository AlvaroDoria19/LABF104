# ⚡ RT-C2503-01 — Chuleta de comandos

**Cisco 2503 (serie 2500)**

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
 hostname F104-RT-2503-01
 no ip domain-lookup
 end
write memory
```

### Diagnóstico

```text
show version
show flash
show ip interface brief
show interfaces Ethernet0
show controllers Serial 0
show ip route
show isdn status
show logging
```

### Interfaces

```text
configure terminal
 interface Ethernet0
  ip address 192.168.104.41 255.255.255.0
  no shutdown
  exit
 interface Serial0
  ip address 172.16.104.1 255.255.255.252
  encapsulation ppp
  clock rate 2000000
  no shutdown
 end
```

> ⚠️ `Ethernet0` no pasará a `up/up` sin el transceptor AUI conectado.
> `clock rate` sólo en el extremo DCE (`show controllers Serial 0`).

### Enrutamiento

```text
router ospf 1
 network 172.16.104.0 0.0.0.3 area 0
 exit
ip route 0.0.0.0 0.0.0.0 172.16.104.2
```

### ISDN BRI

```text
configure terminal
 isdn switch-type basic-net3
 interface BRI0
  ip address 10.104.99.1 255.255.255.0
  encapsulation ppp
  dialer map ip 10.104.99.2 name REMOTO <numero>
  dialer-group 1
  no shutdown
  exit
 dialer-list 1 protocol ip permit
 end
```

Verificar: `show isdn status` · `show dialer` · `show interfaces BRI0`

### IPX (exclusivo de este equipo)

```text
configure terminal
 ipx routing
 interface Ethernet0
  ipx network 100 encapsulation novell-ether
 end
```

Verificar: `show ipx interface` · `show ipx route` · `show ipx servers`

### X.25

```text
interface Serial0
 encapsulation x25
 x25 address 3110222
 x25 map ip 172.16.104.2 3110333 broadcast
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
