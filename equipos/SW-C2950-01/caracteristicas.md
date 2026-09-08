# ⭐ SW-C2950-01 — Características y protocolos

**Cisco Catalyst WS-C2950-24** · Switch de 24 puertos 10/100, Capa 2, con **Standard Image (SI)**. El mejor equipo del laboratorio para prácticas Cisco de VLAN, RSTP, EtherChannel y 802.1X.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **RSTP y MSTP** (802.1w / 802.1s): el único switch Cisco del laboratorio con *spanning tree* moderno. Comparándolo con el 2900XL (sólo PVST) se ve muy bien la diferencia de convergencia.
- **EtherChannel con PAgP y LACP**: prácticas de agregación de enlaces con negociación real.
- **802.1X** con *Guest VLAN* → prácticas de control de acceso por puerto con RADIUS.
- **Port security dinámica y *sticky***, *storm control* y *protected ports*: seguridad de capa 2 completa.
- **SPAN** para captura de tráfico con Wireshark en las prácticas de análisis.
- **QoS con auto-QoS para VoIP**, 4 colas por puerto y WRR.
- **Voice VLAN** → prácticas de telefonía IP junto a los routers.
- **Botón MODE físico** → recuperación de contraseña rápida y sin red.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q *trunking* (❌ sin ISL), **VTP v1/v2**, **STP / RSTP / MSTP**, PVST+, PortFast, BPDU Guard, UplinkFast, BackboneFast, Root Guard, **EtherChannel (PAgP + LACP)**, UDLD, Voice VLAN, *protected ports* |
| **Capa 3** | ❌ Sin enrutamiento. Sólo `ip default-gateway` para la gestión |
| **Multicast** | IGMP snooping v1/v2, CGMP |
| **Seguridad** | **802.1X** con Guest VLAN, *port security* estática/dinámica/*sticky*, *storm control*, RADIUS, TACACS+, AAA, SNMPv3, ACL de acceso a la gestión |
| **QoS** | Clasificación y marcado 802.1p/DSCP, 4 colas por puerto, WRR, *auto-QoS* para VoIP |
| **Gestión** | Consola, **Telnet**, Device Manager (web), SNMP v1/v2c/v3, CDP, **SPAN**, syslog, NTP |

---

## ⚠️ Limitaciones de este equipo

- ❌ **Sin SSH.** `show version` confirma `Running Standard Image`, que **no incluye criptografía**. El acceso remoto es Telnet en claro → gestión sólo en la VLAN 104 con ACL.
- ❌ **Standard Image (SI)**: no tiene ACL de router ni *VLAN maps*, ni **RSPAN**, ni *rate limiting* de entrada. Todo eso es exclusivo de la Enhanced Image (EI).
- ❌ **Sin enrutamiento IP** ni IPv6 en el plano de datos.
- ❌ **Sin uplinks Gigabit**: el `WS-C2950-24` tiene 24 puertos 10/100 y nada más. Los *trunks* hacia el 4500G o el PowerConnect irán a 100 Mbps.
- ⚠️ **Sin LLDP** (sólo CDP) en esta versión de IOS.
- ⚠️ Su `hostname` actual (`SW_SERVERS`) es casi idéntico al del 2900XL (`SW_servers`). **Renómbralos** según la convención del laboratorio.
- 💡 Si alguna práctica exigiera SSH, existe la imagen EI con cripto `c2950-i6k2l2q4-mz.121-22.EA14.bin`, pero es software EOL de difícil obtención. **No es necesario para las prácticas habituales.**

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
dir flash:
show interfaces status
show vlan brief
show running-config
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
