from dataclasses import dataclass
from pathlib import Path
from re import match
from shutil import copytree

from modules.action import Action
from modules.settings import get_library_folder
from PyQt5.QtCore import pyqtSignal


def install_template(dist: Path):
    library_folder = Path(get_library_folder())
    template = library_folder / "template"

    template.mkdir(exist_ok=True)

    for directory in dist.iterdir():
        if match(r"\d+\.\d+.*", directory.name) is not None:
            copytree(
                src=template.as_posix(),
                dst=directory.as_posix(),
                dirs_exist_ok=True,
            )
            return


@dataclass(frozen=True)
class TemplateAction(Action):
    destination: Path

    finished = pyqtSignal()

    def run(self):
        install_template(self.destination)
        self.finished.emit()
