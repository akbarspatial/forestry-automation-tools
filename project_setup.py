import os
import datetime

def create_project_structure(project_name):
    """
    Membuat struktur folder standar untuk proyek GIS/Kehutanan.
    Standard: ISO 19115 (Metadata) inspired structure.
    """
    # Dapatkan tanggal hari ini
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Nama folder utama
    base_folder = f"{today}_{project_name}"
    
    # Struktur folder standar Kehutanan
    subfolders = [
        "01_Spatial_Data/SHP",
        "01_Spatial_Data/Raster",
        "01_Spatial_Data/GPS_Raw",
        "02_Tabular_Data",
        "03_Maps_Layout/PDF",
        "03_Maps_Layout/JPG",
        "04_Reports_Docs",
        "05_Scripts_Toolbox"
    ]
    
    try:
        # Buat folder utama
        os.makedirs(base_folder)
        print(f"[SUCCESS] Project Base Created: {base_folder}")
        
        # Buat subfolder
        for folder in subfolders:
            path = os.path.join(base_folder, folder)
            os.makedirs(path)
            print(f"  ├── Created: {folder}")
            
        print("\n[INFO] Siap digunakan untuk analisis GIS.")
        
    except FileExistsError:
        print(f"[ERROR] Folder '{base_folder}' sudah ada.")

if __name__ == "__main__":
    print("--- GIS Project Structure Generator ---")
    p_name = input("Masukkan Nama Proyek (tanpa spasi): ")
    create_project_structure(p_name)
