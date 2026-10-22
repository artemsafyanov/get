import mcp3021_driver as mcp
import time
import adc_plot

if __name__ == "__main__":
    adc = mcp.MCP3021(5.19)

    voltage_values = []
    time_values = []
    duration = 3.0

    try:
        start_time = time.time()
        while True:
            otn_time = time.time() - start_time
            voltage_values.append(adc.get_voltage())
            time_values.append(otn_time)
            if (otn_time >= duration):
                break
        adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
        adc_plot.plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()