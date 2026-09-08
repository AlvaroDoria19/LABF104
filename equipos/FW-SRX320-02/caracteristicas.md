# ⭐ FW-SRX320-02 — Características y protocolos

**Juniper SRX320** · Firewall de nueva generación / router de servicios con Junos. Políticas por zonas, NAT, IPsec y alta disponibilidad en clúster de 2 nodos.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **Firewall con estado y políticas por zonas**: el modelo de seguridad más didáctico que existe. Zonas + políticas + *screens* enseñan a pensar en seguridad de red, no sólo en listas de acceso.
- **NAT completo en las tres direcciones**: *source NAT* (PAT), *destination NAT* (publicar servidores) y *static NAT*. Cubre todo el temario de traducción de direcciones.
- **IPsec VPN site-to-site**, *route-based* con interfaces `st0` y *policy-based*, IKEv1 e IKEv2. Con los **dos SRX320** se monta un túnel real entre dos sedes — la práctica estrella del laboratorio.
- **Chassis Cluster de 2 nodos**: con la pareja de SRX320 se puede montar alta disponibilidad real (interfaces `reth`, *redundancy groups*, conmutación por fallo). Muy pocos laboratorios docentes pueden hacer esto.
- **Enrutamiento completo**: estático, RIP, **OSPFv2/v3**, **BGP** e **IS-IS**, además de *routing instances* (VRF). Es el equipo con más protocolos de enrutamiento del laboratorio.
- **Modo conmutador** (`ethernet-switching` con VLANs e IRB): puede hacer de switch además de firewall.
- **`show security flow session`**: ver la tabla de sesiones en vivo es la mejor herramienta pedagógica para explicar qué significa «firewall con estado».
- **Mismo Junos que los EX2300**: el alumno reutiliza toda la sintaxis aprendida en los switches.
- **2 ranuras Mini-PIM**: a diferencia del SRX300, este SRX320 admite módulos de expansión (ADSL2+/VDSL2, T1/E1, serie, LTE, WiFi). Si alguna ranura está poblada con un módulo serie, es el único firewall del laboratorio con WAN serie real además de Ethernet — confírmalo con `show chassis hardware`.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Seguridad (base, sin licencia)** | **Políticas por zonas** (`security zones` + `security policies`), *screens* anti-DoS (SYN flood, *scan*, *spoofing*), ALGs (FTP, SIP, TFTP…), tabla de sesiones con estado, registro por sesión |
| **NAT** | **Source NAT** (interfaz / *pool* / PAT), **Destination NAT**, **Static NAT**, *persistent NAT* |
| **VPN** | **IPsec** site-to-site (*route-based* con `st0` y *policy-based*), IKEv1 / IKEv2, GRE · ⚠️ AutoVPN / ADVPN según versión |
| **UTM / AppSec** (requiere licencia) | Antivirus, *web filtering*, antispam, *content filtering*, **IPS (IDP)**, AppID / AppTrack / AppFW, ATP Cloud |
| **Enrutamiento** | Estático, **RIP**, **OSPFv2 / OSPFv3**, **BGP**, **IS-IS**, *routing instances* (VRF), *filter-based forwarding* (PBR), VRRP, DHCP server / relay / cliente |
| **Capa 2** | Modo *switching* con `ethernet-switching`, VLANs, **IRB**, RSTP / MSTP, LACP · ⚠️ *transparent mode* (firewall L2) según versión |
| **IPv6** | Doble pila completa: políticas, enrutamiento y VPN sobre IPv6 · ⚠️ NAT64/NAT66 según versión |
| **Alta disponibilidad** | **Chassis Cluster** (`fab0`/`fab1`, interfaces `reth`, *redundancy groups*), *graceful restart* |
| **Monitorización** | `show security flow session`, `monitor traffic`, syslog estructurado, SNMP, captura de paquetes |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **Falta la versión de Junos de este equipo.** El `show system firmware` que capturaste sólo devuelve el BIOS del Routing Engine, no la versión del sistema operativo. **Ejecuta `show system information` y `show chassis hardware`** y rellena las tablas de la [ficha](README.md).
- ⚠️ **Confirma qué llevan las 2 ranuras Mini-PIM.** Pueden estar vacías o con un módulo instalado (ADSL/VDSL, T1/E1, serie, LTE, WiFi) — `show chassis hardware` lo dice. Si no hay ningún módulo serie, las prácticas de WAN serie de este equipo van por Ethernet; para eso usa los Cisco 2620 y 2503.
- ⚠️ **UTM, IPS y ATP requieren suscripción de pago.** Sin licencia tienes firewall, NAT, VPN y enrutamiento — más que suficiente para el temario. Comprueba qué hay con `show system license`.
- ⚠️ **El error nº 1 con los SRX**: una política de seguridad **no basta** para poder gestionar el equipo. Hace falta además `host-inbound-traffic` en la zona. Si no puedes hacer ping ni SSH al firewall, es esto.
- ⚠️ **El usuario `root` debe tener contraseña antes del primer `commit`** o el commit falla.
- ⚠️ **La imagen `.tgz` no se puede extraer del equipo.** Junos se instala descomprimido: descárgala del portal de Juniper y guárdala en el Google Drive, la PC del laboratorio y el **USB de rescate en FAT32**.
- 💡 **BIOS del Routing Engine**: tienes la **3.1** y hay disponible la **3.6**. Actualizarlo es opcional y no urgente. Si lo haces: `request system firmware upgrade re bios`, con la configuración respaldada y **sin interrumpir la alimentación**.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
show system information
show chassis hardware
show version
show system firmware
show system license
show security zones
show interfaces terse
show configuration | display set | no-more
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
