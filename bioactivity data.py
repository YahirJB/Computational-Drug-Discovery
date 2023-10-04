# Import necessary libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client

# Target search for Leptospira
target = new_client.target
target_query = target.search('Leptospira')
targets = pd.DataFrame.from_dict(target_query)
targets
selected_target = targets.target_chembl_id[0]
selected_target
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="Survival")
df = pd.DataFrame.from_dict(res)
df.head(3)
df.standard_type.unique()
df.to_csv('bioactivity_data.csv', index=False)
