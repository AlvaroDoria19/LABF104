# ⭐ RT-C2503-02 — Características y protocolos

**Cisco 2503 (serie 2500)** · Router de acceso fijo con 2 puertos serie e ISDN BRI. Tiene **16 MB de DRAM** (4× más que su gemelo) pero ejecuta un IOS más antiguo: 11.1.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **16 MB de DRAM**: cuatro veces más que el `RT-C2503-01`. Es el 2503 con más margen de memoria y, en teoría, el único de los dos que podría actualizarse a IOS 12.0/12.1 (la flash de 8 MB sí admitiría una imagen `c2500-i-l` de 12.0).
- **ISDN BRI integrada** con software Basic Rate v1.0 → prácticas de DDR.
- **X.25 v2.0** (NET2/BFE/GOSIP) e **IPX** → prácticas multiprotocolo.
- **BOOTFLASH con imagen RXBOOT**: el router se puede reparar por TFTP aunque la flash principal se corrompa.
- Muy útil como **pareja del `RT-C2503-01`** para montar enlaces serie back-to-back con cable DB-60 DTE/DCE.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Enrutamiento IP** | Estático, RIP v1/v2, IGRP, **EIGRP**, **OSPF**, **BGP-4**, EGP, redistribución |
| **Multiprotocolo** | **IPX/Novell**, bridging. ⚠️ Sin AppleTalk/DECnet/VINES/LAT/TN3270 (eso es sólo Enterprise → los tiene el `RT-C2503-01`) |
| **WAN** | HDLC, **PPP** (PAP/CHAP), **Frame Relay**, **X.25** v2.0, **ISDN BRI** + DDR |
| **Servicios IP** | ACL estándar y extendidas, `ip helper-address` (DHCP relay), HSRP, proxy ARP, NTP, CDP, SNMP v1 |
| **Bridging** | Transparent bridging, SRB / RSRB |
| **QoS** | Priority queuing, custom queuing |

---

## ⚠️ Limitaciones de este equipo

- ❌ **Sin NAT.** NAT se introdujo en IOS **11.2**, y este equipo tiene 11.1. Si una práctica necesita NAT, usa el `RT-C2503-01` (11.2) o mejor un 2620.
- ❌ **Sin servidor DHCP** (llegó en IOS 12.0). Sólo `ip helper-address` como relay.
- ❌ **Sin SSH.** Sólo Telnet en claro → gestión restringida a la VLAN 104 con ACL.
- ⚠️ **IOS distinto al del `RT-C2503-01`** (11.1 `INR` frente a 11.2 `Enterprise`). Son equipos físicamente iguales con software y capacidades diferentes: **no asumas que una práctica que funciona en uno funciona en el otro**.
- ⚠️ **Flash marcada `Read ONLY`** (normal en *run-from-flash*): para escribir hay que arrancar desde ROM.
- ❌ **Sin transceptor AUI, no hay LAN.** El conector largo de 15 pines es `Ethernet0`.
- ❌ Sin FastEthernet ni sub-interfaces 802.1Q.

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

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
