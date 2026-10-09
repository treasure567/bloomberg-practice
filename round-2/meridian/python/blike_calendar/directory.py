from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .models import BusinessTier


@dataclass
class Employee:
    employee_id: str
    organization: str
    default_tier: BusinessTier


class EmployeeDirectory:
    """Lookup of employees and their default business tier."""

    def __init__(self) -> None:
        self._employees: Dict[str, Employee] = {}

    def add(self, employee_id: str, organization: str, default_tier: BusinessTier) -> None:
        self._employees[employee_id] = Employee(employee_id, organization, default_tier)

    def get(self, employee_id: str) -> Employee:
        if employee_id not in self._employees:
            raise KeyError(employee_id)
        return self._employees[employee_id]

    def tier_for(self, employee_id: str) -> BusinessTier:
        return self._employees[employee_id].default_tier
