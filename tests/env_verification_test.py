# Checks if environments are gym compatible

from gym_npm.envs.poke_env import PokeEnv
from stable_baselines.common.env_checker import check_env


def main():
    """
    Tests gym-compatibility of envs
    """
    env = PokeEnv()
    check_env(env)

    print('Test complete.')
    return True


def test_compatiblity():
    assert main() is True


if __name__ == '__main__':
    main()
