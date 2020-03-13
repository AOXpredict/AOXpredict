# AOXpredict
This Repository includes the model file, descriptors file and descriptions of descriptors calculation.

# Contents

* Process of calculating indicators
  * ΔE<sub>inter</sub>
  * Steric
  * others
  

## Process of calculating descriptors

* ΔEinter: represents the energy difference between the prototype molecule and the intermediate, and is defined as:

             ΔEinter= (ETI - Esub - Ewater) × 627.509 (kcal/mol)

Where ETI, Esub and Ewater are the single-point energies of the intermediate, water, and substrate, respectively. All  geometries and energies were computed using the B3LYP density functional theory method implemented in the
Gaussian09 program package, in which all structures including water molecule were optimized with the 6-31G(d, p) basis set and the single-point energies were determined with the 6-311+G(2d,2p) basis set. No solvent model is considered during the calculation.

* Steric: 



             Steric = E2.8 – E3.0/3.2 (kJ/mol)

Where E<sub>2.8</sub> represents the energy when the substrate is 2.8 Å from the probe. Whereas, E<sub>3.0/3.2</sub> represents the lowest systematic energy usually with the distance between the substrate and probe as 3.0 Å or 3.2 Å. 

Steric is calculated with Coordinate Scan in MacroModel (MacroModel, version 9.8, Schrödinger, LLC, New York, NY, USA). In this case, the distance is between the hydrogen on the carbon of the potential site and the center carbon (“the carbon in the reaction wedge” in original paper) of the probe.The systematic energies of substrates and probe at different distances between 2.2 and 7.0 Å with a 0.2 Å increment were determined to approximate the steric hindrance between substrates and AOX.The coordinates of the probe, WB17, and the optimized compounds acquired from the last step were ionized at pH 7.4 using Schrodinger LigPrep (LigPrep, version 2.3, Schrödinger, LLC). During the scan, two angles were fixed at 180 degrees and ensured similar steric interaction for different shaped substrates. Three points define an angle, and these two angles are the one from the carbon in the reaction wedge to the H−C of the reacting bond, and from the carbon directly behind the carbon in the reaction wedge to the carbon in the reaction wedge and finally the carbon to be oxidized. The dihedral  O−C−C−N between the lower oxygen, the center carbon, the oxidized carbon and the adjacent nitrogen was held constant at 90 degrees. 5000 minimization at maximum interactions were performed, and other parameters in this module were used with default values. 

* others


The other descriptors are computed using Spartan’18 v. 1.2.0 with computational level as B3LYP/6-31G* in vacuum, which could be categorized as topological, physicochemical and electronic features. The detatiled list of all descriptors are presented in /Data/.


