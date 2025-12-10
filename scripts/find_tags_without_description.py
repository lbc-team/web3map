from lbc_api import get_tag_info
from time import sleep

# Read manuals.md to get all main tag names
main_tags = []
with open('scripts/output/manuals.md', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:  # Skip empty lines
            continue

        # Split by colon to get main_tag_name
        if ':' in line:
            main_tag_name = line.split(':', 1)[0].strip()
            main_tags.append(main_tag_name)

print(f"Found {len(main_tags)} main tags in manuals.md")
print("=" * 60)

# Check each main tag for description
tags_without_description = []

for i, tag_name in enumerate(main_tags, 1):
    print(f"[{i}/{len(main_tags)}] Checking: {tag_name}...")

    tag_info = get_tag_info(tag_name)

    if tag_info:
        description = tag_info.get('description', '').strip() if tag_info.get('description') else ''

        if not description:
            tags_without_description.append(tag_name)
            print(f"  ❌ No description")
        else:
            print(f"  ✓ Has description")
    else:
        print(f"  ⚠️  Tag not found in database")
        tags_without_description.append(tag_name)

    # Sleep to avoid overwhelming the API
    sleep(0.5)

# Output results
print("\n" + "=" * 60)
print(f"Summary: {len(tags_without_description)} tags without description out of {len(main_tags)} total tags")
print("=" * 60)

if tags_without_description:
    print("\nTags without description:")
    for tag in tags_without_description:
        print(f"  - {tag}")

    # Save to file
    output_file = 'scripts/output/tags_without_description.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for tag in tags_without_description:
            f.write(f"{tag}\n")
    print(f"\nResults saved to: {output_file}")
else:
    print("\n✓ All tags have descriptions!")
