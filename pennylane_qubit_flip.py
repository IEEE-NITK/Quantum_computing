# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:29:48 2022

@author: Sujay
"""

import pennylane as qml
from pennylane import numpy as np

dev1 = qml.device('default.qubit', wires = 1)

@qml.qnode(dev1)
def circuit(params):
    qml.RX(params[0], wires = 0)
    qml.RY(params[1], wires = 0)
    return qml.expval(qml.PauliZ(0))

print(circuit([0.3, 0.7]))