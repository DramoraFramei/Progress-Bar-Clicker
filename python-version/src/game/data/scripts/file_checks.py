# pylint: disable=line-too-long

import json
import os

from ...app.imports import (
    TIMESTAMP,
    SLOTS_FILES_NAME,
)


class FILE_CHECKS:
    """
    File checks
    """


class _FileCheckResult:
    """Result of file check with .bool() method."""

    def __init__(self, found: bool | bool = False):
        """
        Initialize the file check result
        """
        self._found = bool(found)

    def bool(self):
        """Return the result of the file check."""
        return self._found


def file_check(slot_folders: list, slot_names: list):
    """
    Check if save files exist in slot folders. Returns object with .bool().
    """
    # Check if the slot folders and slot names are lists
    if not isinstance(slot_folders, list):
        raise ValueError("slot_folders must be a list")
    if not isinstance(slot_names, list):
        raise ValueError("slot_names must be a list")
    # Check if the slot folders and slot names are lists
    for slot_folder in slot_folders:
        if not os.path.exists(slot_folder):
            return _FileCheckResult(found=False)
    for slot_name in slot_names:
        if not os.path.exists(SLOTS_FILES_NAME.format(slot_name=slot_name, TIMESTAMP=TIMESTAMP)):
            return _FileCheckResult(found=False)
    return _FileCheckResult(found=True)
