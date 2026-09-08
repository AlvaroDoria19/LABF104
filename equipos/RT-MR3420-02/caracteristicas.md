# ⭐ RT-MR3420-02 — Características y protocolos

**TP-Link TL-MR3420 (OpenWRT / LEDE)** · Router inalámbrico con OpenWRT/LEDE. Los únicos equipos con WiFi del laboratorio y el único router Linux: enseña por dentro lo que los Cisco y Juniper hacen por CLI propietaria.

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

## ⭐ Características destacadas

- **Los únicos equipos inalámbricos del laboratorio.** Ningún switch, router ni firewall del F104 tiene radio: estos dos routers son los que permiten prácticas de **WiFi 802.11n, WPA2, selección de canal, modo AP / cliente / WDS y portal cautivo**.
- **El único router Linux.** OpenWRT deja ver lo que hay debajo de la abstracción de un router comercial: interfaces, tabla de rutas, `iptables`/netfilter, `dnsmasq`. Puesto al lado del Cisco 2620 y del SRX320 haciendo el mismo NAT, la comparación es inmejorable didácticamente.
- **Configuración como texto plano** en `/etc/config/*`: se puede versionar en Git, difundir por `scp` y comparar con `diff`. Muy útil para que el alumno vea la configuración como código.
- **VLANs 802.1Q con `swconfig`** en el switch integrado: etiquetado real en un equipo de gama doméstica.
- **Puerto USB para módem 3G/4G** → prácticas de conmutación por fallo hacia red móvil, algo imposible con el resto del inventario.
- **`opkg`** permite añadir funciones (OpenVPN, WireGuard, SQM, snmpd)… siempre que quepan en los 4 MB de flash.
- Coste casi nulo: son el equipo ideal para que los alumnos experimenten sin miedo a estropear material caro.

---

## 🌐 Protocolos y funciones soportadas

| Área | Soporte |
|---|---|
| **Capa 2** | 802.1Q VLAN mediante `swconfig`, *bridging*, STP opcional en el puente, 802.11 b/g/n, WDS, `relayd` (puente en capa 3) |
| **Capa 3** | Rutas estáticas, *policy routing* con `ip rule` · ⚠️ **RIP / OSPF / BGP sólo instalando `quagga` o `bird`**, y con 4 MB de flash es muy poco probable que quepan |
| **Servicios** | **dnsmasq** (DHCP + DNS + TFTP), `odhcpd`, DHCPv6-PD y anuncios RA, NAT/PAT, redirección de puertos, DMZ, DDNS, NTP |
| **Firewall** | **iptables / netfilter** gestionado por `fw3` con **zonas**, reglas, redirecciones y SNAT/DNAT — el mismo modelo de zonas del SRX320 pero en Linux |
| **IPv6** | Doble pila completa: RA, DHCPv6, prefijo delegado, reglas de firewall IPv6 |
| **Inalámbrico** | `hostapd` (AP con WPA/WPA2-PSK y **WPA2-Enterprise contra RADIUS**), `wpa_supplicant` (cliente), múltiples SSID, aislamiento de clientes, 802.11s *mesh* |
| **VPN** | ⚠️ OpenVPN, WireGuard o strongSwan mediante `opkg` — **sujeto al espacio libre en flash** |
| **QoS** | ⚠️ SQM (`fq_codel`, `cake`) mediante `opkg` |
| **Gestión** | **SSH** (dropbear), **LuCI** por HTTP/HTTPS (`uhttpd`), CLI con **UCI**, syslog (`logread`), ⚠️ SNMP con `opkg` |

---

## ⚠️ Limitaciones de este equipo

- ⚠️ **4 MB de flash y 32 MB de RAM.** Es la limitación que define este equipo: apenas queda espacio para paquetes. Comprueba el espacio real antes de instalar nada con `df -h /overlay`. OpenVPN, quagga o SQM pueden simplemente no caber.
- ⚠️ **Software fuera de soporte.** LEDE 17.01 dejó de recibir parches en 2019 y OpenWRT abandonó los equipos de 4/32 MB desde la 19.07. **No hay actualizaciones de seguridad**: mantén estos routers en la red del laboratorio y **nunca expuestos a internet**.
- ⚠️ **Revisión de hardware sin confirmar.** El firmware debe coincidir **exactamente** con la revisión del equipo: instalar el de otra revisión lo deja inservible. Confírmala con `ubus call system board` antes de tocar el firmware.
- ❌ **Sin puerto de consola accesible.** Si el TFTP de U-Boot no funciona, la única vía es abrir la carcasa y soldar/conectar un adaptador USB-TTL al UART. Es el equipo con el rescate más incómodo del laboratorio, aunque también el más barato de reemplazar.
- ⚠️ **Enrutamiento dinámico poco realista** por el espacio en flash: para OSPF y BGP usa los Cisco 2620 o el SRX320.
- ⚠️ **Direccionamiento fuera de la VLAN de gestión.** Estos dos routers no están en `192.168.104.0/24` como el resto del inventario.

---

## ✅ Comandos de verificación

Ejecútalos para rellenar los datos marcados con ⚠️ en la [ficha del equipo](README.md):

```text
ubus call system board
cat /etc/openwrt_release
uname -a
df -h
free
ip -4 addr show
ip route
swconfig dev switch0 show
iwinfo
logread | tail -30
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
