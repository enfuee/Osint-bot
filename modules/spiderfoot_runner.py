import subprocess
import os

def run_spiderfoot(target, outdir="reports"):
    output_path = os.path.join(outdir, f"{target}_spiderfoot.csv")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        "spiderfoot/sf.py",
        "-s", target,
        "-m", "ALL",
        "-o", output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    line_count = 0
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            line_count = sum(1 for _ in f) - 1  # exclude header

    summary = f"SpiderFoot collected {line_count} OSINT entries.\n"
    return summary, output_path
