# ⭐ SW-3C4500G-01 — Características y protocolos

**3Com Switch 4500G 24-Port** · Switch Gigabit gestionable de 24 puertos + 4 SFP con **enrutamiento de Capa 3**. El equipo con más capacidad de conmutación del laboratorio junto al PowerConnect.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **28 puertos Gigabit en total** (24 RJ-45 + 4 SFP dedicados): es el switch con más puertos Gigabit del laboratorio.
- **Enrutamiento de Capa 3 real**: rutas estáticas, **RIP v1/v2**, **OSPFv2** y **VRRP**. Permite montar prácticas de enrutamiento inter-VLAN y redundancia de gateway sin necesidad de un router externo.
- **128 MB de SDRAM y 16 MB de flash**: hay espacio de sobra para una segunda imagen de respaldo en el propio equipo.
- **CLI Comware** (heredada de H3C/Huawei): tener este switch junto a los Cisco, Dell y Juniper convierte el laboratorio en un banco de comparación de cuatro sintaxis distintas. Valor didáctico muy alto.
- **SSHv2, 802.1X y ACL completas** → prácticas de acceso seguro y control de admisión.
- **MSTP (802.1s)** y **LACP** → prácticas de redundancia y agregación con negociación.
- **4 SFP** para prácticas de fibra óptica y transceptores.
- **Equivalente OEM del H3C S5500-EI / HP 4500G**: la documentación de H3C y HPE también le aplica, lo que amplía mucho las fuentes disponibles.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q VLAN (4094 IDs), VLAN de voz, GVRP, QinQ, **STP / RSTP / MSTP**, BPDU guard, *loopback detection*, **LACP** (802.3ad), *port isolation*, jumbo frames, *storm control* |
| **Capa 3** | Rutas estáticas, **RIP v1/v2**, **OSPFv2**, **VRRP**, proxy ARP, DHCP server / relay / *snooping*, interfaces `Vlan-interface` |
| **IPv6** | Doble pila, ND, DHCPv6 relay · ⚠️ RIPng / OSPFv3 según la versión de software |
| **Multicast** | IGMP v1/v2/v3 *snooping*, IGMP *querier* · ⚠️ PIM-DM/SM a confirmar en esta versión |
| **Seguridad** | ACL de L2/L3/L4, **802.1X**, autenticación MAC, *port security*, RADIUS, HWTACACS, AAA, **SSHv2**, niveles de usuario 0-3 |
| **QoS** | Clasificación 802.1p / DSCP, colas SP y WRR, *rate limiting*, *policing* y *shaping* |
| **Gestión** | LLDP, NTP, syslog, *mirroring* local y remoto, SNMP v1/v2c/v3, RMON, gestión web, *cluster management* |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **Producto fuera de soporte del fabricante** (3Com desapareció al ser absorbida por HP). La imagen `.bin` **ya no es descargable**: la copia del laboratorio es la única fuente. Es de máxima prioridad tenerla en el Drive y en la PC del laboratorio.
- ⚠️ La CLI **no es Cisco**: `system-view` en vez de `configure terminal`, `display` en vez de `show`, `quit` en vez de `exit`, y **hay que ejecutar `save`** explícitamente o se pierde todo al reiniciar. Es el error más común de los alumnos con este equipo.
- ⚠️ **Contraseña del BootROM**: si se pierde *además* de la del sistema, el equipo **no es recuperable por consola**. Anótala en la sección [Acceso](README.md#-acceso) y no la cambies sin registrarla.
- ⚠️ Interfaces nombradas `GigabitEthernet 1/0/1` (chasis/subslot/puerto), no `Gi0/1`.
- ⚠️ **Sin BGP ni IS-IS**: para prácticas de enrutamiento externo hay que usar los Cisco 2620.
- ❌ Sin PoE (no es modelo `PWR`) y sin módulo 10 Gigabit instalado.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
display version
display device
display device manuinfo
dir flash:/
display boot-loader
display interface brief
display current-configuration
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
