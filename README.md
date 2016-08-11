# Waveplates
Code to compute settings of lambda half and lambda quarter plates in Quantum State Tomography for biexciton exciton emmission.

The following experimental setup is assumed:

The signal first meets a lambda quarter plate and then a lambda half plate.
Then the signal meets a 50-50 beam splitter, splitting the signal into two paths.

The first path consists of a lambda quarter plate and a lambda half plate again.
The signal then meets a polarizer and reaches the detector.

The second path does not have any plates, there is only a polarizer and a detector.


In order to perform a Quantum State Tomography measurement, it is necessary to specify a complete set of 16 to be measured components. A full library for constructing such a set and for the data analysis can be found at: https://github.com/afognini/Tomography

An example for such a component is HH, where the horizontal polarisation is measured for both paths.
Another example is HD, in which the horizontal component of the polarisation is measured in the first path, but the diagonal component is measured in the second path.

Assuming that the wave plates are facing the source, this program calculates the exact angles of the plates for every component.
