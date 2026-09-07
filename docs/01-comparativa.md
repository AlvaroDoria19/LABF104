# 📊 Comparativa del Laboratorio F104

[⬅️ Volver al inicio](../README.md) · [📇 Equipos](../equipos/README.md)

> Vista de conjunto de los 19 equipos.
> **El detalle de cada chasis está en su carpeta:** [`equipos/`](../equipos/README.md)

---

## Tabla general

| Equipo | Cant. | Capa | Puertos | SO instalado | SSH | STP | Enrutamiento dinámico | 802.1X |
|---|:--:|:--:|---|---|:--:|---|---|:--:|
| **3Com 4500G 24-Port** | 2 | L2/L3 | 24 GbE + 4 SFP | 3Com OS V5.01.03s56 | ✅ | MSTP | RIP, OSPFv2 | ✅ |
| **3Com 4210 26-Port** | 2 | L2 | 24 FE + 2 uplinks | ⚠️ pendiente | ⚠️ | MSTP | ❌ | ✅ |
| **Catalyst WS-C2924-XL-EN** | 1 | L2 | 24 FE | IOS 11.2(8.11)SA6 | ❌ | PVST | ❌ | ❌ |
| **Catalyst WS-C2950-24** | 1 | L2 | 24 FE | IOS 12.1(22)EA13 **SI** | ❌ | RSTP/MSTP | ❌ | ✅ |
| **Cisco 2503** #1 | 1 | L3 | 1 AUI + 2 serie + BRI | IOS 11.2(17) **Enterprise** | ❌ | — | RIP, EIGRP, OSPF, BGP | — |
| **Cisco 2503** #2 | 1 | L3 | 1 AUI + 2 serie + BRI | IOS 11.1(17) `INR` | ❌ | — | RIP, EIGRP, OSPF, BGP | — |
| **Cisco 2620** | 2 | L3 | 1 FE + serie múltiple | IOS 12.2(27) **IP Plus** | ❌ | — | RIP, EIGRP, OSPF, BGP, IS-IS | — |
| **Dell PowerConnect 7024** | 3 | L2/L3 | 24 GbE + 4 SFP | ⚠️ pendiente | ✅ | MSTP/PVSTP+ | RIP, OSPFv2/v3 | ✅ |
| **Juniper EX2300-24T** | 2 | L2/L3 | 24 GbE + 4 SFP+ | Junos 18.1R3.3 | ✅ | RSTP/MSTP/VSTP | Estático, RIP, OSPF⚠️ | ✅ |
| **Juniper SRX300** | 2 | L3–L7 | 6 GbE + 2 SFP | ⚠️ pendiente | ✅ | RSTP/MSTP | RIP, OSPF, BGP, IS-IS | — |
| **TP-Link TL-MR3420** | 2 | L3 + WiFi | 4 LAN + 1 WAN + USB | LEDE 17.01 `git-19.167…` | ✅ | STP opcional | Sólo estático ⚠️ | ✅ (WPA2-Ent.) |

⚠️ Ver [datos pendientes](#-datos-pendientes-de-capturar) al final. El detalle de cada chasis está
en su carpeta: [`equipos/`](../equipos/README.md)

---

## Memoria y almacenamiento

Determina qué se puede actualizar y qué no. Es el dato que más condiciona el plan de contingencia.

| Equipo | DRAM | Flash | Flash libre | ¿Cabe una 2ª imagen? |
|---|---|---|---|:--:|
| 3Com 4500G | 128 MB | 16 MB | ⚠️ pendiente | ✅ Probablemente |
| 3Com 4210 | ⚠️ pendiente | ⚠️ pendiente | ⚠️ pendiente | ⚠️ |
| Catalyst 2924-XL-EN | 8 MB | ⚠️ ≈ 4 MB | ⚠️ pendiente | ❌ Casi seguro que no |
| Catalyst 2950-24 | ≈ 20 MB | ⚠️ ≈ 8 MB | ⚠️ pendiente | ✅ Posiblemente |
| Cisco 2503 #1 | ⚠️ **4 MB** | 8 MB | **396 KB** | ❌ **No** |
| Cisco 2503 #2 | 16 MB | 8 MB | ⚠️ pendiente | ❌ Improbable |
| Cisco 2620 #1 | 64 MB | 16 MB | **6,4 MB** | ✅ **Sí** |
| Cisco 2620 #2 | 64 MB | 16 MB | ⚠️ pendiente | ✅ Probablemente |
| Dell PC7024 | — | — | — | ✅ **Doble imagen nativa** |
| Juniper EX2300 | — | ⚠️ reducida | ⚠️ pendiente | ✅ *snapshot* en partición alterna |
| Juniper SRX300 | — | — | — | ✅ *snapshot* en partición alterna |
| TP-Link TL-MR3420 | ⚠️ 32 MB | ⚠️ **4 MB** | ⚠️ `df -h /overlay` | ❌ **No** (apenas caben paquetes) |

> [!IMPORTANT]
> **Los tres equipos con riesgo real son el Catalyst 2924-XL, el Cisco 2503 #1 y el 3Com 4210.**
> En ellos no cabe una segunda imagen: cualquier cambio de OS obliga a borrar la actual primero.
> No toques su software sin la imagen respaldada, verificada y la consola conectada.

---

## Riesgo de pérdida de imagen

Ordenado por prioridad de respaldo. **Los EOL sin distribución son los irreemplazables.**

| Prioridad | Equipo | Imagen | ¿Se puede sacar del equipo? | ¿Se puede volver a descargar? |
|:--:|---|---|:--:|:--:|
| 🔴 1 | 3Com 4500G | ⚠️ nombre pendiente | ✅ FTP/TFTP | ❌ 3Com ya no existe |
| 🔴 1 | 3Com 4210 | ⚠️ pendiente | ✅ FTP/TFTP | ❌ 3Com ya no existe |
| 🔴 1 | Cisco 2503 #1 | `c2500-j-l_112-17.bin` | ✅ TFTP/FTP † | ❌ EOL sin distribución |
| 🔴 1 | Cisco 2503 #2 | `igs-inr-l.111-17` | ✅ TFTP/FTP † | ❌ EOL sin distribución |
| 🟠 2 | Catalyst 2924-XL | `c2900xl-hs-mz-112.8.11-SA6.bin` | ✅ TFTP | ❌ EOL sin distribución |
| 🟠 2 | Catalyst 2950 | `c2950-i6q4l2-mz.121-22.EA13.bin` | ✅ FTP/TFTP | ❌ EOL sin distribución |
| 🟠 2 | Cisco 2620 | `c2600-is-mz.122-27.bin` | ✅ FTP/TFTP | ❌ EOL sin distribución |
| 🟡 3 | Dell PC7024 | `.stk` ⚠️ | ⚠️ Probablemente no | ⚠️ Soporte de Dell |
| 🟡 3 | Juniper EX2300 | `junos-arm-32-18.1R3.3.tgz` | ❌ No | ✅ Portal de Juniper (con cuenta) |
| 🟡 3 | Juniper SRX300 | ⚠️ pendiente | ❌ No | ✅ Portal de Juniper (con cuenta) |
| 🟢 4 | TP-Link TL-MR3420 | `lede-17.01.7-…-tl-mr3420-v1-…bin` | ❌ No | ✅ Archivo de descargas de OpenWRT |

† Los dos Cisco 2503 **necesitan el transceptor AUI→RJ-45** para tener LAN, o bien sacar la imagen
por `Serial0` usando un Cisco 2620 como pasarela.

---

## Para qué usar cada equipo

| Práctica | Equipo recomendado | Por qué |
|---|---|---|
| VLAN, VTP y STP clásico | Catalyst 2924-XL | PVST puro: se ve la convergencia lenta |
| RSTP, EtherChannel, port security, 802.1X | **Catalyst 2950** | El más completo en L2 de los Cisco |
| Enrutamiento inter-VLAN sin router | 3Com 4500G · Dell PC7024 | Switches L3 con OSPF y VRRP |
| OSPF, BGP, NAT, ACL, router-on-a-stick | **Cisco 2620** | 64 MB de RAM e IOS IP Plus |
| WAN serie: HDLC, PPP, Frame Relay | Cisco 2620 · Cisco 2503 | Puertos serie reales, no simulados |
| ISDN / DDR | Cisco 2503 | BRI integrada |
| Multiprotocolo (IPX, AppleTalk, DECnet) | **Cisco 2503 #1** | Único con IOS Enterprise |
| Apilamiento y multicast (PIM) | Dell PowerConnect 7024 | Hasta 12 unidades y PIM-DM/SM |
| Junos, `commit confirmed`, `rollback` | **Juniper EX2300** | Modelo de configuración transaccional |
| Virtual Chassis | Juniper EX2300 (los 2) | Dos switches gestionados como uno |
| Firewall por zonas, NAT, IPsec | **Juniper SRX300** (los 2) | Túnel real entre las dos unidades |
| Alta disponibilidad | Juniper SRX300 (los 2) | Chassis Cluster de 2 nodos |
| **WiFi: 802.11n, WPA2, AP/cliente, WDS** | **TP-Link TL-MR3420** (los 2) | Los **únicos equipos con radio** del laboratorio |
| Router Linux: iptables, dnsmasq, UCI | TP-Link TL-MR3420 | Deja ver por dentro lo que hacen los Cisco y Juniper |
| Conmutación por fallo a red móvil | TP-Link TL-MR3420 | Puerto USB para módem 3G/4G |
| Comparar 5 sintaxis de CLI | 2950 + 4500G + PC7024 + EX2300 + MR3420 | IOS vs Comware vs Dell vs Junos vs Linux/UCI |

---

## ⚠️ Avisos transversales del laboratorio

> [!WARNING]
> **Ningún equipo Cisco del laboratorio tiene SSH.** Confirmado con `show version`:
> - Catalyst 2950 → `Running Standard Image` (sin criptografía)
> - Cisco 2620 → imagen `C2600-IS-M` (IP Plus, sin `k9`)
> - Catalyst 2924-XL y Cisco 2503 → plataformas sin soporte de criptografía
>
> Todo el acceso remoto a los Cisco es **Telnet en claro**. Mantén su gestión estrictamente en la
> VLAN 104 aislada y protégela con ACL. Los 3Com, Dell y Juniper sí tienen SSH: úsalo en ellos.

**Hostnames a corregir.** Varios equipos comparten o repiten nombre, lo que hace muy fácil
configurar el equipo equivocado:

| Equipo | Hostname actual | Recomendado |
|---|---|---|
| `SW-C2900XL-01` | `SW_servers` | `F104-SW-2924XL-01` |
| `SW-C2950-01` | `SW_SERVERS` | `F104-SW-2950-01` |
| `RT-C2503-01` | `Router` | `F104-RT-2503-01` |
| `RT-C2503-02` | `Router` | `F104-RT-2503-02` |
| `SW-PC7024-01…03` | `L3Switch` (los 3) | `F104-SW-PC7024-01…03` |
| `SW-EX2300-01/02` | `SW-LAB1` / `SW-LAB2` | `F104-SW-EX2300-01/02` |

**Los dos Cisco 2503 no son gemelos.** Mismo hardware, software distinto:

| | `RT-C2503-01` | `RT-C2503-02` |
|---|---|---|
| IOS | 11.2(17) **Enterprise** | 11.1(17) `INR` |
| DRAM | **4 MB** | 16 MB |
| NAT | ✅ (llegó en 11.2) | ❌ |
| IPX / AppleTalk / DECnet | ✅ Todos | Sólo IPX |
| Flash libre | 396 KB | ⚠️ pendiente |

No asumas que una práctica que funciona en uno funciona en el otro.

**Conflicto de direccionamiento a resolver.** `RT-MR3420-02` está en `192.168.1.1`, que es a la vez
la dirección por defecto de OpenWRT **y** la del SRX300 con configuración de fábrica. Si ambos
equipos se conectan a la misma red hay conflicto de IP. Además, los dos TP-Link están fuera del
esquema `192.168.104.0/24` de gestión.

**Software fuera de soporte en los TP-Link.** LEDE 17.01 dejó de recibir parches en 2019 y OpenWRT
abandonó los equipos de 4/32 MB desde la 19.07. Funcionan bien para el laboratorio, pero **no deben
exponerse a internet**.

**Los dos Cisco 2620 tampoco están igual poblados:** el #1 reporta **10** puertos serie de baja
velocidad y el #2 sólo **6**. Confírmalo con `show diag` antes de repartir las prácticas.

---

## 📋 Datos pendientes de capturar

| Equipo(s) | Qué falta | Comando |
|---|---|---|
| `SW-3C4210-01/02` | **Todo**: versión, imagen, memoria, nº de serie | `display version` · `dir flash:/` |
| `SW-PC7024-01…03` | Versión de firmware, nombre del `.stk` y nº de serie | `show version` |
| `FW-SRX300-01/02` | **Versión de Junos** y nº de serie | `show system information` · `show chassis hardware` |
| `SW-3C4500G-01/02` | Nombre del fichero `.bin` y nº de serie | `dir flash:/` · `display device manuinfo` |
| `SW-C2900XL-01` · `SW-C2950-01` | Tamaño y espacio libre de flash | `dir flash:` |
| `RT-C2620-02` | Nombre exacto de la imagen y flash libre | `show flash:` |
| `RT-MR3420-01/02` | **Revisión de hardware** (v1/v2/v5) y espacio libre en flash | `ubus call system board` · `df -h /overlay` |
| `SW-EX2300-01/02` | Nº de serie y licencias instaladas | `show chassis hardware` · `show system license` |
| Todos | Ubicación física (rack / posición) | — |


---

[⬅️ Volver al inicio](../README.md) · [📇 Equipos](../equipos/README.md) · [🚨 Contingencia](02-plan-contingencia.md) · [⚡ Chuleta](03-chuleta-comandos.md) · [📝 Bitácora](04-bitacora.md)
