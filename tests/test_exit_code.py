import pytest

from pytest_exit_code import ExitCode


@pytest.mark.parametrize(
    "keyword,expected",
    [
        ("test_pass", ExitCode.TESTS_PASSED),
        ("test_fail", ExitCode.TESTS_FAILED),
        ("test_error", ExitCode.TESTS_ERRORED),
        ("test_skip", ExitCode.TESTS_SKIPPED),
        (
            "",
            ExitCode.TESTS_PASSED
            | ExitCode.TESTS_FAILED
            | ExitCode.TESTS_ERRORED
            | ExitCode.TESTS_SKIPPED,
        ),
    ],
)
def test_correct_exit_codes(
    pytester,
    keyword: str,
    expected: ExitCode,
) -> None:
    pytester.makepyfile(
        """
        import pytest

        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2

        @pytest.fixture
        def failing_fixture():
            raise RuntimeError("Failure in fixture")

        def test_error(failing_fixture):
            assert 1 == 1

        @pytest.mark.skip
        def test_skip():
            assert 1 == 1
    """
    )

    result = pytester.runpytest("-k", keyword)
    assert result.ret == expected
