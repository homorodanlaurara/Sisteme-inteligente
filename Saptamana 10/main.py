import pandas as pd
import os

def smartphoneusage(file_path):
    if not os.path.exists(file_path):
        print(f"fisierul'{file_path}' nu a fost gasit")
        return None
    
    #incarcarea datelor
    df = pd.read_csv(file_path)
    print("Analiza dependentei de Smartphone")
    print(f"{df.shape[0]} randuri si {df.shape[1]} coloane.\n")
    
    #analiza
    print("Statistici Generale")
    #media orelor de ecran
    avg_screen_time = df['daily_screen_time_hours'].mean()
    print(f"Media timpului petrecut pe ecran: {avg_screen_time:.2f} ore/zi")
    
    #cati utilizatori sunt considerati addicted (coloana addicted_label)
    addicted_count = df['addicted_label'].sum()
    print(f"utilizatori cu potentiala adictie: {addicted_count}")
    
    #verificam valori lipsa
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("\nvalori lipsa detectate")
        print(missing[missing > 0])
    else:
        print("\nnu exista valori lipsa.")
        
    return df

if __name__ == "__main__":
    FILE_NAME = 'smartphoneusage.csv'
    
    df_smartphone = smartphoneusage(FILE_NAME)
    
    if df_smartphone is not None:
        print("\nPrimele 5 randuri")
        print(df_smartphone.head())
