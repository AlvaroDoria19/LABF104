# ⭐ SW-3C4210-01 — Características y protocolos

**3Com Switch 4210 26-Port** · Switch Fast Ethernet gestionable de 24 puertos + 2 uplinks, **sólo Capa 2**. Switch de acceso ideal para prácticas de VLAN y 802.1X.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **26 puertos** (24 Fast Ethernet + 2 uplinks): buena densidad para dar servicio a un aula entera de puestos de prácticas.
- **MSTP, LACP y 802.1X** en un switch de acceso económico: cubre las prácticas de redundancia, agregación y control de admisión sin necesitar el 4500G.
- **CLI Comware**, igual que el 4500G → el alumno aprende una sola sintaxis para los dos switches 3Com.
- **Autenticación MAC y port isolation**: prácticas de aislamiento de clientes en el mismo dominio de difusión.
- Perfecto como **switch de borde** en topologías jerárquicas: 4210 en acceso → 4500G o PowerConnect en distribución.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q VLAN, VLAN de voz, GVRP, **STP / RSTP / MSTP**, **LACP** (802.3ad), *port isolation*, *storm control*, *loopback detection* |
| **Capa 3** | ❌ **Sin enrutamiento.** Sólo `Vlan-interface` para la propia gestión + `ip route-static` como gateway por defecto |
| **Multicast** | IGMP *snooping* v1/v2 |
| **Seguridad** | ACL básicas, **802.1X**, autenticación MAC, *port security*, RADIUS, AAA, niveles de usuario · ⚠️ SSHv2 sólo en releases recientes |
| **QoS** | Prioridad 802.1p, colas, *rate limiting* de entrada |
| **Gestión** | Consola, Telnet, web, SNMP v1/v2c/v3, syslog, *mirroring* de puerto, NTP/SNTP · ⚠️ LLDP a confirmar |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **Datos de este equipo pendientes de capturar.** Ejecuta los [comandos de verificación](#-comandos-de-verificación) y rellena las tablas de esta ficha.
- ❌ **Sin enrutamiento de Capa 3.** Cualquier práctica inter-VLAN necesita el 4500G, el PowerConnect o un router.
- ❌ **Sólo Fast Ethernet en acceso** (100 Mbps). No lo uses como núcleo de la topología.
- ⚠️ **Comware v3 ≠ Comware v5.** Aunque se parezcan, hay comandos que cambian respecto al 4500G. Si un comando falla, usa `?` para ver la sintaxis real.
- ⚠️ **SSH puede no estar disponible** en Comware v3. Verifica con `display ssh server status`; si no lo soporta, gestión sólo por Telnet en la VLAN 104 aislada.
- ⚠️ **Producto fuera de soporte del fabricante**: la imagen `.bin` no es descargable. La copia del laboratorio es la única fuente.
- ⚠️ **Contraseña del BootROM**: si se pierde junto con la del sistema, el equipo no es recuperable por consola.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
display version
display device
dir flash:/
display boot-loader
display interface brief
display vlan all
display current-configuration
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
