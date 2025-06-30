import json
import argparse
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
from modules.sherlock_runner import run_sherlock
from modules.maigret_runner import run_maigret
from modules.harvester_runner import run_theharvester
from modules.spiderfoot_runner import run_spiderfoot

def main():
    parser = argparse.ArgumentParser(description="OSINT CLI")
    parser.add_argument("--target", required=True, help="Username atau domain target")
    parser.add_argument("--mode", choices=["username", "domain", "all"], default="all", help="Mode scan: username, domain, atau all")
    parser.add_argument("--tools", nargs="*", help="Pilih alat untuk dijalankan (sherlock, maigret, theharvester, spiderfoot). Kosongkan untuk menjalankan semua alat sesuai mode.")
    args = parser.parse_args()

    target = args.target
    mode = args.mode
    selected_tools = args.tools

    os.makedirs("reports", exist_ok=True)
    summary_lines = []
    file_list = []

    if mode in ["username", "all"]:
        if not selected_tools or "sherlock" in selected_tools:
            sherlock_summary, sherlock_file = run_sherlock(target)
            if sherlock_summary and sherlock_file:
                summary_lines.append(sherlock_summary)
                file_list.append(sherlock_file)
            else:
                summary_lines.append("Sherlock scan failed or returned no results.\n")

        if not selected_tools or "maigret" in selected_tools:
            maigret_summary, maigret_file = run_maigret(target)
            if maigret_summary and maigret_file:
                summary_lines.append(maigret_summary)
                file_list.append(maigret_file)
            else:
                summary_lines.append("Maigret scan failed or returned no results.\n")

    if mode in ["domain", "all"]:
        if not selected_tools or "theharvester" in selected_tools:
            harvester_summary, harvester_file = run_theharvester(target)
            if harvester_summary and harvester_file:
                summary_lines.append(harvester_summary)
                file_list.append(harvester_file)
            else:
                summary_lines.append("theHarvester scan failed or returned no results.\n")

        if not selected_tools or "spiderfoot" in selected_tools:
            spider_summary, spider_file = run_spiderfoot(target)
            if spider_summary and spider_file:
                summary_lines.append(spider_summary)
                file_list.append(spider_file)
            else:
                summary_lines.append("SpiderFoot scan failed or returned no results.\n")

    summary_path = f"reports/{target}_summary.md"
    with open(summary_path, "w") as f:
        f.write(f"# OSINT Summary for {target}\n\n")
        f.writelines(summary_lines)

    file_list.insert(0, summary_path)

if __name__ == "__main__":
    main()
