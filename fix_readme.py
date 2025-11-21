import re

with open('README.md', 'r') as f:
    content = f.read()

# Fix TOC
content = content.replace('## Table of Contents', '## Contents')

# Fix typos
content = content.replace('Typescript', 'TypeScript')
content = content.replace('Javascript', 'JavaScript')
content = re.sub(r'NodeJS\b', 'Node.js', content)
content = content.replace('DynamoDb', 'DynamoDB')

# Fix emoji in title
content = content.replace('# Awesome DynamoDB 🚀', '# Awesome DynamoDB')

# Fix list items - replace "). " with ") - " but preserve structure
lines = content.split('\n')
fixed_lines = []

for line in lines:
    original_line = line
    # Only process list items that start with "- ["
    if line.strip().startswith('- ['):
        # Find the pattern ](...). Description
        line = re.sub(r'\]\(([^)]+)\)\.\s+', r'](\1) - ', line)
        # Also handle ](...) Description (no period)
        if line == original_line:  # Only if not already fixed
            # Match pattern like ](url) Description where Description starts with capital letter
            line = re.sub(r'\]\(([^)]+)\)\s+([A-Z])', r'](\1) - \2', line)
    
    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

# Fix specific issues found by lint
# Line 60: Add space after period
content = content.replace('](https://www.npmjs.com/package/dynoport).A CLI', '](https://www.npmjs.com/package/dynoport) - A CLI')

# Add periods where missing at end of descriptions
lines = content.split('\n')
fixed_lines = []
for line in lines:
    if line.strip().startswith('- [') and '](' in line and ') - ' in line:
        # Check if ends with period
        if not line.rstrip().endswith('.') and not line.rstrip().endswith(')'):
            line = line.rstrip() + '.'
    fixed_lines.append(line)
content = '\n'.join(fixed_lines)

# Fix "is" at start (should be dash)
content = re.sub(r'\- \[Alternator\]\([^)]+\) is ', r'- [Alternator](https://github.com/scylladb/scylla/blob/master/docs/alternator/alternator.md) - ', content)
content = re.sub(r'\- \[typesafe-dynamodb\]\([^)]+\) provides ', r'- [typesafe-dynamodb](https://github.com/sam-goodwin/typesafe-dynamodb) - Provides ', content)
content = re.sub(r'\- \[SenseDeep\]\([^)]+\) includes ', r'- [SenseDeep](https://www.sensedeep.com/blog/posts/stories/dynamodb-studio.html) - Includes ', content)

# Fix item names repeating in description
content = re.sub(r'NoSQL Architect is a fully', r'A fully', content)
content = re.sub(r'DynamoSharp is an ORM', r'An ORM', content)

# Fix lowercase starts
content = re.sub(r'\) - ddbsh is', r') - A simple CLI for DynamoDB modeled on isql and the MySQL CLIs.', content)

with open('README.md', 'w') as f:
    f.write(content)

print("All fixes applied!")
