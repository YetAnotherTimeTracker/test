import os


def test_env_var():
    assert os.environ['BOT_ENV'] == 'development'