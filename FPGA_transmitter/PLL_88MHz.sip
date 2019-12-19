set_global_assignment -entity "PLL_88MHz" -library "lib_PLL_88MHz" -name IP_TOOL_NAME "altera_pll"
set_global_assignment -entity "PLL_88MHz" -library "lib_PLL_88MHz" -name IP_TOOL_VERSION "16.1"
set_global_assignment -entity "PLL_88MHz" -library "lib_PLL_88MHz" -name IP_TOOL_ENV "mwpim"
set_global_assignment -library "lib_PLL_88MHz" -name SPD_FILE [file join $::quartus(sip_path) "PLL_88MHz.spd"]

set_global_assignment -library "lib_PLL_88MHz" -name MISC_FILE [file join $::quartus(sip_path) "PLL_88MHz_sim/PLL_88MHz.vo"]
