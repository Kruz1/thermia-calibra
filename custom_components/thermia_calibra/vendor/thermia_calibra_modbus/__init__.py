"""Thermia Calibra / Genesis Modbus device library."""

from .device import ThermiaCalibra, UpdateReport
from .register_catalog import REGISTER_CATALOG, RegisterDefinition
from .readings import (
    GenesisCoils,
    GenesisDiscreteInputs,
    GenesisHoldingRegisters,
    GenesisHotWaterRegisters,
    GenesisInputRegisters,
    GenesisRoomSensorRegisters,
)

__all__ = [
    "GenesisCoils",
    "GenesisDiscreteInputs",
    "GenesisHoldingRegisters",
    "GenesisHotWaterRegisters",
    "GenesisInputRegisters",
    "GenesisRoomSensorRegisters",
    "REGISTER_CATALOG",
    "RegisterDefinition",
    "ThermiaCalibra",
    "UpdateReport",
]
