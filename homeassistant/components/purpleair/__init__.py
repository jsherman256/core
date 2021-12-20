"""The purpleair integration."""
from __future__ import annotations

from purpleair.sensor import Sensor

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

PLATFORMS: list[str] = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up purpleair from a config entry."""
    # TODO Store an API object for your platforms to access
    from pprint import pprint

    pprint(hass.data.keys())
    hass.data[DOMAIN][entry.entry_id] = await hass.async_add_executor_job(Sensor, 4575)

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
