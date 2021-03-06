import numpy as np
import numpy.linalg as la
from pak.evaluation import MOTM

def evaluate(Gt, Hy, threshold):
    """ Ground-truth vs hypothesis for the
        Multiple Object Tracking Precision

        Gt: [
            (frame, pid, x, y)
        ]

        Hy: [
            (frame, pid, x, y)
        ]

        threshold: after which no correspondence is possible
    """
    cost_fun = lambda a, b: la.norm(a-b)
    fp, m, mme, c, d, g = MOTM.evaluate(Gt, Hy, threshold, cost_fun)

    D = np.sum(d)
    C = np.sum(c)
    return D/C
