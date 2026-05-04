from enum import StrEnum


class DiffType(StrEnum):
    HDIFF = "hdiff"
    HGDIFF = "hgdiff"
    LDIFF = "ldiff"
    KRDIFF = "krdiff"
