from reports.models import Art, ArtCall
querySet = ArtCall.objects.filter(has_arv='No')

patients = {}
i = 0
for patient in querySet:
	item = {i:patient}
	patients.update(item)
	i+=1
	print(i, patient)

print(patients)

for item in patients.items():
	print(item)