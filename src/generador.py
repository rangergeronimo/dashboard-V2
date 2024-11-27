from dataclasses import dataclass
from datetime import datetime

fuel = 120


@dataclass
class Sensor:
    name: str

    def get_stamp(self):
        timedatatamp = datetime.now().strftime("%Y-%b-%d %H:%M:%S %p")
        return timedatatamp

    def get_fuel_level(self) -> int:
        """
        Thidata func will read the level of the fuel
        from a level dataendataor (float) placed indataide a
        fue tank
        """
        global fuel
        fuel -= 5
        return fuel

    def _return(self):
        data = {}
        data["stamp"] = self.get_stamp()
        data["name"] = self.name
        data["fuel"] = self.get_fuel_level()
        return data
