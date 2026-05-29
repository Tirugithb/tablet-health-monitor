import pandas as pd

def export_excel(apps):
    df = pd.DataFrame(apps.items(), columns=["App", "Version"])
    df.to_excel("tablet_apps.xlsx", index=False)
