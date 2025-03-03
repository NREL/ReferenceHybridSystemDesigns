# GreenHEART imports
from greenheart.simulation.greenheart_simulation import GreenHeartSimulationConfig
from greenheart.tools.optimization.gc_run_greenheart import run_greenheart
from greenheart.tools.plot import plot_energy_flows, plot_hydrogen_flows

# run the stuff
if __name__ == "__main__":
    # load inputs as needed
    region = "tx"
    filename_turbine_config = "./input-files/turbines/ATB2024_6MW_170RD_floris_turbine.yaml"
    filename_floris_config = "./input-files/floris/floris_input_lbw_6MW.yaml"
    filename_hopp_config = "./input-files/plant/hopp_config_"+region+".yaml"
    filename_greenheart_config = "./input-files/plant/greenheart_config_onshore_"+region+".yaml"

    config = GreenHeartSimulationConfig(
        filename_hopp_config,
        filename_greenheart_config,
        filename_turbine_config,
        filename_floris_config,
        verbose=True,
        show_plots=False,
        save_plots=True,
        use_profast=True,
        post_processing=True,
        incentive_option=1,
        plant_design_scenario=2,
        output_level=8,
        save_greenheart_output=True,
    )

    # for analysis
    prob, config = run_greenheart(config, run_only=True)

    # for optimization
    # prob, config = run_greenheart(config, run_only=False)
    
    lcoe = prob.get_val("lcoe", units="USD/(MW*h)")
    lcoh = prob.get_val("lcoh", units="USD/kg")
    lcoa = prob.get_val("lcoa", units="USD/kg")

    print("LCOE: ", lcoe, "[$/MWh]")
    print("LCOH: ", lcoh, "[$/kg]")
    print("LCOA: ", lcoa, "[$/kg]")

    plot_energy_flows("./output/data/production/energy_flows.csv", show_fig=False)
    plot_hydrogen_flows("./output/data/production/energy_flows.csv", show_fig=False)