import zipfile

jar_path = "zemberek-full.jar"

with zipfile.ZipFile(jar_path, "r") as jar:
    print(f"📦 İçindekiler: {jar_path}")
    for name in jar.namelist():
        if name.endswith(".class") and "morphology" in name:
            print(name)
