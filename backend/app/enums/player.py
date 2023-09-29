from enum import Enum


class PlayerState(str, Enum):
    CALLED = 'called'
    NOT_CALLED = 'not_called'
    INJURED = 'injured'
    SUSPENDED = 'suspended'


class PlayerPosition(str, Enum):
    POINTGUARD = 'pointguard'
    SHOOTINGGUARD = 'shootingguard'
    SMALLFORWARD = 'smallforward'
    POWERFORWARD = 'powerforward'
    CENTER = 'center'
