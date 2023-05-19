import sys
import warnings
from typing import Any, List, ClassVar, Tuple, Set

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final

from unittest import (
    TestCase as TestCase,
)

from unittest.case import (
    SkipTest as SkipTest,
)

__all__: List[str]

def run_module_suite(file_to_run=..., argv=...): ...

class KnownFailureException(Exception): ...
class IgnoreException(Exception): ...

class clear_and_catch_warnings(warnings.catch_warnings):
    class_modules: ClassVar[Tuple[str, ...]]
    modules: Set[str]
    def __init__(self, record=..., modules=...): ...
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...

class suppress_warnings:
    log: List[warnings.WarningMessage]
    def __init__(self, forwarding_rule=...): ...
    def filter(self, category=..., message=..., module=...): ...
    def record(self, category=..., message=..., module=...): ...
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...
    def __call__(self, func): ...

verbose: int
IS_PYPY: Final[bool]
HAS_REFCOUNT: Final[bool]
HAS_LAPACK64: Final[bool]

def assert_(val, msg=...): ...
def memusage(processName=..., instance=...): ...
def jiffies(_proc_pid_stat=..., _load_time=...): ...
def build_err_msg(
    arrays,
    err_msg,
    header=...,
    verbose=...,
    names=...,
    precision=...,
): ...
def assert_equal(actual, desired, err_msg=..., verbose=...): ...
def print_assert_equal(test_string, actual, desired): ...
def assert_almost_equal(
    actual,
    desired,
    decimal=...,
    err_msg=...,
    verbose=...,
): ...
def assert_approx_equal(
    actual,
    desired,
    significant=...,
    err_msg=...,
    verbose=...,
): ...
def assert_array_compare(
    comparison,
    x,
    y,
    err_msg=...,
    verbose=...,
    header=...,
    precision=...,
    equal_nan=...,
    equal_inf=...,
): ...
def assert_array_equal(x, y, err_msg=..., verbose=...): ...
def assert_array_almost_equal(x, y, decimal=..., err_msg=..., verbose=...): ...
def assert_array_less(x, y, err_msg=..., verbose=...): ...
def runstring(astr, dict): ...
def assert_string_equal(actual, desired): ...
def rundocs(filename=..., raise_on_error=...): ...
def raises(*args): ...
def assert_raises(*args, **kwargs): ...
def assert_raises_regex(exception_class, expected_regexp, *args, **kwargs): ...
def decorate_methods(cls, decorator, testmatch=...): ...
def measure(code_str, times=..., label=...): ...
def assert_allclose(
    actual,
    desired,
    rtol=...,
    atol=...,
    equal_nan=...,
    err_msg=...,
    verbose=...,
): ...
def assert_array_almost_equal_nulp(x, y, nulp=...): ...
def assert_array_max_ulp(a, b, maxulp=..., dtype=...): ...
def assert_warns(warning_class, *args, **kwargs): ...
def assert_no_warnings(*args, **kwargs): ...
def tempdir(*args, **kwargs): ...
def temppath(*args, **kwargs): ...
def assert_no_gc_cycles(*args, **kwargs): ...
def break_cycles(): ...
def _assert_valid_refcount(op): ...
def _gen_alignment_data(dtype=..., type=..., max_size=...): ...
