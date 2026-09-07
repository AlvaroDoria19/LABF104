# ⭐ SW-C2900XL-01 — Características y protocolos

**Cisco Catalyst WS-C2924-XL-EN** · Switch de 24 puertos 10/100, sólo Capa 2, con **Enterprise Edition Software**. Equipo histórico ideal para prácticas de VLAN, VTP y STP clásico.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **Enterprise Edition Software**: a diferencia de la Standard Edition, soporta VLANs completas, VTP y *trunking* — es lo que lo hace útil como switch de prácticas y no un simple *hub* gestionable.
- **Cluster member switch capable**: puede integrarse en un clúster gestionado desde otro switch Cisco (función didáctica interesante junto al 2950).
- **24 puertos 10/100**: densidad suficiente para que varios grupos trabajen a la vez.
- **Botón MODE físico** → la recuperación de contraseña es de las más rápidas y fiables del laboratorio (no necesita servidor ni red).
- **Equipo histórico en funcionamiento**: IOS de 2003 sobre hardware de 1998. Excelente para mostrar la evolución de las CLI de Cisco comparándolo con el 2950 y el EX2300.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q y **ISL** *trunking*, **VTP v1/v2**, STP por VLAN (PVST), PortFast, UplinkFast, *port security* por MAC estática |
| **Capa 3** | ❌ Ninguno. Sólo `ip default-gateway` para la propia gestión |
| **Multicast** | CGMP |
| **Gestión** | Consola, **Telnet**, interfaz web (Visual Switch Manager / CMS), SNMP v1, CDP, *port monitoring* (SPAN de un puerto) |
| **Seguridad** | `enable secret`, contraseñas de línea, ACL de acceso a la gestión, *port security* estática |

---

## ⚠️ Limitaciones de este equipo

- ❌ **Sin SSH ni SNMPv3.** Sólo Telnet y web en claro. Es el equipo más expuesto del laboratorio: **mantén su gestión estrictamente en la VLAN 104 aislada**.
- ❌ **Sin RSTP ni MSTP** (sólo PVST clásico), ❌ **sin LACP**, ❌ **sin 802.1X**, ❌ **sin QoS real**.
- ❌ **Sin enrutamiento**: cualquier práctica inter-VLAN necesita un router (2620) o un switch L3 (4500G / PowerConnect).
- ⚠️ **IOS 11.2(8.11)SA6 es *interim software*** (una versión intermedia, no una release final). La última rama publicada para esta plataforma fue `12.0(5)WC17`. **No recomiendo actualizar**: con ~4 MB de flash no cabe una segunda imagen y el riesgo de dejar el switch inservible no compensa la ganancia.
- ⚠️ **Flash muy pequeña.** Confirma el espacio libre con `dir flash:` antes de tocar nada.
- ⚠️ Su `hostname` actual (`SW_servers`) es casi idéntico al del 2950 (`SW_SERVERS`). **Renómbralos** siguiendo la convención del laboratorio para evitar confusiones.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show version
dir flash:
show interfaces status
show vlan
show running-config
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md) · [📝 Bitácora](../../docs/04-bitacora.md)
