import subprocess
import os
import logging

def run_theharvester(domain, tool_paths, outdir="reports"):
    output_path = os.path.join(outdir, f"{domain}_harvest.txt")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        tool_paths["theharvester"] + "/theHarvester.py",
        "-d", domain,
        "-b", "all",
        "-f", os.path.join(outdir, domain)
    ]

    try:
        if not os.path.exists(tool_paths["theharvester"]):
            logging.error(f"theHarvester tool path not found: {tool_paths["theharvester"]}")
            return "theHarvester tool path not found.\n", None
        logging.info(f"Running theHarvester for {domain}...")
        with open(output_path, "w") as outfile:
            subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL, check=True)
        logging.info(f"theHarvester scan completed for {domain}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running theHarvester for {domain}: {e}")
        return f"Error running theHarvester: {e}\n", None
    except FileNotFoundError:
        logging.error("theHarvester command not found. Make sure it\"s installed and in your PATH.")
        return "theHarvester command not found. Make sure it\"s installed and in your PATH.\n", None
    except Exception as e:
        logging.error(f"An unexpected error occurred with theHarvester for {domain}: {e}")
        return f"An unexpected error occurred with theHarvester: {e}\n", None

    email_count = 0
    subdomain_count = 0
    try:
        with open(output_path, "r") as f:
            for line in f:
                if "Found email:" in line:
                    email_count += 1
                elif "Found host:" in line:
                    subdomain_count += 1
    except FileNotFoundError:
        logging.error(f"theHarvester output file not found: {output_path}")
        return "theHarvester output file not found.\n", None
    except Exception as e:
        logging.error(f"Error reading theHarvester output for {domain}: {e}")
        return f"Error reading theHarvester output: {e}\n", None
    summary = f"theHarvester found {email_count} emails, {subdomain_count} subdomains.\n"
    return summary, output_path
