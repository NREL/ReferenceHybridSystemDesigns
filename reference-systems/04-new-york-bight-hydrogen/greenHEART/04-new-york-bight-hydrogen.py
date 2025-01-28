# general imports
import os

# GreenHEART imports
from greenheart.simulation.greenheart_simulation import GreenHeartSimulationConfig
from greenheart.tools.optimization.gc_run_greenheart import run_greenheart

# ORBIT imports
from ORBIT.core.library import initialize_library

initialize_library(os.path.join(os.getcwd(), "./input-files/"))

# run the stuff
if __name__ == "__main__":
    # load inputs as needed
    turbine_model = "osw_15MW"
    region = "nyb"
    filename_turbine_config = "./input-files/turbines/"+ turbine_model +".yaml"
    filename_floris_config = "./input-files/floris/floris_input_"+ turbine_model+ ".yaml"
    filename_hopp_config = "./input-files/plant/hopp_config_"+region+".yaml"
    filename_orbit_config = "./input-files/plant/orbit-config-" + turbine_model + "-"+region+".yaml"
    filename_greenheart_config = "./input-files/plant/greenheart_config_offshore_"+region+".yaml"

    config = GreenHeartSimulationConfig(
        filename_hopp_config=filename_hopp_config,
        filename_greenheart_config=filename_greenheart_config,
        filename_turbine_config=filename_turbine_config,
        filename_orbit_config=filename_orbit_config,
        filename_floris_config=filename_floris_config,
        verbose=True,
        show_plots=False,
        save_plots=True,
        use_profast=True,
        post_processing=True,
        incentive_option=1,
        plant_design_scenario=4,
        output_level=8,
        save_greenheart_output=True,
    )

    # for analysis
    prob, config = run_greenheart(config, run_only=True)

    # for optimization
    # prob, config = run_greenheart(config, run_only=False)
    
    lcoe = prob.get_val("lcoe", units="USD/(MW*h)")
    lcoh = prob.get_val("lcoh", units="USD/kg")

    print("LCOE: ", lcoe, "[$/MWh]")
    print("LCOH: ", lcoh, "[$/kg]")
