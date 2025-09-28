from pytest import fixture
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.test.config import Config

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        help='Test execution environment [dev,qa]'
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg