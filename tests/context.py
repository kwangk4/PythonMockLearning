# -*- coding: utf-8 -*-

import sys
import mock

sys.modules['unexisted_lib_1'] = mock.Mock()
sys.modules['unexisted_lib_2'] = mock.Mock()
sys.modules['unexisted_lib_3'] = mock.Mock()
sys.modules['unexisted_lib_4'] = mock.Mock()