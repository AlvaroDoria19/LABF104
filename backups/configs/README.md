# 💾 Respaldos de configuración

Un fichero por equipo y fecha. Convención de nombre:

```text
<ID-equipo>_<AAAA-MM-DD>.cfg        respaldo puntual
<ID-equipo>_base.cfg                configuración base a restaurar tras cada práctica
```

Ejemplos: `SW-C2950-01_2026-09-06.cfg` · `RT-C2620-01_base.cfg` · `FW-SRX300-01_base.conf`

> Los respaldos **sí** se versionan en Git: son texto y su histórico es justamente lo que interesa.
> Revisa antes de hacer commit que no contengan contraseñas en claro
> (`enable password`, `password simple`, claves pre-compartidas de IPsec).

Buscar contraseñas en claro antes del commit:

```bash
grep -riE "password|pre-shared-key|secret" backups/configs/ | grep -v "secret 5"
```
