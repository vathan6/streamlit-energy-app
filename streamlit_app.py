import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Παιχνίδι Κατανάλωσης Ενέργειας", layout="centered")

st.title("🔌 Παιχνίδι Κατανάλωσης Ενέργειας – Nash Ισορροπία")

# Sidebar sliders για τις παραμέτρους
n_users = st.slider("Αριθμός Χρηστών", min_value=2, max_value=50, value=10)
c = st.slider("Κόστος ανά μονάδα ενέργειας (c)", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
d = st.slider("Εξωτερική επίδραση από άλλους χρήστες (d)", min_value=0.0, max_value=1.0, value=0.1, step=0.01)

# Συναρτήσεις μοντέλου
def benefit(x):
    return 10 * x - 0.5 * x**2

def cost(x):
    return c * x

def externality(x_other_sum):
    return d * x_other_sum

def net_utility(x_i, x_other_sum):
    return benefit(x_i) - cost(x_i) - externality(x_other_sum)

def find_nash_equilibrium():
    x_eq = 10 - c - d * (n_users - 1)
    return max(x_eq, 0)

# Υπολογισμός Nash ισορροπίας
x_star = find_nash_equilibrium()
x_others_sum = (n_users - 1) * x_star

st.subheader("📊 Αποτελέσματα")
st.markdown(f"- **Κατανάλωση ανά χρήστη στη Nash ισορροπία:** {x_star:.2f} μονάδες")
st.markdown(f"- **Συνολική κατανάλωση των άλλων χρηστών:** {x_others_sum:.2f} μονάδες")

# Γράφημα καθαρού οφέλους
energy_range = np.linspace(0, 12, 100)
utilities = [net_utility(x, x_others_sum) for x in energy_range]

fig, ax = plt.subplots()
ax.plot(energy_range, utilities, label='Καθαρό Όφελος χρήστη')
ax.axvline(x_star, color='red', linestyle='--', label=f'Nash: {x_star:.2f}')
ax.set_xlabel("Κατανάλωση Ενέργειας ανά Χρήστη")
ax.set_ylabel("Καθαρό Όφελος")
ax.set_title("Καθαρό Όφελος vs Κατανάλωση Ενέργειας")
ax.legend()
ax.grid(True)

st.pyplot(fig)
