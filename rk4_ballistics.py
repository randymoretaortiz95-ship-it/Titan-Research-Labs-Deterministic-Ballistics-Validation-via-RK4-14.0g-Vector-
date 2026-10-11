"""
Titan Research Labs - Simulatore Balistico Deterministico (RK4)
Autore: Titan Research Labs
Descrizione: Calcola la traiettoria balistica bidimensionale di un vettore da 
14.0g utilizzando l'integrazione numerica Runge-Kutta al quarto ordine (RK4).
"""

import math

def run_simulation():
    # Parametri fisici del vettore e ambientali
    m = 0.014            # Massa in kg (14.0 g)
    rho = 1.213          # Densità dell'aria in kg/m^3
    diameter = 0.04      # Diametro di riferimento in metri
    A = math.pi * (diameter / 2)**2  # Sezione trasversale in m^2
    Cd = 0.55            # Coefficiente di resistenza aerodinamica (Drag)
    g = 9.80665          # Accelerazione di gravità in m/s^2

    # Condizioni iniziali
    x = 0.0              # Posizione orizzontale iniziale (m)
    y = 2.0              # Posizione verticale iniziale (altezza in m)
    v0 = 32.0            # Velocità iniziale (m/s)
    theta_deg = 0.0      # Angolo di lancio rispetto all'orizzontale
    
    vx = v0 * math.cos(math.radians(theta_deg))
    vy = v0 * math.sin(math.radians(theta_deg))

    # Parametri di integrazione numerica
    dt = 0.0001          # Passo temporale di micro-integrazione
    t = 0.0              # Tempo iniziale

    # Funzione delle derivate posizionata CORRETTAMENTE fuori dal ciclo di calcolo
    def derivatives(px, py, pvx, pvy):
        v_norm = math.sqrt(pvx**2 + pvy**2)
        drag_factor = 0.5 * rho * A * Cd * v_norm / m
        ax = -drag_factor * pvx
        ay = -g - drag_factor * pvy
        return pvx, pvy, ax, ay

    print("=== AVVIO SIMULAZIONE NUMERICA REALE (RK4) ===")
    print(f"Massa: {m*1000:.1f}g | Velocità Iniziale: {v0} m/s | Densità Aria: {rho} kg/m^3\n")

    # Ciclo di integrazione fino all'impatto al suolo (y <= 0)
    while y > 0:
        # Applicazione dell'algoritmo Runge-Kutta al 4o ordine (RK4)
        # k1
        vx1, vy1, ax1, ay1 = derivatives(x, y, vx, vy)
        
        # k2
        vx2, vy2, ax2, ay2 = derivatives(
            x + 0.5 * dt * vx1, 
            y + 0.5 * dt * vy1, 
            vx + 0.5 * dt * ax1, 
            vy + 0.5 * dt * ay1
        )
        
        # k3
        vx3, vy3, ax3, ay3 = derivatives(
            x + 0.5 * dt * vx2, 
            y + 0.5 * dt * vy2, 
            vx + 0.5 * dt * ax2, 
            vy + 0.5 * dt * ay2
        )
        
        # k4
        vx4, vy4, ax4, ay4 = derivatives(
            x + dt * vx3, 
            y + dt * vy3, 
            vx + dt * ax3, 
            vy + dt * ay3
        )

        # Aggiornamento dello stato con media pesata RK4
        x += (dt / 6.0) * (vx1 + 2 * vx2 + 2 * vx3 + vx4)
        y += (dt / 6.0) * (vy1 + 2 * vy2 + 2 * vy3 + vy4)
        vx += (dt / 6.0) * (ax1 + 2 * ax2 + 2 * ax3 + ax4)
        vy += (dt / 6.0) * (ay1 + 2 * ay2 + 2 * ay3 + ay4)
        t += dt

    v_impact = math.sqrt(vx**2 + vy**2)
    
    print("=== RISULTATI DELLA SIMULAZIONE NUMERICA REALE (RK4) ===")
    print(f"Tempo di volo (t): {t:.4f} s")
    print(f"Gittata orizzontale (X): {x:.4f} m")
    print(f"Velocità all'impatto: {v_impact:.2f} m/s")
    print("=====================================================")

if __name__ == "__main__":
    run_simulation()