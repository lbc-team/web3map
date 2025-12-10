

from lbc_api import setmain_tag
from time import sleep

# Read manuals.md and process each line
def update_main_tag():
    with open('scripts/output/manuals.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            # Split by colon to get main_tag_name and sub_tag_names
            if ':' in line:
                main_tag_name, sub_tag_names = line.split(':', 1)
                main_tag_name = main_tag_name.strip()
                sub_tag_names = sub_tag_names.strip()

                # Call setmain_tag for each entry
                print(f"Processing: {main_tag_name} -> {sub_tag_names}")
                setmain_tag(main_tag_name, sub_tag_names)
                sleep(2)
            else:
                print(f"Skipping line without colon: {line}")

    print("All tags processed successfully!")


if __name__ == "__main__":
    # update_main_tag()
    setmain_tag("Front-running", "抢跑交易,抢跑")