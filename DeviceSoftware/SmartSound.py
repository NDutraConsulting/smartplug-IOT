from SmartMCP3008 import SmartMCP3008
import RPi.GPIO as GPIO


class SmartSound():

    def __init__(self, GPIO_pin, MCP_ENV_PIN, MCP_AUD_PIN):
        self.mcp = SmartMCP3008()
        self.GPIO_pin = GPIO_pin
        self.MCP_ENV_PIN = MCP_ENV_PIN
        self.MCP_AUD_PIN = MCP_AUD_PIN
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_pin, GPIO.IN)

    def get_gate(self):
        GPIO.setmode(GPIO.BCM)
        return GPIO.input(self.GPIO_pin)

    def get_envelope(self):
        return self.mcp.read(self.MCP_ENV_PIN)

    def get_audio(self):
        return self.mcp.read(self.MCP_AUD_PIN)
