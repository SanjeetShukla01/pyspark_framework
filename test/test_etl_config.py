import unittest

from src.config.etl_config import aa_params
from src.utils.common import DotDict


class TestEtlConfig(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        print(aa_params)
        print(aa_params.paths)
        print(aa_params.paths["log_path"])
        print(DotDict(aa_params.paths).log_path)
        # Nested Dict
        print(aa_params)
        print(aa_params.get('paths.log_path'))


if __name__ == '__main__':
    unittest.main()
