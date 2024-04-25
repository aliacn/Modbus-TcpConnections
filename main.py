from pymodbus.client import ModbusTcpClient
import socket

def check_connection(ip, port):
    try:
        # Bir soket oluştur ve bağlantıyı dene
        socket.create_connection((ip, port), timeout=5)
        print("Bağlantı başarılı!")
        return True
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return False

# IP adresi ve port numarasını belirt
ip_address = "10.108.229.186"
port_number = 502

# Bağlantıyı kontrol et
if check_connection(ip_address, port_number):
    # Modbus TCP/IP istemcisini oluştur
    client = ModbusTcpClient(ip_address, port_number)

    # Bağlantıyı aç
    client.connect()

    try:
        # Veri okuma işlemi
        # Örneğin, enerji analizöründe 1. register'dan başlayarak 10 register okuyalım
        starting_register = 40001
        num_registers_to_read = 40011
        result = client.read_holding_registers(starting_register, num_registers_to_read, unit=1)

        if result.isError():
            print("Modbus Hatası:", result)
        else:
            # Okunan verileri işle
            registers = result.registers
            print("Okunan register değerleri:", registers)
    finally:
        # Bağlantıyı kapat
        client.close()
