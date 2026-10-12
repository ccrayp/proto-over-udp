from enum import Enum

ADD_COMMAND = "ADD"         # id|ADD|code|product_name|None?quantity
GET_COMMAND = "GET"         # id|GET|code?product_name
SET_QTY_COMMAND = "SET_QTY" # id|SET_QTY|code|quantity
DELETE_COMMAND = "DELETE"   # id|DELETE|code
LIST_COMMAND = "LIST"       # id|LIST|

ALLOWED_COMMANDS = [ADD_COMMAND, GET_COMMAND, SET_QTY_COMMAND, DELETE_COMMAND, LIST_COMMAND]

ARGS_QTY_BY_COMMAND = {
    ADD_COMMAND: [2, 3],
    GET_COMMAND: [1],
    SET_QTY_COMMAND: [2],
    DELETE_COMMAND: [1],
    LIST_COMMAND: [0]
}

OK_STATUS = "OK"
ERROR_STATUS = "ERROR"