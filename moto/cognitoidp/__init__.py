from __future__ import unicode_literals
from .models import cognitoidp_backends
from ..core.models import base_decorator

mock_cognitoidp = base_decorator(cognitoidp_backends)
