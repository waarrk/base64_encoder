# SPDX-FileCopyrightText: 2025 Yusaku Washio <s22c1704za@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import base64
from typing import Union

def encode(data: Union[str, bytes]) -> str:
	data_bytes = data.encode('utf-8') if isinstance(data, str) else data
	return base64.b64encode(data_bytes).decode('ascii')

__all__ = [
	'encode',
]