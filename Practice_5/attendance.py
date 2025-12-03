"""
Öğrenci Devamsızlık Takibi
"""
from typing import Dict, Set

attendance: Dict[str, Set[str]] = {}


def mark_absent(student_id: str, date: str):
    attendance.setdefault(student_id, set()).add(date)


def get_absences(student_id: str):
    return sorted(attendance.get(student_id, set()))


def absences_on(date: str):
    return [sid for sid, dates in attendance.items() if date in dates]


if __name__ == '__main__':
    print('Devamsızlık demo: örnek kayıtlar')
    mark_absent('S001','2025-12-01')
    mark_absent('S002','2025-12-01')
    mark_absent('S001','2025-12-02')
    print('S001 devamsızlıklar:', get_absences('S001'))
    print('2025-12-01 tarihinde devamsız olanlar:', absences_on('2025-12-01'))
