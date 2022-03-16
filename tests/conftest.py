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
    if "connector_action_test_params" in m.fixturenames:
        if m.config.getoption("allequs") is True:
            m.parametrize("connector_action_test_params", parameterize_equ())
