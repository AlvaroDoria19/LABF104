# ⭐ RT-C2620-01 — Características y protocolos

**Cisco 2620 (serie 2600)** · Router modular de acceso con FastEthernet y múltiples puertos serie. El equipo más versátil del laboratorio para prácticas de enrutamiento y WAN.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **64 MB de DRAM y 16 MB de flash**: la mejor dotación de memoria del laboratorio entre los routers. Tiene margen para actualizar a IOS 12.3 si algún día hiciera falta.
- **IOS descomprimido en RAM** (a diferencia del 2503, que ejecuta desde flash): mucho más rápido y con margen para imágenes grandes.
- **Muchos puertos serie**: es el router con el que montar las prácticas de WAN, Frame Relay y PPP multi-enlace.
- **Feature set IP Plus**: enrutamiento completo (incluido BGP e IS-IS), X.25, Frame Relay, ISDN, NAT y QoS avanzada.
- **`FastEthernet0/0` soporta sub-interfaces 802.1Q** → prácticas de *router-on-a-stick* con los switches del laboratorio.
- Sobra espacio en flash (≈ 6,4 MB libres) → **admite una segunda imagen de respaldo en el propio equipo**, cosa que ningún otro router del laboratorio puede hacer.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Enrutamiento IP** | Estático, RIP v1/v2, IGRP, **EIGRP**, **OSPFv2**, **BGP-4**, IS-IS, ODR, redistribución, *route-maps*, PBR |
| **Conmutación / VLAN** | Sub-interfaces 802.1Q (`FastEthernet0/0.10`) para enrutamiento inter-VLAN |
| **WAN** | HDLC, **PPP** (PAP/CHAP, MLPPP), **Frame Relay** (LMI, sub-interfaces, FRTS), **X.25** v3.0.0, ISDN, async/sync de baja velocidad |
| **Servicios IP** | **NAT/PAT**, DHCP server y relay, ACL estándar/extendidas/nombradas, NTP, HSRP, proxy ARP, CDP, SNMP v1/v2c/v3 |
| **QoS** | WFQ, CBWFQ, LLQ, policing y shaping, RSVP, compresión de cabeceras |
| **Bridging** | Transparent bridging, IRB |
| **Seguridad** | AAA, RADIUS, TACACS+, ACL, contraseñas cifradas (`enable secret`) |
| **IPv6** | ⚠️ Improbable en IOS 12.2 mainline. Verifica con `ipv6 ?` en configuración global |

---

## ⚠️ Limitaciones de este equipo

- ❌ **Sin SSH.** La imagen `C2600-IS-M` no lleva criptografía (`k9`). El acceso remoto es **Telnet en claro** → mantén la gestión en la VLAN 104 aislada y protégela con ACL.
- ❌ **Sin IPsec ni VPN**, por el mismo motivo.
- ⚠️ Si necesitáis SSH/IPsec para alguna práctica, haría falta la imagen `c2600-ik9o3s-mz.123-26.bin` (hay DRAM y flash suficientes), pero es software EOL de difícil obtención.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
show diag
show flash:
show ip interface brief
show running-config
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
