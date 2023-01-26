import numpy as np
import pandas as pd
pd.read_csv("HEALTH_WFMI_26012023013130019.csv").loc[:, ["Country of origin", "Value"]].rename(columns={"Country of origin": "country", "Value": "number"}).drop(126).assign(percent=lambda x: x.number / sum(x.number)).sort_values("number", ascending=False).head(10)

