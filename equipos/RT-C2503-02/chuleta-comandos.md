# ⚡ RT-C2503-02 — Chuleta de comandos

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
 hostname F104-RT-2503-02
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
```

### Interfaces

```text
configure terminal
 interface Ethernet0
  ip address 192.168.104.42 255.255.255.0
  no shutdown
  exit
 interface Serial0
  ip address 172.16.104.2 255.255.255.252
  encapsulation ppp
  clock rate 2000000
  no shutdown
 end
```

> ⚠️ `Ethernet0` no pasará a `up/up` sin el transceptor AUI conectado.

### Enrutamiento

```text
router eigrp 104
 network 172.16.0.0
 network 192.168.104.0
 exit
ip route 0.0.0.0 0.0.0.0 172.16.104.1
```

### Enlace back-to-back con el otro 2503

Es la topología estrella de este equipo. Cable DB-60 con un extremo DCE y otro DTE:

```text
show controllers Serial 0
```

En el extremo **DCE** añade `clock rate 2000000`; en el DTE, nada. Luego:

```text
ping 172.16.104.1
show interfaces Serial0
```

### ISDN BRI

```text
configure terminal
 isdn switch-type basic-net3
 interface BRI0
  encapsulation ppp
  dialer-group 1
  no shutdown
 end
```

### IPX

```text
configure terminal
 ipx routing
 interface Ethernet0
  ipx network 200 encapsulation novell-ether
 end
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
