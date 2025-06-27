import subprocess
import os

def run_sherlock(username, outdir="reports"):
    output_path = os.path.join(outdir, f"{username}_sherlock.txt")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        "sherlock/sherlock.py",
        username,
        "--print-found",
        "--timeout", "10"
    ]

    with open(output_path, "w") as outfile:
        subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL)

    with open(output_path, "r") as f:
        lines = f.readlines()
        found = [line.strip() for line in lines if "https://" in line]

    summary = f"Sherlock found {len(found)} profiles.\n"
    return summary, output_path
