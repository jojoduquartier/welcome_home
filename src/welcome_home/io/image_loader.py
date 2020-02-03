from kedro.io import AbstractDataSet
import numpy as np
import cv2


class JpegData(AbstractDataSet):
    def __init__(self, filepath: str, type_: str = "jpg"):
        self._file_path = filepath
        self._type = type_

    def _load(self) -> np.ndarray:
        print("Loading: {}".format(self._file_path))
        img = cv2.imread(self._file_path)
        img = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def _save(self, array: np.ndarray) -> None:
        pass

    def _describe(self):
        return dict(file_path=self._file_path)
