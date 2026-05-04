from hashlib import md5
from os import urandom

import pytest
from pydantic import TypeAdapter
from pydantic import ValidationError


def test_relative_path():
    from ttl_game_manifests.types_ import RelativePath

    relative_path_adapter = TypeAdapter(RelativePath)

    relative_path_adapter.validate_strings("relative/path")
    relative_path_adapter.validate_strings("./relative/path")

    with pytest.raises(ValidationError):
        relative_path_adapter.validate_strings("/absolute/path")
    with pytest.raises(ValidationError):
        relative_path_adapter.validate_strings("/absolute/path/to/file.gg")


def test_relative_dll_path():
    from ttl_game_manifests.types_ import RelativeDllPath

    relative_dll_path_adapter = TypeAdapter(RelativeDllPath)

    relative_dll_path_adapter.validate_strings("relative/path.dll")
    relative_dll_path_adapter.validate_strings("another/relative/path.dll")

    with pytest.raises(ValidationError):
        relative_dll_path_adapter.validate_strings("relative/path")
    with pytest.raises(ValidationError):
        relative_dll_path_adapter.validate_strings("relative/path.txt")


def test_relative_exe_path():
    from ttl_game_manifests.types_ import RelativeExePath

    relative_exe_path_adapter = TypeAdapter(RelativeExePath)

    relative_exe_path_adapter.validate_strings("relative/path.exe")
    relative_exe_path_adapter.validate_strings("another/relative/path.exe")

    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("relative/path")
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("relative/path.dll")


def test_relative_txt_path():
    from ttl_game_manifests.types_ import RelativeTxtPath

    relative_txt_path_adapter = TypeAdapter(RelativeTxtPath)

    relative_txt_path_adapter.validate_strings("relative/path.txt")
    relative_txt_path_adapter.validate_strings("another/relative/path.txt")

    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_strings("relative/path")
    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_strings("relative/path.dll")


def test_file_name():
    from ttl_game_manifests.types_ import FileName

    file_name_adapter = TypeAdapter(FileName)

    file_name_adapter.validate_strings("file.gg")
    file_name_adapter.validate_strings("name_only")

    with pytest.raises(ValidationError):
        file_name_adapter.validate_strings("relative/path/to/file.gg")
    with pytest.raises(ValidationError):
        file_name_adapter.validate_strings("/absolute/path/to/file.gg")


def test_json_file_name():
    from ttl_game_manifests.types_ import JsonFileName

    json_file_name_adapter = TypeAdapter(JsonFileName)

    json_file_name_adapter.validate_strings("file.json")
    json_file_name_adapter.validate_strings("name with spaces.json")

    with pytest.raises(ValidationError):
        json_file_name_adapter.validate_strings("relative/path/to/file.json")
    with pytest.raises(ValidationError):
        json_file_name_adapter.validate_strings("/absolute/path/to/file.json")


def test_icon_url():
    from ttl_game_manifests.types_ import IconUrl

    icon_url_adapter = TypeAdapter(IconUrl)

    icon_url_adapter.validate_strings("https://example.com/icon.ico")
    icon_url_adapter.validate_strings("https://example.com/icon.png")

    with pytest.raises(ValidationError):
        icon_url_adapter.validate_strings("relative/path/to/icon.png")
    with pytest.raises(ValidationError):
        icon_url_adapter.validate_strings("https://example.com/icon.jpg")


def test_background_url():
    from ttl_game_manifests.types_ import BackgroundUrl

    background_url_adapter = TypeAdapter(BackgroundUrl)

    background_url_adapter.validate_strings("https://example.com/background.jpg")
    background_url_adapter.validate_strings("https://example.com/background.png")
    background_url_adapter.validate_strings("https://example.com/background.webp")

    with pytest.raises(ValidationError):
        background_url_adapter.validate_strings("relative/path/to/background.png")
    with pytest.raises(ValidationError):
        background_url_adapter.validate_strings("https://example.com/background.gif")
    with pytest.raises(ValidationError):
        background_url_adapter.validate_strings("https://example.com/background.webm")


def test_live_background_url():
    from ttl_game_manifests.types_ import LiveBackgroundUrl

    live_background_url_adapter = TypeAdapter(LiveBackgroundUrl)

    live_background_url_adapter.validate_strings("https://example.com/live_background.mp4")
    live_background_url_adapter.validate_strings("https://example.com/live_background.webm")

    with pytest.raises(ValidationError):
        live_background_url_adapter.validate_strings("relative/path/to/live_background.mp4")
    with pytest.raises(ValidationError):
        live_background_url_adapter.validate_strings("https://example.com/live_background.gif")


def test_json_url():
    from ttl_game_manifests.types_ import JsonUrl

    json_url_adapter = TypeAdapter(JsonUrl)

    json_url_adapter.validate_strings("https://example.com/data.json")

    with pytest.raises(ValidationError):
        json_url_adapter.validate_strings("relative/path/to/data.json")
    with pytest.raises(ValidationError):
        json_url_adapter.validate_strings("https://example.com/data.jsonp")
    with pytest.raises(ValidationError):
        json_url_adapter.validate_strings("https://example.json")


def test_hex_md5():
    from ttl_game_manifests.types_ import HexMd5

    hex_md5_adapter = TypeAdapter(HexMd5)

    data1 = urandom(256)
    hash1 = md5(data1, usedforsecurity=False)
    hex_md5_adapter.validate_strings(hash1.hexdigest())

    data2 = urandom(256)
    hash2 = md5(data2, usedforsecurity=False)
    hex_md5_adapter.validate_strings(hash2.hexdigest())

    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_strings("invalid_hex_string")
    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_strings("a" * 33)


def test_metadata_version():
    from ttl_game_manifests.types_ import MetadataVersion

    metadata_version_adapter = TypeAdapter(MetadataVersion)

    metadata_version_adapter.validate_strings("420")
    metadata_version_adapter.validate_strings("1.2.3.4")

    with pytest.raises(ValidationError):
        metadata_version_adapter.validate_strings("1.0")
    with pytest.raises(ValidationError):
        metadata_version_adapter.validate_strings("1.0.0.")


def test_proton_version():
    from ttl_game_manifests.types_ import ProtonVersion

    proton_version_adapter = TypeAdapter(ProtonVersion)

    proton_version_adapter.validate_strings("10.26-proton-ge")
    proton_version_adapter.validate_strings("10.0-20251222-proton-cachyos")

    with pytest.raises(ValidationError):
        proton_version_adapter.validate_strings("1.2.3")
    with pytest.raises(ValidationError):
        proton_version_adapter.validate_strings("10.26-wine-ge")
