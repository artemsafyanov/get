import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp_i2c = mcp.MCP4725(5.11)

    while True:
        mcp_i2c.set_voltage(sg.get_triangle_wave_amplitude(signal_frequency, time.time()) * amplitude)
        sg.wait_for_sampling_period(sampling_frequency)
    
finally:
    mcp_i2c.deinit()