from enum import StrEnum


class DownloadMode(StrEnum):
    FILE = "DOWNLOAD_MODE_FILE"
    CHUNK = "DOWNLOAD_MODE_CHUNK"
    RAW = "DOWNLOAD_MODE_RAW"
    MULTIFILE = "DOWNLOAD_MODE_MULTIFILE"
