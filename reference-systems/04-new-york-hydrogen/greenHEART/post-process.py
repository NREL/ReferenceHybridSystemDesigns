import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

from hopp.tools.dispatch.plot_tools import plot_generation_profile, plot_battery_generation
from greenheart.tools.dispatch.plot_dispatch import plot_hydrogen_flows, get_hour_from_datetime, plot_generation_profile

def plot_energy_flows(energy_flow_data_path, start_date_time=dt.datetime(2024, 1, 5, 14), end_date_time=dt.datetime(2024, 1, 10, 14)):

    # set start and end dates
    hour_start, hour_end = get_hour_from_datetime(start_date_time, end_date_time)

    # load data
    # import pdb;pdb.set_trace()
    df_data = pd.read_csv(energy_flow_data_path, index_col=0)
    df_data = df_data.iloc[hour_start:hour_end]

    # set up plots
    fig, ax = plt.subplots(2,2, sharex=True, figsize=(10,6))

    # plot electricity output
    # df_e_out = df_data[["wind generation [kW]", "pv generation [kW]", "wave generation [kW]"]]
    df_e_out = df_data[["wind generation [kW]", "pv generation [kW]"]]*1E-6
    df_e_out.rename(columns={"wind generation [kW]": "wind generation [GW]", "pv generation [kW]": "pv generation [GW]"}, inplace=True)
    df_e_out.plot(ax=ax[0,0], logy=False, ylabel="Electricity Output (GW)", ylim=[0, max(df_e_out["wind generation [GW]"])*1.5])
    ax[0, 0].legend(frameon=False)

    # plot battery charge/discharge
    df_batt_power = df_data[["battery charge [kW]", "battery discharge [kW]"]]*1E-6
    df_batt_power.rename(columns={"battery charge [kW]": "battery charge [GW]", "battery discharge [kW]": "battery discharge [GW]"}, inplace=True)
    leg_info_batt_pow = df_batt_power.plot(ax=ax[0,1], logy=False, ylabel="Battery Power (GW)", ylim=[0, max([max(df_batt_power["battery discharge [GW]"]),max(df_batt_power["battery charge [GW]"])])*1.5], legend=False)

    ax01_twin=ax[0, 1].twinx()

    df_batt_soc = df_data[["battery state of charge [%]"]]
    leg_info_batt_soc = df_batt_soc.plot(ax=ax01_twin, ylabel="Battery SOC (%)", linestyle=":", color="k", ylim=[0,150], legend=False)

    leg_lines = leg_info_batt_pow.lines + leg_info_batt_soc.lines
    leg_labels = [l.get_label() for l in leg_lines]
    ax[0, 1].legend(leg_lines, leg_labels, frameon=False, loc=0)
    
    # plot energy usage
    # df_e_usage = df_data[["desal energy hourly [kW]", "electrolyzer energy hourly [kW]", "transport compressor energy hourly [kW]", "storage energy hourly [kW]"]]
    df_e_usage = df_data[["electrolyzer energy hourly [kW]",]]*1E-6
    df_e_usage.rename(columns={"electrolyzer energy hourly [kW]": "electrolyzer energy hourly [GW]"}, inplace=True)
    df_e_usage.plot(ax=ax[1,0], logy=False, ylabel="Electricity Usage (GW)", xlabel="Hour", ylim=[0, max(df_e_usage["electrolyzer energy hourly [GW]"])*1.5])
    ax[1, 0].legend(frameon=False)

    # plot hydrogen production
    df_h_out = df_data[["h2 production hourly [kg]", "hydrogen storage SOC [kg]"]]*1E-3
    ax[1, 1].plot(df_h_out)
    ax[1, 1].set(ylabel="Hydrogen Produced (t)", xlabel="Hour")

    # fig.add_axes((0, 0, 1, 0.5))
    plt.tight_layout()
    plt.show()

def plot_energy(energy_flow_data_path, start_date_time=dt.datetime(2024, 1, 2, 1), end_date_time=dt.datetime(2024, 12, 3, 14)):

    # set start and end dates
    hour_start, hour_end = get_hour_from_datetime(start_date_time, end_date_time)

    # load data
    # import pdb;pdb.set_trace()
    df_data = pd.read_csv(energy_flow_data_path, index_col=0)
    df_data = df_data.iloc[hour_start:hour_end]

    # set up plots
    fig, ax = plt.subplots(2,2, sharex=True, figsize=(10,6))

    # plot electricity output
    # df_e_out = df_data[["wind generation [kW]", "pv generation [kW]", "wave generation [kW]"]]
    df_e_out = df_data[["wind generation [kW]", "pv generation [kW]", "generation hourly [kW]", "battery charge [kW]", "battery discharge [kW]", "generation curtailed hourly [kW]"]]*1E-6
    df_e_out.rename(
        columns={"wind generation [kW]": "wind generation [GW]",
                 "pv generation [kW]": "pv generation [GW]",  
                 "generation hourly [kW]": "generation hourly [GW]",
                 "generation curtailed hourly [kW]": "generation curtailed hourly [GW]",
                 "battery charge [kW]": "battery charge [GW]", 
                 "battery discharge [kW]": "battery discharge [GW]"
                 }, 
        inplace=True)
    df_e_out['Sum PV+Wind'] = df_e_out["pv generation [GW]"] + df_e_out['wind generation [GW]']
    df_e_out['Sum PV+Wind+Batt.'] = df_e_out["pv generation [GW]"] + df_e_out['wind generation [GW]'] + df_e_out['battery discharge [GW]'] - df_e_out['battery charge [GW]']
    df_e_out['Sum Wind+Batt.'] = df_e_out['wind generation [GW]'] + df_e_out['battery discharge [GW]'] - df_e_out['battery charge [GW]']
    df_e_out.plot(ax=ax[0,0], logy=False, ylabel="Electricity Output (GW)")#, ylim=[0, max(df_e_out["total renewable energy production hourly [GW]"])*1.5])
    ax[0, 0].legend(frameon=False)

    # plot battery charge/discharge
    df_batt_power = df_data[["battery charge [kW]", "battery discharge [kW]"]]*1E-6
    df_batt_power.rename(columns={"battery charge [kW]": "battery charge [GW]", "battery discharge [kW]": "battery discharge [GW]"}, inplace=True)
    leg_info_batt_pow = df_batt_power.plot(ax=ax[0,1], logy=False, ylabel="Battery Power (GW)", ylim=[0, max([max(df_batt_power["battery discharge [GW]"]),max(df_batt_power["battery charge [GW]"])])*1.5], legend=False)

    ax01_twin=ax[0, 1].twinx()

    df_batt_soc = df_data[["battery state of charge [%]"]]
    leg_info_batt_soc = df_batt_soc.plot(ax=ax01_twin, ylabel="Battery SOC (%)", linestyle=":", color="k", ylim=[0,150], legend=False)

    leg_lines = leg_info_batt_pow.lines + leg_info_batt_soc.lines
    leg_labels = [l.get_label() for l in leg_lines]
    ax[0, 1].legend(leg_lines, leg_labels, frameon=False, loc=0)
    
    # plot energy usage
    # df_e_usage = df_data[["desal energy hourly [kW]", "electrolyzer energy hourly [kW]", "transport compressor energy hourly [kW]", "storage energy hourly [kW]"]]
    # df_e_usage = df_data[["electrolyzer energy hourly [kW]",]]*1E-6
    # df_e_usage.rename(columns={"electrolyzer energy hourly [kW]": "electrolyzer energy hourly [GW]"}, inplace=True)
    # df_e_usage.plot(ax=ax[1,0], logy=False, ylabel="Electricity Usage (GW)", xlabel="Hour", ylim=[0, max(df_e_usage["electrolyzer energy hourly [GW]"])*1.5])
    # ax[1, 0].legend(frameon=False)
    df_error = pd.DataFrame()
    df_error["error pv/wind/batt [GW]"] = df_e_out["Sum PV+Wind+Batt."] - df_e_out["generation hourly [GW]"] - df_e_out["generation curtailed hourly [GW]"]
    df_error.plot(ax=ax[1,0])

    # plot hydrogen production
    df_h_out = df_data[["h2 production hourly [kg]", "hydrogen storage SOC [kg]"]]*1E-3
    ax[1, 1].plot(df_h_out)
    ax[1, 1].set(ylabel="Hydrogen Produced (t)", xlabel="Hour")
    
    df_e_out["generation curtailed hourly [GW]"]
    # fig.add_axes((0, 0, 1, 0.5))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    energy_flows_data_path = "./output/data/production/energy_flows.csv"
    # plot_energy_flows(energy_flow_data_path=energy_flows_data_path)
    # plot_energy(energy_flow_data_path=energy_flows_data_path)
    plot_generation_profile(energy_flows_data_path, dt.datetime(2024, 7, 1, 0), dt.datetime(2024, 7, 10, 23), plot_filename="output/figures/production/electricity_flow.pdf")
    plot_hydrogen_flows(energy_flows_data_path)