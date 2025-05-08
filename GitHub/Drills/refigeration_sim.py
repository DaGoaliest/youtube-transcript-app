import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt

# -----------------------------
# SETUP: Refrigerant and Pressures
# -----------------------------

# Define the refrigerant being used
fluid = 'R134a'

# Define pressures in Pascals
P_evap = 300_000    # Evaporator (low pressure side)
P_cond = 1_200_000  # Condenser (high pressure side)

# -----------------------------
# THERMODYNAMIC STATE CALCULATIONS
# -----------------------------

# Point 1: After evaporation - saturated vapor (Q=1) at low pressure
h1 = CP.PropsSI('H', 'P', P_evap, 'Q', 1, fluid)
s1 = CP.PropsSI('S', 'P', P_evap, 'Q', 1, fluid)
T1 = CP.PropsSI('T', 'P', P_evap, 'Q', 1, fluid)

# Point 2: After compression - isentropic compression to high pressure
h2 = CP.PropsSI('H', 'P', P_cond, 'S', s1, fluid)
T2 = CP.PropsSI('T', 'P', P_cond, 'S', s1, fluid)

# Point 3: After condensation - saturated liquid (Q=0) at high pressure
h3 = CP.PropsSI('H', 'P', P_cond, 'Q', 0, fluid)
T3 = CP.PropsSI('T', 'P', P_cond, 'Q', 0, fluid)

# Point 4: After expansion - constant enthalpy drop to low pressure
h4 = h3  # Expansion is isenthalpic
T4 = CP.PropsSI('T', 'P', P_evap, 'H', h4, fluid)

# -----------------------------
# BUILD THE CYCLE DATA LISTS
# -----------------------------

# Enthalpy values for each point (J/kg → kJ/kg)
h_vals = [h1, h2, h3, h4, h1]
h_vals_kJ = [h / 1000 for h in h_vals]

# Temperature values (K → °C)
T_vals = [T1, T2, T3, T4, T1]
T_vals_C = [T - 273.15 for T in T_vals]

# Pressure values (Pa → bar)
P_vals = [P_evap, P_cond, P_cond, P_evap, P_evap]
P_vals_bar = [P / 100000 for P in P_vals]

# -----------------------------
# PLOTTING: Side-by-side Subplots
# -----------------------------

# Create 2 subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# --- T-h Diagram (Temperature vs. Enthalpy) ---
axs[0].plot(h_vals_kJ, T_vals_C, marker='o', color='blue')
axs[0].set_title('T-h Diagram (R134a)')
axs[0].set_xlabel('Enthalpy (kJ/kg)')
axs[0].set_ylabel('Temperature (°C)')
axs[0].grid(True)

# --- P-h Diagram (Pressure vs. Enthalpy) ---
axs[1].plot(h_vals_kJ, P_vals_bar, marker='o', color='orange')
axs[1].set_title('P-h Diagram (R134a)')
axs[1].set_xlabel('Enthalpy (kJ/kg)')
axs[1].set_ylabel('Pressure (bar)')
axs[1].invert_yaxis()  # Standard for P-h charts: high pressure on top
axs[1].grid(True)

# Show both plots neatly
plt.tight_layout()
plt.show()
