# ⭐ RT-C2503-01 — Características y protocolos

**Cisco 2503 (serie 2500)** · Router de acceso fijo con 2 puertos serie e ISDN BRI. Ejecuta IOS **Enterprise** multiprotocolo, pero con sólo 4 MB de DRAM.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **IOS Enterprise multiprotocolo**: es el único equipo del laboratorio capaz de hacer prácticas de **IPX, AppleTalk, DECnet, VINES, XNS y LAT**. Un valor didáctico que ningún equipo moderno tiene.
- **X.25 completo** (v2.0, NET2/BFE/GOSIP), **TN3270** y **SuperLAT**: protocolos históricos que se pueden mostrar en funcionamiento real, no sólo en teoría.
- **ISDN BRI integrada** con software Basic Rate v1.0 → prácticas de DDR (*Dial-on-Demand Routing*).
- **BOOTFLASH con imagen RXBOOT**: aunque la flash principal se corrompa, el router arranca desde ROM y se puede reparar por TFTP. Es su gran red de seguridad.
- **`Ethernet0` ejecuta a 10 Mbps half-duplex** — sirve perfectamente para prácticas y es una buena forma de enseñar negociación de velocidad/dúplex.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Enrutamiento IP** | Estático, RIP v1/v2, IGRP, **EIGRP**, **OSPF**, **BGP-4**, EGP, redistribución |
| **Multiprotocolo** (Enterprise) | **IPX/Novell**, **AppleTalk**, **DECnet**, **Banyan VINES**, **XNS**, **Apollo Domain**, **SuperLAT**, **TN3270** |
| **WAN** | HDLC, **PPP** (PAP/CHAP), **Frame Relay**, **X.25** v2.0 (NET2/BFE/GOSIP), SMDS, **ISDN BRI** + DDR |
| **Servicios IP** | **NAT** (introducido en IOS 11.2), ACL estándar y extendidas, `ip helper-address` (DHCP relay), HSRP, proxy ARP, NTP, CDP, SNMP v1/v2c |
| **Bridging** | Transparent bridging, SRB / RSRB, concurrent routing and bridging |
| **QoS** | Priority queuing, custom queuing, WFQ |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **4 MB de DRAM.** Es el techo real de este equipo: **no se puede actualizar a IOS 12.x** (12.0 IP ya pide 6-8 MB y 12.3 exige 16 MB de DRAM y 16 MB de flash). Queda fijado en IOS 11.x.
- ⚠️ **Flash de 8 MB con sólo 396 KB libres.** No cabe una segunda imagen: para actualizar hay que **borrar la actual primero**, lo que deja el router sin sistema durante el proceso.
- ⚠️ **Flash marcada `Read ONLY`**: es normal (el IOS se ejecuta *desde* la flash). Para escribir en ella hay que arrancar desde ROM — ver el plan de contingencia.
- ⚠️ **Sin transceptor AUI, `Ethernet0` se queda en `up/down`.** El conector largo de 15 pines es el AUI; sin el transceptor no hay LAN por esa vía. **No es bloqueante**: el [plan de contingencia](plan-contingencia.md#b2--tftp-por-enlace-serie-usando-otro-router-como-pasarela-) documenta cómo recuperar la imagen y respaldar la configuración por el `Serial0`, usando un Cisco 2620 como pasarela hacia la LAN.
- ❌ **Sin SSH** y **sin servidor DHCP** (llegó en IOS 12.0). Sólo Telnet y `ip helper-address`.
- ❌ **Sin FastEthernet** y **sin sub-interfaces 802.1Q** en el puerto Ethernet.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
show flash
show ip interface brief
show controllers Serial 0
show running-config
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
