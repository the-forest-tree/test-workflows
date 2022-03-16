from tests.test_connector import parameterize_equ


def pytest_addoption(parser):
    parser.addoption(
        "--allequs",
        action="store_true",
        default=False,
        help="Run iequ tests",
    )


def pytest_generate_tests(metafunc):
    m = metafunc
    if "my_param" in m.fixturenames:
        if m.config.getoption("allequs") is True:
            m.parametrize("my_param", parameterize_equ())
