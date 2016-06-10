from reports.models import Art, ArtCall
from datetime import date
querySet = ArtCall.objects.filter(has_arv='Yes')

patients = {}
i = 0
for patient in querySet:
	item = {i:patient}
	patients.update(item)
	i+=1

for item in patients.items():
	if(not item[1].art.age is None):
		print(item[1].art, item[1].art.gender, item[1].art.telephone_number, item[1].art.district)

def get_age(born):
	today = date.today()
	return today.year - born.year

print(get_age(item[1].art.age))
print(date.today())
print(item[1].art.age.year)