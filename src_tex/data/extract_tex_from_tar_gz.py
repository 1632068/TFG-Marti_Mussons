import os
import gzip
import tarfile
import shutil

def decompress_gz_and_collect_tex(gz_folder, tex_output_folder):
    os.makedirs(tex_output_folder, exist_ok=True)

    tex_count = 0
    for file in os.listdir(gz_folder):
        if file.endswith(".gz"):
            gz_path = os.path.join(gz_folder, file)
            filename_base = os.path.splitext(file)[0]  # elimina .gz
            output_path = os.path.join(tex_output_folder, filename_base + ".tex")

            # Evitar col·lisions de noms
            counter = 1
            while os.path.exists(output_path):
                output_path = os.path.join(tex_output_folder, f"{filename_base}_{counter}.tex")
                counter += 1

            try:
                # 1. Descomprimir .gz → .tar temporal
                with gzip.open(gz_path, 'rb') as f_in:
                    with tarfile.open(fileobj=f_in) as tar:
                        # 2. Buscar el primer .tex
                        tex_member = next((m for m in tar.getmembers() if m.name.endswith(".tex")), None)
                        if tex_member is None:
                            print(f"🟡 No s'ha trobat cap .tex a {file}")
                            continue

                        tex_file = tar.extractfile(tex_member)
                        content = tex_file.read().decode('utf-8', errors='ignore')

                        with open(output_path, 'w', encoding='utf-8') as f_out:
                            f_out.write(content)
                            tex_count += 1
                            print(f"✅ Descomprimit: {file} → {output_path}")

            except Exception as e:
                print(f"⚠️ Error amb {file}: {e}")

    print(f"\nTotal fitxers .tex extrets: {tex_count}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extreu .tex de fitxers .tar.gz i els desa en una carpeta.")
    parser.add_argument("--input", required=True, help="Carpeta amb els fitxers .gz")
    parser.add_argument("--tex", required=True, help="Carpeta on desar els .tex resultants")
    args = parser.parse_args()

    decompress_gz_and_collect_tex(args.input, args.tex)
