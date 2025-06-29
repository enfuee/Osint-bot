import subprocess
import os
import logging

def run_sherlock(username, tool_paths, outdir="reports"):
    output_path = os.path.join(outdir, f"{username}_sherlock.txt")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        tool_paths["sherlock"] + "/sherlock.py",
        username,
        "--print-found",
        "--timeout", "10"
    ]

    try:
        if not os.path.exists(tool_paths["sherlock"]):
            logging.error(f"Sherlock tool path not found: {tool_paths["sherlock"]}")
            return "Sherlock tool path not found.\n", None
        logging.info(f"Running Sherlock for {username}...")
        with open(output_path, "w") as outfile:
            subprocess.run(cmd, stdout=outfile, stderr=subprocess.DEVNULL, check=True)
        logging.info(f"Sherlock scan completed for {username}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Sherlock for {username}: {e}")
        return f"Error running Sherlock: {e}\n", None
    except FileNotFoundError:
        logging.error("Sherlock command not found. Make sure it\"s installed and in your PATH.")
        return "Sherlock command not found. Make sure it\"s installed and in your PATH.\n", None
    except Exception as e:
        logging.error(f"An unexpected error occurred with Sherlock for {username}: {e}")
        return f"An unexpected error occurred with Sherlock: {e}\n", None

    try:
        with open(output_path, "r") as f:
            lines = f.readlines()
            found = [line.strip() for line in lines if "https://" in line]
    except FileNotFoundError:
        logging.error(f"Sherlock output file not found: {output_path}")
        return "Sherlock output file not found.\n", None
    except Exception as e:
        logging.error(f"Error reading Sherlock output for {username}: {e}")
        return f"Error reading Sherlock output: {e}\n", None
    summary = f"Sherlock found {len(found)} profiles.\n"
    return summary, output_path
