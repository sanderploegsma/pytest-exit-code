from enum import IntFlag


class ExitCode(IntFlag):
    TESTS_PASSED = 0
    TESTS_FAILED = 1
    TESTS_ERRORED = 2
    TESTS_SKIPPED = 4
