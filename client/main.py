import time

from client.SocketClient import SocketClient, MAX_TRIES
from client.Validator import Validator
from client.Printer import Printer
from common.Commands import *
from common.PayloadFactory import PayloadFactory

socket = SocketClient("127.0.0.1", 5011)

while True:
    try:
        Printer.inputEnterance()
        inputStr = input()

        if inputStr.lower() == "exit":
            break

        if inputStr.lower() == "help" or inputStr == "?":
            Printer.showHelp()
            Printer.newLine()
            continue


        isValid, invalidToken, errorPosition = Validator.validate(inputStr)
        if not isValid:
            Printer.invalidInput(inputStr, invalidToken, errorPosition)
            Printer.newLine()
            continue

        payload = PayloadFactory.newOfRawData(rawData=inputStr, generateId=True)
        Printer.printRequestId(payload)

        triesCounter = 0
        start_time = time.perf_counter()
        
        while triesCounter != MAX_TRIES:
            socket.transmit(payload)
            responsePayload = socket.recieve()
            if responsePayload is not None:
                break
            triesCounter += 1
            Printer.timeout(triesCounter, MAX_TRIES)

        elapsed_time = time.perf_counter() - start_time

        if responsePayload is not None:
            Printer.report(elapsed_time, triesCounter, responsePayload, MAX_TRIES)
            
        Printer.newLine()
    except KeyboardInterrupt:
        break

# socket.transmit(PayloadFactory.newOfArgs(command=ADD_COMMAND, args=["C1", "Мороженое"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=ADD_COMMAND, args=["P1", "Вафли", "10"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=GET_COMMAND, args=["C1"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=GET_COMMAND, args=["Вафли"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=SET_QTY_COMMAND, args=["C1", "2"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=GET_COMMAND, args=["P1"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=LIST_COMMAND))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=DELETE_COMMAND, args=["C1"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=DELETE_COMMAND, args=["P1"]))
# print(socket.recieve().toString())
# socket.transmit(PayloadFactory.newOfArgs(command=LIST_COMMAND))
# print(socket.recieve().toString())