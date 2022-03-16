from tests.test_connector import parameterize_equ


def pytest_addoption(parser):
    parser.addoption(
        "--allequs",
        action="store_true",
        default=False,
        help="Run iequ tests",
    )


def pytest_generate_tests(metafunc):
    if "connector_action_test_params" in metafunc.fixturenames:
        if metafunc.config.getoption("allequs") is True:
            metafunc.parametrize(
                "connector_action_test_params",
                parameterize_equ()
            )
