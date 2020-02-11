from kedro.io import AbstractDataSet
from PIL import Image
import numpy as np


class JpegData(AbstractDataSet):
    def __init__(self, filepath: str, type_: str = "jpg"):
        self._file_path = filepath
        self._type = type_

    def _load(self) -> np.ndarray:
        print("Loading: {}".format(self._file_path))
        img = Image.open(self._file_path)
        img = img.convert("L")
        img = img.resize((100, 100), Image.ANTIALIAS)
        return np.array(img)

    def _save(self, array: np.ndarray) -> None:
        pass

    def _describe(self):
        return dict(file_path=self._file_path)
