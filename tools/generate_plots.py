import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
from os import makedirs
from hopp.utilities import load_yaml

def plot_performance_curves(sites, save_location=False, xlim=[0,30], ylimp=[0,0.5], ylimt=[0,1.0], include_labels=True):

    if include_labels:
        labels = [["(a)", "(b)"],
                  ["(c)", "(d)"],
                  ["(e)", "(f)"]]
    else: 
        labels = [["", ""],
                  ["", ""],
                  ["", ""]]
                  
    fig, ax = plt.subplots(nrows=2, ncols=3, sharex=True, sharey="row", figsize=(8, 4))

    for i, site in enumerate(sites):

        turbine_data = load_performance_data(site)
        wind_speed = turbine_data["power_thrust_table"]["wind_speed"]
        power = turbine_data["power_thrust_table"]["power"]
        thrust = turbine_data["power_thrust_table"]["thrust"]

        rating = int(turbine_data["turbine_rating"])

        ax[0, i].plot(wind_speed, power)
        if i == 0:
            ax[0, i].set(ylabel="Power Coefficient", xlim=xlim, ylim=ylimp)
        ax[0, i].text(0.5,0.455,labels[i][0])

        ax[1, i].plot(wind_speed, thrust)
        ax[1, i].set(xlabel="Wind Speed (m/s)", xlim=xlim, ylim=ylimt)
        if i == 0:
            ax[1, i].set(ylabel="Thrust Coefficient", xlim=xlim, ylim=ylimt)
        ax[1, i].text(0.5,0.95,labels[i][1])
        
        ax[0, i].spines[['right', 'top']].set_visible(False)
        ax[1, i].spines[['right', 'top']].set_visible(False)

        ax[0, i].set_title(f"{rating} MW Turbine")

    plt.tight_layout()
    if save_location:
        if not Path.exists(Path(save_location)):
            makedirs(save_location)
        plt.savefig(save_location+f"performance_curves.pdf", transparent=True)

    return 0

def load_performance_data(site):

    if site == 1:
        data = load_yaml("../reference-systems/01-minnesota-steel/greenHEART/input-files/turbines/ATB2024_6MW_170RD_floris_turbine.yaml")
    elif site == 2:
        data = load_yaml("../reference-systems/02-texas-ammonia/greenHEART/input-files/turbines/ATB2024_6MW_170RD_floris_turbine.yaml")
    elif site == 3:
        data = load_yaml("../reference-systems/03-gulf_of_mexico-hydrogen/greenHEART/input-files/turbines/osw_17MW.yaml")
    elif site == 4:
        data = load_yaml("../reference-systems/04-new_york-hydrogen/greenHEART/input-files/turbines/osw_15MW.yaml")
    elif site == 5:
        data = load_yaml("../reference-systems/05-california-hydrogen/greenHEART/input-files/turbines/osw_15MW.yaml")

    return data


if __name__ == "__main__":
    plot_performance_curves(sites=[1,3,4], save_location="./images/", include_labels=True)