# ⚡ RT-MR3420-01 — Chuleta de comandos

**TP-Link TL-MR3420 (OpenWRT / LEDE)**

[🏠 Ficha del equipo](README.md) · [⭐ Características](caracteristicas.md) · [⚡ Chuleta de comandos](chuleta-comandos.md) · [🚨 Plan de contingencia](plan-contingencia.md)

---

> **Sin puerto de consola externo.** El UART está dentro de la carcasa (requiere abrirla y un
adaptador USB-TTL de 3,3 V a `115200 8N1`). El acceso normal es **SSH** y **LuCI** (web);
para recuperar la contraseña se usa el **modo failsafe** por telnet.
> Credenciales en la [ficha del equipo](README.md#-acceso).
> Para comparar la sintaxis con las otras familias de CLI del laboratorio, ve a la
> [chuleta general](../../docs/03-chuleta-comandos.md).

---

### Acceso

```text
ssh root@172.16.10.1
```

Interfaz web LuCI: `http://172.16.10.1`

### Identificación y diagnóstico

```text
ubus call system board
cat /etc/openwrt_release
uname -a
df -h
free
ip -4 addr show
ip route
brctl show
swconfig dev switch0 show
iwinfo
logread | tail -50
dmesg | tail -50
netstat -tulpn
```

> `ubus call system board` es el equivalente a `show version`: devuelve modelo, revisión, SoC y
> versión de OpenWRT de una sola vez.

### UCI: el sistema de configuración

Toda la configuración vive en `/etc/config/*` y se manipula con `uci`. **Nada se aplica hasta que
haces `uci commit` y reinicias el servicio.**

```text
uci show                        ! toda la configuración
uci show network
uci show firewall
uci show wireless
uci show dhcp
uci changes                     ! cambios pendientes de confirmar
uci commit network              ! confirmar
uci revert network              ! descartar los cambios pendientes
```

### Red e interfaces

```text
uci set network.lan.ipaddr='172.16.10.1'
uci set network.lan.netmask='255.255.255.0'
uci commit network
/etc/init.d/network restart
```

Ruta estática:

```text
uci add network route
uci set network.@route[-1].interface='lan'
uci set network.@route[-1].target='10.104.0.0'
uci set network.@route[-1].netmask='255.255.0.0'
uci set network.@route[-1].gateway='<gateway>'
uci commit network
/etc/init.d/network restart
```

### VLANs 802.1Q en el switch integrado

```text
swconfig dev switch0 show
uci show network | grep switch
```

```text
uci set network.@switch_vlan[0].vlan='10'
uci set network.@switch_vlan[0].ports='0t 1 2'
uci commit network
/etc/init.d/network restart
```

> En `ports`, el sufijo `t` marca el puerto como *tagged* (trunk) y sin sufijo es *untagged*
> (acceso). El puerto `0` suele ser el interno hacia la CPU.

### Firewall (zonas, igual que en el SRX pero con iptables)

```text
uci show firewall
/etc/init.d/firewall restart
iptables -L -v -n
iptables -t nat -L -v -n
```

Redirección de puertos (publicar un servidor):

```text
uci add firewall redirect
uci set firewall.@redirect[-1].name='WEB'
uci set firewall.@redirect[-1].src='wan'
uci set firewall.@redirect[-1].src_dport='80'
uci set firewall.@redirect[-1].dest='lan'
uci set firewall.@redirect[-1].dest_ip='10.104.1.50'
uci set firewall.@redirect[-1].dest_port='80'
uci commit firewall
/etc/init.d/firewall restart
```

### WiFi

```text
uci show wireless
wifi status
wifi down ; wifi up
iwinfo wlan0 scan
iwinfo wlan0 assoclist
```

Punto de acceso con WPA2:

```text
uci set wireless.@wifi-device[0].disabled='0'
uci set wireless.@wifi-device[0].channel='6'
uci set wireless.@wifi-iface[0].ssid='F104-LAB'
uci set wireless.@wifi-iface[0].encryption='psk2'
uci set wireless.@wifi-iface[0].key='<clave-wifi>'
uci commit wireless
wifi
```

### DHCP y DNS (dnsmasq)

```text
uci show dhcp
cat /tmp/dhcp.leases
/etc/init.d/dnsmasq restart
```

### Paquetes

```text
df -h /overlay
opkg update
opkg list-installed
opkg install <paquete>
opkg remove <paquete>
```

> ⚠️ **Comprueba `df -h /overlay` antes de instalar.** Con 4 MB de flash es muy fácil llenar el
> sistema de ficheros y dejar el router en un estado del que sólo se sale reinstalando.

### Servicios

```text
/etc/init.d/network restart
/etc/init.d/firewall restart
/etc/init.d/dnsmasq restart
/etc/init.d/uhttpd restart
reboot
```

---

[⬅️ Índice de equipos](../README.md) · [🏠 Inicio](../../README.md) · [📊 Comparativa](../../docs/01-comparativa.md) · [⚡ Chuleta general](../../docs/03-chuleta-comandos.md)
