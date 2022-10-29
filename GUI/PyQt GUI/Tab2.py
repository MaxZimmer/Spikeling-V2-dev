import numpy as np
import pyqtgraph

DarkSolarized = [[0,30,38],[131,148,150],[220,50,47],[38,139,210],[133,153,0]]

class Tab2():

    def DrawNeuron(self):
        self.Oscilloscope2.clear()
        a = float(self.a_Izhikevich.text())
        b = float(self.b_Izhikevich.text())
        c = float(self.c_Izhikevich.text())
        d = float(self.d_Izhikevich.text())
        t = 0.0
        time = 250
        time1 = 50
        time2 = 200
        dt = 1.0 / 200.0
        ntime = int(time / dt) + 1
        ntime1 = int(time1 / dt)
        ntime2 = int(time2 / dt)
        v = -65.0
        v_thresh = 30.0
        I_dc = 15.0
        u = 0.0
        vs = []
        nt = np.linspace(0, time, ntime)
        while t < time:
            vs.append(v)
            dv = (0.04 * v * v) + (5.0 * v) + 140.0 - u
            du = a * ((b * v) - u)
            if t > 50.0 and t < 200:
                dv += I_dc
            v += dv * dt
            u += du * dt
            if v >= v_thresh:
                v = c
                u = u + d
            t += dt

        nstim = np.zeros(ntime)
        nstim[:] = -80
        nstim[ntime1:ntime2] = -20

        self.Oscilloscope2.plot(nt, nstim, pen=(DarkSolarized[3]))
        self.Oscilloscope2.plot(nt, vs, pen=(DarkSolarized[2]))
        self.Oscilloscope2.setBackground(DarkSolarized[0])
        self.Oscilloscope2.showGrid(x=True, y=True)
