---
name: Harvest Updates
description: Parses chat logs/edits, diffs changes, validates YAML, and writes back to master files.
code: HU
---

**Language:** Use {communication_language} for all content and output.

# Harvest Updates

## What Success Looks Like

Approved tailored bullets or newly discovered accomplishments are successfully merged into the master YAML resume or cover letter library files. Formatting is preserved, and the YAML is validated and guaranteed to be syntactically correct.

## Your Approach

1. **Identify Approved Updates**:
   - Collect the specific tailored bullet points or profile changes that the owner has approved during the session.
2. **Merge Changes**:
   - Read the existing master YAML file from the path listed in `BOND.md`.
   - Perform the merge natively: locate the correct experience block, company, or section and insert the new tailored variation or new bullet point.
   - Write the updated YAML file back to disk.
3. **Execute YAML Validation Gate (Non-Negotiable)**:
   - Run the validation command immediately after writing the file:
     `python3 scripts/validate_yaml.py {file_path}`
   - **Self-Correction Loop**: If the validation script exits with a non-zero code, print the syntax error, read the file, locate the syntax error (such as a missing quote, incorrect indentation, or invalid character), correct it, write the file back, and re-run the validation script. Repeat this loop until validation reports success.
4. **Show Diffs**:
   - Present a clear, readable diff showing precisely what was added, removed, or modified in the master YAML libraries.

## Memory Integration

* Log the transaction (e.g., tailored resume bullets for [Role] at [Company]) in the session log `sessions/YYYY-MM-DD.md`.

## Wrapping Up

* Confirm the update: *"✓ Master YAML library successfully updated and validated."*
* Present the diff to the owner.
* When complete, notify the user and proceed to the next tailoring task or wrap up the session.
