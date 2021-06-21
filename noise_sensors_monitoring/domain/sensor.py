from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Sensor:
    deviceId: str
    dbLevel: int
    connected: bool
    longitude: float
    latitude: float
    batteryLevel: int
    sigStrength: int

    @classmethod
    def from_dict(self, data: Dict):
        return self(**data)
    
    def to_dict(self):
        return asdict(self)
