from pymodbus.client.sync import ModbusSerialClient as ModbusClient

def run_sync_dados(id,porta, register_ini, register_fim):
    client = ModbusClient(method='rtu', port=porta, timeout=0.25, baudrate=9600)
    client.strict=False
    client.connect()
    try:
        dados = client.read_input_registers(register_ini,register_fim,unit=id)
    except Exception as e:
        print('Erro leitura de registros')
    try:
        a = dados.registers
    except Exception as e:
        return []
    client.close()
    return a
    
    