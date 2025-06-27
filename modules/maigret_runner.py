import subprocess
import os

def run_maigret(username, outdir="reports"):
    output_txt = os.path.join(outdir, f"{username}_maigret.txt")
    output_json = os.path.join(outdir, f"{username}_maigret.json")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        "maigret/maigret.py",
        username,
        "-n",
        "--json", output_json
    ]

    with open(output_txt, "w") as outfile:
        subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL)

    profile_count = 0
    with open(output_txt, "r") as f:
        for line in f:
            if line.startswith("[+]") and "account was found" in line:
                profile_count += 1

    summary = f"Maigret found {profile_count} detailed profiles.\n"
    return summary, output_txt
