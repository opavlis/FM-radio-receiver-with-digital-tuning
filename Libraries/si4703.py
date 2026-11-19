import time

class Si4703:
    def __init__(self, i2c, i2c_addr=0x10):
        self.i2c = i2c
        self.addr = i2c_addr
        self.registers = [0] * 16
        
        # 1. Start oscilátoru
        self.read_registers()
        self.registers[0x07] = 0x8100  # ENABLE bit
        self.write_registers()
        time.sleep_ms(500)
        
        # 2. Zapnutí rádia a nastavení pro Evropu
        self.read_registers()
        self.registers[0x02] = 0x4001  # Power up (Enable, Disable Mute)
        self.registers[0x04] |= 0x2000 # Krok 100 kHz (Evropa)
        self.registers[0x05] |= 0x000F # Hlasitost na max (0-15)
        self.write_registers()
        time.sleep_ms(110)

    def read_registers(self):
        # Si4703 je zvláštní: čtení vždy začíná od registru 0x0A
        data = self.i2c.readfrom(self.addr, 32)
        for i in range(16):
            reg = (0x0A + i) % 16
            self.registers[reg] = (data[i*2] << 8) | data[i*2 + 1]

    def write_registers(self):
        # Zápis vždy začíná od registru 0x02. Posíláme registry 0x02 až 0x07
        data = bytearray(12)
        for i in range(6):
            reg = 0x02 + i
            data[i*2] = (self.registers[reg] >> 8) & 0xFF
            data[i*2 + 1] = self.registers[reg] & 0xFF
        self.i2c.writeto(self.addr, data)

    def set_frequency(self, freq_mhz):
        # Přepočet frekvence na kanál (základ 87.5 MHz, krok 100 kHz)
        freq_khz = int(freq_mhz * 1000)
        channel = (freq_khz - 87500) // 100
        
        self.read_registers()
        self.registers[0x03] = channel | 0x8000  # Zápis kanálu a TUNE bitu
        self.write_registers()
        
        # Čekání na dokončení ladění (STC bit v registru 0x0A)
        while True:
            self.read_registers()
            if self.registers[0x0A] & 0x4000:
                break
            time.sleep_ms(10)
        
        # Vypnutí TUNE bitu po úspěšném naladění
        self.read_registers()
        self.registers[0x03] &= ~0x8000
        self.write_registers()

    def set_volume(self, volume):
        # volume: 0 (ticho) až 15 (max)
        self.read_registers()
        self.registers[0x05] = (self.registers[0x05] & 0xFFF0) | (volume & 0x0F)
        self.write_registers()