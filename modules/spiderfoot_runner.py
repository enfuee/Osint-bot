import subprocess
import os
import logging

def run_spiderfoot(target, tool_paths, outdir="reports"):
    output_path = os.path.join(outdir, f"{target}_spiderfoot.csv")
    os.makedirs(outdir, exist_ok=True)

    cmd = [
        "python3",
        tool_paths["spiderfoot"] + "/sf.py",
        "-s", target,
        "-m", "ALL",
        "-o", output_path
    ]

    try:
        if not os.path.exists(tool_paths["spiderfoot"]):
            logging.error(f"SpiderFoot tool path not found: {tool_paths["spiderfoot"]}")
            return "SpiderFoot tool path not found.\n", None
        logging.info(f"Running SpiderFoot for {target}...")
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        logging.info(f"SpiderFoot scan completed for {target}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running SpiderFoot for {target}: {e}")
        return f"Error running SpiderFoot: {e}\n", None
    except FileNotFoundError:
        logging.error("SpiderFoot command not found. Make sure it\"s installed and in your PATH.")
        return "SpiderFoot command not found. Make sure it\"s installed and in your PATH.\n", None
    except Exception as e:
        logging.error(f"An unexpected error occurred with SpiderFoot for {target}: {e}")
        return f"An unexpected error occurred with SpiderFoot: {e}\n", None

    line_count = 0
    try:
        if os.path.exists(output_path):
            with open(output_path, "r") as f:
                line_count = sum(1 for _ in f) - 1  # exclude header
    except FileNotFoundError:
        logging.error(f"SpiderFoot output file not found: {output_path}")
        return "SpiderFoot output file not found.\n", None
    except Exception as e:
        logging.error(f"Error reading SpiderFoot output for {target}: {e}")
        return f"Error reading SpiderFoot output: {e}\n", None
    summary = f"SpiderFoot collected {line_count} OSINT entries.\n"
    return summary, output_path
