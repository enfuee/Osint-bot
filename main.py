import argparse
import os
from modules.sherlock_runner import run_sherlock
from modules.maigret_runner import run_maigret
from modules.harvester_runner import run_theharvester
from modules.spiderfoot_runner import run_spiderfoot
from utils import telegram

def main():
    parser = argparse.ArgumentParser(description="OSINT CLI + Telegram")
    parser.add_argument("--target", required=True, help="Username atau domain target")
    parser.add_argument("--mode", choices=["username", "domain", "all"], default="all")
    args = parser.parse_args()

    target = args.target
    mode = args.mode

    os.makedirs("reports", exist_ok=True)
    summary_lines = []
    file_list = []

    if mode in ["username", "all"]:
        sherlock_summary, sherlock_file = run_sherlock(target)
        summary_lines.append(sherlock_summary)
        file_list.append(sherlock_file)

        maigret_summary, maigret_file = run_maigret(target)
        summary_lines.append(maigret_summary)
        file_list.append(maigret_file)

    if mode in ["domain", "all"]:
        harvester_summary, harvester_file = run_theharvester(target)
        summary_lines.append(harvester_summary)
        file_list.append(harvester_file)

        spider_summary, spider_file = run_spiderfoot(target)
        summary_lines.append(spider_summary)
        file_list.append(spider_file)

    summary_path = f"reports/{target}_summary.md"
    with open(summary_path, "w") as f:
        f.write(f"# OSINT Summary for {target}\n\n")
        f.writelines(summary_lines)

    file_list.insert(0, summary_path)

    telegram.send_message(f"🕵️ OSINT Scan selesai untuk `{target}`")
    for path in file_list:
        telegram.send_file(path)

if __name__ == "__main__":
    main()
