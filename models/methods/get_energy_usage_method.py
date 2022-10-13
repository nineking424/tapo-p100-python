from models.methods import method
from typing import Any


class GetEnergyUsageMethod(method.Method):
    def __init__(self, params: Any):
        super().__init__("get_energy_usage", params)
