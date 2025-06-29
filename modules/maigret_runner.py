import subprocess
import os
import json
import logging

def run_maigret(username, tool_paths, outdir="reports"):
    output_txt = os.path.join(outdir, f"{username}_maigret.txt")
    output_json = os.path.join(outdir, f"{username}_maigret.json")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        tool_paths["maigret"] + "/maigret.py",
        username,
        "-n",
        "--json", output_json
    ]

    try:
        if not os.path.exists(tool_paths["maigret"]):
            logging.error(f"Maigret tool path not found: {tool_paths["maigret"]}")
            return "Maigret tool path not found.\n", None
        logging.info(f"Running Maigret for {username}...")
        with open(output_txt, "w") as outfile:
            subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL, check=True)
        logging.info(f"Maigret scan completed for {username}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Maigret for {username}: {e}")
        return f"Error running Maigret: {e}\n", None
    except FileNotFoundError:
        logging.error("Maigret command not found. Make sure it\"s installed and in your PATH.")
        return "Maigret command not found. Make sure it\"s installed and in your PATH.\n", None
    except Exception as e:
        logging.error(f"An unexpected error occurred with Maigret for {username}: {e}")
        return f"An unexpected error occurred with Maigret: {e}\n", None

    profile_count = 0
    try:
        with open(output_json, "r") as f:
            data = json.load(f)
            profile_count = len(data)
    except FileNotFoundError:
        logging.error(f"Maigret JSON output file not found: {output_json}")
        return "Maigret JSON output file not found.\n", None
    except json.JSONDecodeError:
        logging.error(f"Error decoding Maigret JSON output for {username}.")
        return "Error decoding Maigret JSON output.\n", None
    except Exception as e:
        logging.error(f"Error reading Maigret JSON output for {username}: {e}")
        return f"Error reading Maigret JSON output: {e}\n", None
    summary = f"Maigret found {profile_count} detailed profiles.\n"
    return summary, output_txt
