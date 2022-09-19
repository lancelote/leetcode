from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class File:
    name: str
    content: str

    @classmethod
    def from_text(cls, text: str) -> File:
        match = re.match(r"(.+)\((.*)\)", text)
        if match is None:
            raise ValueError(f"cannot parse {text}")
        name, content = match.groups()
        return File(name, content)


@dataclass
class DirInfo:
    path: str
    files: list[File]

    @classmethod
    def from_text(cls, text: str) -> DirInfo:
        path, *sub_paths = text.split(" ")
        files = [File.from_text(x) for x in sub_paths]
        return DirInfo(path, files)


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        contents = defaultdict(list)
        dir_infos = (DirInfo.from_text(path) for path in paths)

        for dir_info in dir_infos:
            for file in dir_info.files:
                contents[file.content].append(f"{dir_info.path}/{file.name}")

        return [files for files in contents.values() if len(files) > 1]
