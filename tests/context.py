# -*- coding: utf-8 -*-

import sys
import mock

sys.modules['nonexistent_lib_1'] = mock.Mock()
sys.modules['nonexistent_lib_2'] = mock.Mock()
sys.modules['nonexistent_lib_3'] = mock.Mock()
sys.modules['nonexistent_lib_4'] = mock.Mock()