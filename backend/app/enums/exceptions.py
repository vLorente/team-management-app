from enum import Enum


class HttpMsgExceptions(str, Enum):
    ITEM_NOT_FOUND = 'No se ha encontrado el elemento.'
