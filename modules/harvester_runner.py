import subprocess
import os

def run_theharvester(domain, outdir="reports"):
    output_path = os.path.join(outdir, f"{domain}_harvest.txt")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        "theHarvester/theHarvester.py",
        "-d", domain,
        "-b", "all",
        "-f", os.path.join(outdir, domain)
    ]

    with open(output_path, "w") as outfile:
        subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL)

    email_count = 0
    subdomain_count = 0
    with open(output_path, "r") as f:
        for line in f:
            if "Found email:" in line:
                email_count += 1
            elif "Found host:" in line:
                subdomain_count += 1

    summary = f"theHarvester found {email_count} emails, {subdomain_count} subdomains.\n"
    return summary, output_path
