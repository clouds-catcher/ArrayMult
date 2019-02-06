from typing import Union, Iterable, List

import numpy as np


class Logic:

    @staticmethod
    def vectors_mult(v1: List[float], v2: List[float]) \
            -> Union[Iterable, None]:

        try:
            return (np.array(v1, dtype=np.float64) *
                    np.array(v2, dtype=np.float64)).tolist()
        except:
            return None

    @staticmethod
    def vectors_dot_mult(v1: List[float], v2: List[float]) \
            -> Union[Iterable, None]:

        try:
            return np.dot(np.array(v1, dtype=np.float64),
                          np.array(v2, dtype=np.float64)
                          ).tolist()
        except:
            return None
