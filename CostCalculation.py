import numpy as np

Prajwal = [100] #Food at reparo
Marianna = [125, 155.88]
Ashutosh = [50]
Deepsing = [325+65.68+20.05]
Bjoern = [0]

TotalCost = np.sum(Prajwal) + np.sum(Marianna) + np.sum(Ashutosh) + np.sum(Deepsing) + np.sum(Bjoern)
CostShared = round(TotalCost/5,2)

print("Total Cost:", TotalCost)
print("Cost Shared:", CostShared)

PrajwalPays = round(CostShared - np.sum(Prajwal),2)
MariannaPays = round(CostShared - np.sum(Marianna),2)
AshutoshPays = round(CostShared - np.sum(Ashutosh),2)
DeepsingPays = round(CostShared - np.sum(Deepsing),2)
BjornPays = round(CostShared - np.sum(Bjoern),2)


print("Mariana is Owed:", MariannaPays)
print("Ashutosh Pays:", AshutoshPays, " to Marianna")
print("Deepsing is Owed:", DeepsingPays)
print("Bjoern Pays:", BjornPays, " to Deepsign")

print("Prajwal Pays:", PrajwalPays )
print("Prajwal Pays:", PrajwalPays, " to Deepsing:", -(DeepsingPays+BjornPays))
print("Prajwal Pays:", PrajwalPays, " to Marianna:", -round(MariannaPays+AshutoshPays,2))






