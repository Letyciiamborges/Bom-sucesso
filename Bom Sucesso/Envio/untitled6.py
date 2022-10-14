# -*- coding: utf-8 -*-
"""

"""
from pymodbus.client.sync import ModbusTcpClient

# Para cada inversor ???
#-----------------------------------------------------------------------------

IPADDRESS = '192.168.1.23' # IP do inversor 
c = ModbusTcpClient(IPADDRESS, timeout = 5)
c.connect()

regsList1 =  c.read_holding_registers(70,50)
t1 = len(regsList1)

#-----------------------------------------------------------------------------
i = 0
while True:
    dadosEnviar = {
    "temperatura_inv": float(regsList1.registers[33]),
    "potencia_total_dc":float(regsList1.registers[31]),
    "tensao_a": float(regsList1.registers[10]), 
    "tensao_b": float(regsList1.registers[11]),
    "tensao_c": float(regsList1.registers[12]),
    "corrente_a": float(regsList1.registers[3]),
    "corrente_b": float(regsList1.registers[4]),
    "corrente_c": float(regsList1.registers[5]),
    "potencia_total_ac": float(regsList1.registers[14]),
    "fp": float(regsList1.registers[22]),
    "frequencia": float(regsList1.registers[16]),
    "status": float(regsList1.registers[38]), #olhar aqui
    "pot_ativa": float(regsList1.registers[18]),
    "pot_reativa": float(regsList1.registers[20]),
    }
    
    i+=1
    if i == 10:
        break
    
