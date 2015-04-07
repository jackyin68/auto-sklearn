import unittest

from ParamSklearn.components.regression.gaussian_process import GaussianProcess
from ParamSklearn.util import _test_regressor

import sklearn.metrics


class GaussianProcessComponentTest(unittest.TestCase):
    def test_default_configuration(self):
        for i in range(10):
            # Float32 leads to numeric instabilities
            predictions, targets = _test_regressor(GaussianProcess, dataset='diabetes')
            self.assertAlmostEqual(0.2331,
                sklearn.metrics.r2_score(y_true=targets, y_pred=predictions),
                places=3)

