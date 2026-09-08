# ⭐ SW-EX2300-01 — Características y protocolos

**Juniper EX2300-24T** · Switch Gigabit de acceso con 4 uplinks 10 GbE y Junos. Capa 2 completa + enrutamiento básico, Virtual Chassis y 802.1X.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **Junos OS**: el modelo de configuración más potente del laboratorio. `commit confirmed`, `rollback`, `show | compare` y validación previa con `commit check` son conceptos que ningún otro equipo del laboratorio enseña. Valor didáctico altísimo.
- **`commit confirmed`**: la práctica se puede hacer en remoto sin miedo — si el alumno se deja fuera, el switch revierte solo. Enséñalo el primer día.
- **`rollback 1`**: deshacer un cambio completo con un comando. Comparado con el `write memory` irreversible de Cisco, la diferencia es muy pedagógica.
- **4 uplinks SFP+ a 10 GbE**: los enlaces más rápidos del laboratorio. Sirven para *trunks* de alta capacidad y para **Virtual Chassis**.
- **Virtual Chassis de hasta 4 miembros**: con los dos EX2300 se puede montar un chasis virtual real y ver cómo dos switches físicos se gestionan como uno.
- **Puerto MGMT out-of-band (`me0`)**: gestión por red separada, igual que el PowerConnect. Úsalo.
- **802.1X completo** (single/multiple supplicant, MAC RADIUS, Guest VLAN) y **DHCP snooping + DAI + IP Source Guard**.
- **RSTP / MSTP / VSTP**: incluido VSTP, que es compatible con el PVST+ de Cisco → prácticas de interoperabilidad entre fabricantes con los Catalyst.
- **Automatización nativa**: *op scripts*, *event scripts*, Python y NETCONF/XML. Puerta de entrada a la automatización de redes.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q VLAN, **RSTP / MSTP / VSTP**, BPDU protect, *root protect*, *loop protect*, **LAG / LACP**, Q-in-Q, jumbo frames, *storm control*, MAC limiting, **Virtual Chassis** |
| **Capa 3** | **IRB / RVI** para enrutamiento inter-VLAN, rutas estáticas, **RIP**, DHCP server / relay, filtros de *firewall* (ACL) · ⚠️ **OSPF y funciones L3 avanzadas pueden requerir licencia EFL/AFL** — verifica con `show system license` |
| **IPv6** | Doble pila, ND, MLD *snooping* · ⚠️ RIPng / OSPFv3 según licencia |
| **Multicast** | IGMP v1/v2/v3 *snooping* · ⚠️ PIM con licencia |
| **Seguridad** | **802.1X** (single/multiple supplicant, MAC RADIUS, Guest VLAN), **DHCP snooping**, **Dynamic ARP Inspection**, **IP Source Guard**, filtros de *firewall* por puerto y VLAN, RADIUS, TACACS+, **SSH**, HTTPS |
| **QoS (CoS)** | Clasificación jerárquica, *rewrite rules*, colas, *schedulers*, *shaping* |
| **Gestión / automatización** | LLDP + LLDP-MED, **sFlow**, *port mirroring* (analyzer), syslog, NTP, **NETCONF/XML**, *op* y *event scripts*, Python, J-Web, ZTP |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **Espacio en disco: el problema nº 1 de esta plataforma.** El EX2300 tiene poca flash. **Ejecuta siempre `request system storage cleanup` antes de cualquier `request system software add`** y comprueba con `show system storage`. Es la causa principal de actualizaciones fallidas en este modelo.
- ⚠️ **Junos 18.1R3.3 está fuera de soporte.** No es urgente cambiarlo (funciona y es estable), pero si algún día se actualiza, hazlo **en dos pasos** revisando las *release notes* de la versión destino, y siempre con `request system snapshot` hecho antes.
- ⚠️ **Se está usando `root` directamente** (el `show system information` se ejecutó como `root@SW-LAB1`). **Crea un usuario nominal** de clase `super-user` para el trabajo diario y reserva `root` para consola y emergencias.
- ⚠️ **`commit` falla si `root` no tiene contraseña.** Es el error más habitual al empezar con Junos.
- ⚠️ **Licencias**: algunas funciones de Capa 3 (OSPF y superiores) pueden requerir **EFL/AFL**. Comprueba qué tienes con `show system license` antes de planificar una práctica de enrutamiento dinámico.
- ⚠️ **La imagen `.tgz` no se puede extraer del equipo**: Junos se instala descomprimido. Hay que descargarla del portal de Juniper y guardarla en el Drive, la PC del laboratorio y el **USB de rescate en FAT32**.
- ⚠️ **Hostnames actuales `SW-LAB1` / `SW-LAB2`**: no siguen la convención del laboratorio. Considera renombrarlos a `F104-SW-EX2300-01/02`.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
show system information
show chassis hardware
show system license
show system storage
show interfaces terse
show configuration | display set | no-more
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
