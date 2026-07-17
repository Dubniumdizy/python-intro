"""
SF1550, Lab B, Uppgift 3, VT26
Bo Strömberg och Disa Degerholm
"""


import numpy as np # math, sqrt, sin, vectors
import matplotlib.pyplot as plt # plot diagrams
import scipy as sp # Linear algebra and optimization

class Data:

    EXPECTED_N = 360

    def __init__(self, t, y) -> None:
        self.t = t
        self.y = y
        self.N = len(t)
        if self.N != self.EXPECTED_N:
            print(f"WARNING: N should be {self.EXPECTED_N}.")
        if self.N != len(y):
            raise ValueError("Must be same number of t and y.")
       
    def __len__(self):
        return self.N


class Parameters:

    def __init__(self, names, vec):
        if len(names) != len(vec):
            raise ValueError("Must be same number of parameter names and values.")
        self.names = names
        self.vec = vec

    def __str__(self):
        msg = []
        for name, val in zip(self.names, self.vec):
            msg.append(f"{name}: {val:.4f}")
        return "\n".join(msg)


class Model:

    def __init__(self, data: Data, params_names, design_str) -> None:
        self._data = data
        params_vec = self._calc_params()
        self.params = Parameters(params_names, params_vec)
        self._y_ests = self._calc_y_ests()
        self._rms_error = self._calc_rms_error()
        self._design_str = design_str

    def _calc_params(self):
        raise NotImplementedError
   
    def _calc_y_ests(self):
        raise NotImplementedError
   
    def evaluate(self, t):
        raise NotImplementedError
   
    def _calc_rms_error(self):
        squared_errors = (self._y_ests - self._data.y)**2
        return np.sqrt(np.mean(squared_errors))
   
    def plot_model(self, t_range, label=None):
        plt.plot(t_range+1980, self.evaluate(t_range), label=label)

    def plot_error(self, label=None):
        error = self.evaluate(self._data.t) - self._data.y
        plt.plot(self._data.t + 1980, error, label=label)

    def __str__(self):
        msg = []
        msg.append(self._design_str)
        msg.append(str(self.params))
        msg.append(f"Root Mean Square Error: {self._rms_error:.4f}")
        return "\n" + "\n".join(msg) + "\n"


class LinearModel(Model):
   
    def __init__(self, data: Data, design_fn, params_names, design_str):
        self.design_fn = design_fn
        super().__init__(data, params_names, design_str)

    def _calc_params(self):
        A = self.design_fn(self._data.t)
        params_vec = np.linalg.lstsq(A, self._data.y)[0]
        return params_vec

    def _calc_y_ests(self):
        return self.evaluate(self._data.t)
       
    def evaluate(self, t):
        A = self.design_fn(t)
        return A @ self.params.vec


class NonlinearModel(Model):

    def __init__(self, data: Data, F_fn, J_fn, model_fn, params_names, design_str, initial_guess):
        self.F_fn = F_fn
        self.J_fn = J_fn
        self.model_fn = model_fn
        self.initial_guess = initial_guess
        super().__init__(data, params_names, design_str)

    def _calc_params(self):
        c = np.array(self.initial_guess, dtype=float)
        tol = 1e-10
        delta = np.inf
       
        while np.linalg.norm(delta) >= tol:
            J = self.J_fn(c, self._data.t)
            F = self.F_fn(c, self._data.t, self._data.y)
            delta = np.linalg.lstsq(J, -F)[0]
            c += delta
        return c

    def _calc_y_ests(self):
        return self.evaluate(self._data.t)
       
    def evaluate(self, t):
        return self.model_fn(self.params.vec, t)


def plot_all(t, y, data: Data, model1, model2, model3):
    # Figur 1: Data och anpassade modeller
    plt.figure(1, figsize=(8, 6))
    plt.plot(t+1980, y, ".", color="gray", alpha=0.5, label="Data (1980-2025)")
    plt.plot(data.t+1980, data.y, ".", color="black", label="Data (1991-2020)")
   
    # Välj ett tidsintervall för att plotta modellerna mjukt
    t_plot = np.linspace(data.t.min(), data.t.max(), 500)

    model1.plot_model(t_plot, label="Enkel linjär")
    model2.plot_model(t_plot, label="Multipel linjär")
    model3.plot_model(t_plot, label="Ickelinjär")

    plt.xlabel("År")
    plt.ylabel("KPI")
    plt.title("KPI-data och anpassade modeller")
    plt.legend()
    plt.grid(True)
    plt.savefig("figs/3_models.svg", bbox_inches="tight")

    # Figur 2: Modellfel (residualer)
    plt.figure(2, figsize=(8, 6))
    model1.plot_error(label="Enkel linjär")
    model2.plot_error(label="Multipel linjär")
    model3.plot_error(label="Ickelinjär")

    plt.axhline(0, color="black", linewidth=1.0)
    plt.xlabel("År")
    plt.ylabel("Modellfel (KPI-enheter)")
    plt.title("Modellfel för 1991-2020")
    plt.legend()
    plt.grid(True)
    plt.savefig("figs/3_errors.svg", bbox_inches="tight")


def load_data():
    # Läs in kolumn nummer två från filen (KPI-värdena).
    # Hoppa över de tre första raderna eftersom de inte innehåller data.
    y = np.loadtxt("KPI.csv", delimiter=",", skiprows=3, usecols=1)
    # Skapa en vektor t som innehåller antal år från januari 1980
    # (första datapunkten). Vi delar med 12 eftersom det är en
    # datapunkt per månad och vi vill ha antal år (som flyttal).
    t = np.arange(y.size) / 12
    return t, y


def main():
    """Uppgift 3 - minsta kvadratmetoden
   
    Svar på frågor:
   
    a) Samband mellan RMS-fel och residualvektor:
       Normen av residualvektorn r i minstakvadratanpassningen ges av
       ||r||_2 = sqrt(sum( (f(t_i) - y_i)^2 )).
       RMS-felet är E_RMS = sqrt((1/N) * sum( (f(t_i) - y_i)^2 )).
       Därför är sambandet E_RMS = (1/sqrt(N)) * ||r||_2.

    c1) KPI-ökning per år (trend):
        Koefficienten för lutningen (trenden) från a) är cirka 3.53 KPI-enheter per år.
        De andra modellerna (multipel linjär och ickelinjär) ger mycket snarlika slope-värden
        på ca 3.49 resp 3.50. Resultaten för den långsiktiga uppåtgående trenden är
        alltså ganska lika och inte väsentligt annorlunda.

    c2) Jämförelse av RMS-felen:
        - Enkel linjär modell: Störst RMS-fel (ca 4.13)
        - Multipel linjär modell: Mindre RMS-fel (ca 3.21)
        - Ickelinjär modell (Gauss-Newton): Minst RMS-fel (ca 3.20)
    """
    t, y = load_data()
    # t -- antal år efter januari 1980 (en datapunkt per månad)
    # y -- konsumentprisindex (KPI)

    # Plotta all data (från januari 1980 till december 2025).
    # Denna anropades innan figur 1 startades så matplolib skapade figuren automatiskt.
    # plt.plot(t+1980, y)

    # Välj datan från januari 1991 till december 2020.
    I = (t+1980 >= 1991) & (t+1980 < 2021)
    data = Data(t[I], y[I])

    # Enkel linjär modell
    simple_design = lambda t: np.column_stack((
        np.ones(len(t)),
        t,
    ))
    simple_design_str = "Enkel linjär modell: f(t) = c₀ + c₁*t"
    simple_params = ("intercept", "slope")
    model1 = LinearModel(data, simple_design, simple_params, simple_design_str)
    print(model1)

    # Multipel linjär modell
    L = 8
    multiple_design = lambda t: np.column_stack((
        np.ones(len(t)), t, np.sin(2*np.pi*t/L), np.cos(2*np.pi*t/L)
    ))
    multiple_params = ("intercept", "slope", "sin amplitude", "cos amplitude")
    multiple_design_str = f"Multipel linjär modell: f(t) = c₀ + c₁*t + c₂*sin(2πt/{L}) + c₃*cos(2πt/{L})"
    model2 = LinearModel(data, multiple_design, multiple_params, multiple_design_str)
    print(model2)

    # Ickelinjär modell (Gauss-Newton)
    F = lambda c, t, y: c[0] + c[1]*t + c[2]*np.sin(2*np.pi*t/c[4]) + c[3]*np.cos(2*np.pi*t/c[4]) - y
    J = lambda c, t: np.column_stack((
        np.ones(len(t)),
        t,
        np.sin(2*np.pi*t/c[4]),
        np.cos(2*np.pi*t/c[4]),
        -(2*np.pi*t / c[4]**2) * (c[2]*np.cos(2*np.pi*t/c[4]) - c[3]*np.sin(2*np.pi*t/c[4]))
    ))
    model_fn = lambda c, t: c[0] + c[1]*t + c[2]*np.sin(2*np.pi*t/c[4]) + c[3]*np.cos(2*np.pi*t/c[4])
    nonlin_design_str = f"Ickelinjär modell: f(t) = c₀ + c₁*t + c₂*sin(2πt/c₄) + c₃*cos(2πt/c₄)"
    nonlin_params = ("intercept", "slope", "sin amplitude", "cos amplitude", "period")
   
    guess = np.append(model2.params.vec, L)
    model3 = NonlinearModel(data, F, J, model_fn, nonlin_params, nonlin_design_str, initial_guess=guess)
    print(model3)

    # Plotta alla tre modellerna.
    plot_all(t, y, data, model1, model2, model3)


if __name__ == "__main__":
    main()
    plt.show()