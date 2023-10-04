bioactivity_class = []
for i in df2.standard_value:
  if float(i) >= 10000:
    bioactivity_class.append("inactive")
  elif float(i) <= 1000:
    bioactivity_class.append("active")
  else:
    bioactivity_class.append("intermediate")
mol_cid = []
for i in df2.molecule_chembl_id:
  mol_cid.append(i)
canonical_smiles = []
for i in df2.canonical_smiles:
  canonical_smiles.append(i)
standard_value = []
for i in df2.standard_value:
  standard_value.append(i)
data_tuples = list(zip(mol_cid, canonical_smiles, bioactivity_class, standard_value))
df3 = pd.DataFrame( data_tuples,  columns=['molecule_chembl_id', 'canonical_smiles', 'bioactivity_class', 'standard_value'])
