/*          ---  The Izhikevich Model  ---

Bifurcation methodologies enable us to reduce many biophysically accurate Hodgkin–Huxley-type neuronal models 
to a two-dimensional (2-D) system of ordinary differential equations of the form:
          v' = 0.04v** + 5v + 140 - u + I 
          u' = a(bv - u)
      with the auxiliary after-spike resetting:
          if v >= 30 mV, then v = c and u = u + d

Here, v and u are dimensionless variables, and a, b, c, and d are dimensionless parameters, and '= d/dt, 
where t is the time. The variable v represents the membrane potential of the neuron and u represents a membrane 
recovery variable, which accounts for the activation of K+ ionic currents and inactivation of Na+ ionic currents, 
and it provides negative feedback to v. After the spike reaches its apex (+30 mV), the membrane voltage and the 
recovery variable are reset. Synaptic currents or injected DC-currents are delivered via the variable I.

As most real neurons, the model does not have a fixed threshold; Depending on the history of the membrane potential 
prior to the spike, the threshold potential can be as low as -55 mV or as high as -40mV

• The parameter a describes the time scale of the recovery variable u. 
  Smaller values result in slower recovery. A typical value is a = 0:02.
  
• The parameter b describes the sensitivity of the recovery variable u 
  to the subthreshold fluctuations of the membrane potential v.
  Greater values couple v and u more strongly resulting in possible 
  subthreshold oscillations and low-threshold spiking dynamics. 
  A typical value is b = 0:2. The case b < a(b > a) corresponds to saddle-node (Andronov–Hopf) 
  bifurcation of the resting state

• The parameter c describes the after-spike reset value of the membrane potential v caused
  by the fast high-threshold K+ conductances. 
  A typical value is c = -65mV

• The parameter d describes after-spike reset of the recovery variable u caused by slow 
  high-threshold Na+ and K+ conductances.
  A typical value is d = 2.

*/

// From Iziekevich.org - see also https://www.izhikevich.org/publications/figure1.pdf:
float TonicSpiking[] = {0.02, 0.2, -65, 6, 14};
float PhasicSpiking[] = {0.02, 0.25, -65, 6, 0.5};
float TonicBursting[] = {0.02, 0.2, -50, 2, 15};
float PhasicBursting[] = {0.02, 0.25, -55, 0.05, 0.6};
float MixedMode[] = {0.02, 0.2, -55, 4, 10};
float SpikeFrequencyAdaptation[] = {0.01, 0.2, -65, 8, 30};


float Array_a[] = { 
  TonicSpiking[0],
  PhasicSpiking[0],
  TonicBursting[0],
  PhasicBursting[0],
  MixedMode[0],
  SpikeFrequencyAdaptation[0]
  }; 
  
float Array_b[] = { 
  TonicSpiking[1],
  PhasicSpiking[1],
  TonicBursting[1],
  PhasicBursting[1],
  MixedMode[1],
  SpikeFrequencyAdaptation[1]
  };     
    
float Array_c[] =  { 
  TonicSpiking[2],
  PhasicSpiking[2],
  TonicBursting[2],
  PhasicBursting[2],
  MixedMode[2],
  SpikeFrequencyAdaptation[2]
  }; 
  
float Array_d[] =  { 
  TonicSpiking[3],
  PhasicSpiking[3],
  TonicBursting[3],
  PhasicBursting[3],
  MixedMode[3],
  SpikeFrequencyAdaptation[3]
  }; 
