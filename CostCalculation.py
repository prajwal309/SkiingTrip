import numpy as np

Prajwal = [100] #Food at reparo
Marianna = [125, 155.88]
Ashutosh = [50]
Deepsing = [325+65.68+20.05]
Bjoern = [0]

TotalCost = np.sum(Prajwal) + np.sum(Marianna) + np.sum(Ashutosh) + np.sum(Deepsing) + np.sum(Bjoern)
CostShared = round(TotalCost/5,2)

print("*"*20)
print("Total Cost:", TotalCost)
print("Cost Shared:", CostShared)
print("*"*20)
print("\n\n")
PrajwalPays = round(CostShared - np.sum(Prajwal),2)
MariannaPays = round(CostShared - np.sum(Marianna),2)
AshutoshPays = round(CostShared - np.sum(Ashutosh),2)
DeepsingPays = round(CostShared - np.sum(Deepsing),2)
BjornPays = round(CostShared - np.sum(Bjoern),2)


print("Deepsing is Owed:", -DeepsingPays)
print("Mariana is Owed:", -MariannaPays)
print("Bjoern Pays:", BjornPays)
print("Ashutosh Pays:", AshutoshPays)
print("Prajwal Pays:", PrajwalPays )


print("\n\nAction Item:")
print("Bjoern Pays:", BjornPays, " to Deepsing")
print("Ashutosh Pays:", -MariannaPays, " to Marianna.")
print("Prajwal Pays:", PrajwalPays, " to Deepsing.")
print("Ashutosh Pays:", round(MariannaPays+AshutoshPays,2), " to Deepsing.")






