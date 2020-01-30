from kedro.io import AbstractDataSet
from .image_loader import JpegData
import numpy as np
import pathlib
import typing


class MyOwnDataSet(AbstractDataSet):
    def __init__(self, filepath: str, type_: str = "jpg"):
        self._file_path = filepath
        self._type = type_

    def _load(self) -> typing.Tuple[np.ndarray, ...]:
        return tuple(JpegData(str(file)).load() for file in pathlib.Path(self._file_path).glob('*.jpg'))

    def _save(self, arrays: typing.Tuple[np.ndarray, ...]) -> None:
        pass

    def _describe(self):
        return dict(folder=self._file_path, type_=self._type)
