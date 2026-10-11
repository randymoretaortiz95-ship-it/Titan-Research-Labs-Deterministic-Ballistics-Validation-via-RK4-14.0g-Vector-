# Titan Research Labs - Deterministic Ballistics Verification

Repository ufficiale per la validazione fisica e numerica del vettore isotropo da 14.0g attraverso l'integrazione numerica Runge-Kutta al quarto ordine (RK4).

## Obiettivo del Progetto
Questo repository fornisce un framework computazionale trasparente, aperto e deterministico per calcolare la balistica e la resistenza aerodinamica, eliminando qualsiasi ambiguità interpretativa o approssimazione stocastica. I risultati sono riproducibili al 100% da chiunque disponga di un interprete Python.

## Parametri di Base del Sistema
* Massa del vettore (m): 0.014 kg (14.0 g)
* Velocità iniziale (v0): 32.0 m/s
* Densità dell'aria (rho): 1.213 kg/m^3 (derivata dai dati ambientali di riferimento)
* Coefficiente di Drag (Cd): 0.55
* Accelerazione di gravità (g): 9.80665 m/s^2

## Risultati della Simulazione di Riferimento
Eseguendo lo script di integrazione RK4 con passo temporale dt = 0.0001s, si ottengono i seguenti valori deterministici certificati:
* Tempo di volo (t): 0.6926 s
* Gittata orizzontale (X): 16.8830 m
* Velocità all'impatto: 19.90 m/s

## Come Eseguire la Simulazione
1. Assicurati di avere Python installato sul tuo sistema.
2. Clona questo repository o scarica il file `rk4_ballistics.py`.
3. Esegui lo script dal terminale:
   ```bash
   python rk4_ballistics.py
