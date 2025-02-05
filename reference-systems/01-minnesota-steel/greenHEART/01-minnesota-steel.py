# GreenHEART imports
from greenheart.simulation.greenheart_simulation import GreenHeartSimulationConfig, run_simulation
from greenheart.tools.optimization.gc_run_greenheart import run_greenheart

# run the stuff
if __name__ == "__main__":
    # load inputs as needed
    filename_turbine_config = "./input-files/turbines/ATB2024_6MW_170RD_floris_turbine.yaml"
    filename_floris_config = "./input-files/floris/floris_input_lbw_6MW.yaml"
    filename_hopp_config = "./input-files/plant/hopp_config_mn.yaml"
    filename_greenheart_config = "./input-files/plant/greenheart_config_onshore_mn.yaml"

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
        plant_design_scenario=1,
        output_level=8,
        save_greenheart_output=True,
    )

    # for analysis
    prob, config = run_greenheart(config, run_only=True)

    # for optimization
    prob, config = run_greenheart(config, run_only=False)
    
    lcoe = prob.get_val("lcoe", units="USD/(MW*h)")
    lcoh = prob.get_val("lcoh", units="USD/kg")
    lcos = prob.get_val("lcos", units="USD/t")

    print("LCOE: ", lcoe, "[$/MWh]")
    print("LCOH: ", lcoh, "[$/kg]")
    print("LCOS: ", lcos, "[$/metric-tonne]")

    # for more output results

    # from greenheart.tools.profast_tools import make_price_breakdown
    # from greenheart.tools.profast_tools import make_pf_config_from_profast
    # import matplotlib.pyplot as plt

    # gh_output = run_simulation(config)
    # pf_config = make_pf_config_from_profast(gh_output.profast_lcoh)

    # full_price_breakdown, lco_check = make_price_breakdown(gh_output.profast_lcoh.get_cost_breakdown(), pf_config)

    # plot = plt.barh(*zip(*full_price_breakdown.items()))
    # plt.savefig("./output/figures/lcoh_breakdown/lcoh_elenya.pdf")