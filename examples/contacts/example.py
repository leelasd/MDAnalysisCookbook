
import MDAnalysis
from MDAnalysis import Universe
from MDAnalysis.analysis.contacts import calculate_contacts
import numpy as np
import pandas as pd

ref = Universe("conf_protein.gro.bz2")
u = Universe("conf_protein.gro.bz2", "traj_protein_0.xtc")

x = len(ref.select_atoms("protein"))
selA = "not name H* and resid 72-95 and bynum {}:{}".format(1, x//2)
selB = "not name H* and resid 72-95 and bynum {}:{}".format(x//2, x)


data = calculate_contacts(ref, u, selA, selB)
df = pd.DataFrame(data, columns=["Time (ps)", "Q"])
print(df)
