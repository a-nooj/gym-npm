# Basic package test

import gym
import gym_npm


def main():
    """
    Tests importing of gym envs
    """
    gym.spec('poke-v0')

    print('Test complete.')
    return True


def test_import():
    assert main() is True


if __name__ == '__main__':
    main()
