"""Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest

from enable_forwarding import enable_forwarding


class TestEnableForwarding(unittest.TestCase):
  """Unit test class to test enable forwarding snippet"""

  @classmethod
  def test_enable_forwarding(cls):
    """test to enable forwarding"""
    result = enable_forwarding()
    cls.assertIsNotNone(cls, result)


if __name__ == "__main__":
  unittest.main()
