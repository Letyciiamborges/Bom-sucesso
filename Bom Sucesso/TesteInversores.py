# -*- coding: utf-8 -*-
"""
Teste envio dados inversores 

"""

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST3 = "192.168.3.103"
SERVER_HOST4 = "192.168.3.104"
SERVER_HOST5 = "192.168.3.105"

SERVER_PORT3 = 502
SERVER_PORT4 = 502
SERVER_PORT5 = 502

c3 = ModbusClient()
c4 = ModbusClient()
c5 = ModbusClient()

c3.host(SERVER_HOST3)
c4.host(SERVER_HOST4)
c5.host(SERVER_HOST5)

c3.port(SERVER_PORT3)
c4.port(SERVER_PORT4)
c5.port(SERVER_PORT5)

while True:
    if not c3.is_open():
        if not c3.open():
            print("unable to connect to "+SERVER_HOST3+":"+str(SERVER_PORT3))
    if c3.is_open():
        regs3 = c3.read_holding_registers(40070, 50)
        if regs3:
            print("inversor 3")
        i = 0
        while True:
            vetorinv3=[float(regs3[33]/10), float(regs3[31]/1000), float(regs3[10]/10), float(regs3[11]/10), float(regs3[12]/10), float(regs3[3]/10), float(regs3[4]/10), float(regs3[5]/10), float(regs3[14]/1000), float(regs3[22]/10000), float(regs3[16]/100), float(regs3[38])]
            i+=1
            print(vetorinv3)
            if i == 1:
                break
    if not c4.is_open():
        if not c4.open():
            print("unable to connect to "+SERVER_HOST4+":"+str(SERVER_PORT4))
    if c4.is_open():
        regs4 = c4.read_holding_registers(40070, 50)
        if regs4:
            print("inversor 4")
        i = 0
        while True:
            vetorinv4=[float(regs4[33]/10), float(regs4[31]/1000), float(regs4[10]/10), float(regs4[11]/10), float(regs4[12]/10), float(regs4[3]/10), float(regs4[4]/10), float(regs4[5]/10), float(regs4[14]/1000), float(regs4[22]/10000), float(regs4[16]/100), float(regs4[38])]
            i+=1
            print(vetorinv4)
            if i == 1:
                break
    if not c5.is_open():
        if not c5.open():
            print("unable to connect to "+SERVER_HOST5+":"+str(SERVER_PORT5))
    if c5.is_open():
        regs5 = c5.read_holding_registers(40070, 50)
        if regs5:
            print("inversor 5")
        i = 0
        while True:
            vetorinv5=[float(regs5[33]/10), float(regs5[31]/1000), float(regs5[10]/10), float(regs5[11]/10), float(regs5[12]/10), float(regs5[3]/10), float(regs5[4]/10), float(regs5[5]/10), float(regs5[14]/1000), float(regs5[22]/10000), float(regs5[16]/100), float(regs5[38])]
            i+=1
            print(vetorinv5)
            if i == 1:
                break

time.sleep(2)