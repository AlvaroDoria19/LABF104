# ⭐ SW-PC7024-03 — Características y protocolos

**Dell PowerConnect 7024** · Switch Gigabit gestionable de 24 puertos con **Capa 3 completa** (OSPF, VRRP, multicast) y apilamiento. CLI casi idéntica a Cisco IOS.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **Capa 3 completa**: rutas estáticas, **RIP v1/v2**, **OSPFv2 y OSPFv3**, **VRRP**, *policy based routing* y **multicast PIM-DM/PIM-SM**. Es el switch más capaz del laboratorio en enrutamiento.
- **Puerto de gestión Out-of-Band dedicado**: la joya de este equipo para un laboratorio docente. Permite gestionar el switch por una red totalmente separada, de modo que **una práctica mal configurada no te deja sin acceso**. Úsalo siempre.
- **Doble imagen (`image1` / `image2`)**: se puede actualizar el firmware manteniendo la versión anterior intacta y arrancable. Es la mejor protección contra imágenes corruptas de todo el laboratorio.
- **Apilamiento de hasta 12 unidades**: con varias unidades se pueden montar prácticas de *stacking* reales.
- **CLI prácticamente idéntica a Cisco IOS** (`enable`, `configure`, `show running-config`, `copy running-config startup-config`): excelente para que el alumno vea que la sintaxis Cisco no es exclusiva de Cisco.
- **Seguridad de capa 2 avanzada**: DHCP snooping, **Dynamic ARP Inspection**, IP Source Guard y 802.1X con VLAN dinámica.
- **sFlow y LLDP-MED** para prácticas de monitorización y telefonía IP.
- **Menú de arranque con recuperación de contraseña integrada** → el procedimiento más limpio del laboratorio.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q VLAN, VLAN de voz, GVRP/MVRP, **STP / RSTP / MSTP / PVSTP+**, BPDU guard, *root guard*, *loop protection*, **LACP** (802.3ad), jumbo frames, *storm control* |
| **Capa 3 IPv4** | Rutas estáticas, **RIP v1/v2**, **OSPFv2**, **VRRP**, *policy based routing*, DHCP server / relay, `ip helper-address`, proxy ARP |
| **Capa 3 IPv6** | Doble pila, **OSPFv3**, rutas estáticas IPv6, DHCPv6 relay, MLD *snooping* |
| **Multicast** | IGMP v1/v2/v3 *snooping* y *querier*, **PIM-DM / PIM-SM**, MLD |
| **Seguridad** | ACL de IPv4/IPv6/MAC (con temporización), **802.1X** (MAB, Guest VLAN, VLAN dinámica), *port security*, **DHCP snooping**, **Dynamic ARP Inspection**, **IP Source Guard**, RADIUS, TACACS+, **SSH**, HTTPS |
| **QoS** | DiffServ, clasificación 802.1p / DSCP, colas WRR y SP, *policing*, *rate limiting*, *iSCSI optimization* |
| **Gestión** | LLDP + **LLDP-MED**, SNMP v1/v2c/v3, **sFlow**, RMON, *port mirroring*, syslog, NTP/SNTP, *auto-config*, 802.3az (Energy Efficient Ethernet) |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **Versión de firmware pendiente de capturar.** El `show system` que tomaste no la incluye: hace falta **`show version`**. Rellena la tabla de sistema operativo de esta ficha.
- ⚠️ **Todas las unidades tienen el mismo `hostname` (`L3Switch`)**. Renómbralas siguiendo la convención del laboratorio (`F104-SW-PC7024-03`, `-02`…) o será imposible saber en cuál estás trabajando.
- ⚠️ **Probablemente no se puede extraer el fichero `.stk` del switch.** En la mayoría de versiones de firmware la imagen sólo se puede descargar *al* switch, no *desde* él. Comprueba con `copy ?`; si no está disponible, hay que obtener el `.stk` del soporte de Dell y guardarlo en el Drive y en la PC del laboratorio.
- ❌ **Sin BGP ni IS-IS**: para prácticas de enrutamiento externo hay que usar los Cisco 2620.
- ❌ Sin PoE (no es el modelo `7024P`).
- ⚠️ Producto fuera de soporte de Dell: el firmware puede dejar de estar disponible. Respalda el `.stk` en cuanto lo tengas.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
show system
show switch
show bootvar
show interfaces status
show running-config
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
