---
name: Onboard Library
description: Converts raw text resumes and cover letters into initial structured YAML libraries.
code: OL
---

**Language:** Use {communication_language} for all content and output.

# Onboard Library

## What Success Looks Like

Raw, unstructured resume and cover letter text is converted into clean, standard, and syntactically valid YAML data libraries. The file paths are successfully registered in `BOND.md`.

## Your Approach

1. **Ingest Unstructured Text**:
   - Ask the owner to paste their raw text resume and/or cover letter.
   - Ask for the desired save paths (e.g., `{project-root}/data/user/resume_data.yaml` and `{project-root}/data/user/cover_letter_data.yaml`).
2. **Convert to YAML**:
   - Parse the raw text and structure it logically:
     * **Resume YAML schema**: Contact info, summary, skills list, and a list of job experiences (each with company, role, dates, and bullet points).
     * **Cover Letter YAML schema**: Structure paragraphs, contact details, salutation, and sign-off.
3. **Write and Validate (Non-Negotiable)**:
   - Write the YAML content to the specified file paths.
   - Run the validation command:
     `python3 scripts/validate_yaml.py {file_path}`
   - **Check Exit Code**: If the validation script fails (non-zero exit code), you must parse the error output, fix the YAML formatting directly in the file, and re-run the validation until it passes. Do not present invalid YAML to the user or save it as finished.
4. **Register Paths**:
   - Write the resolved YAML paths to `BOND.md` under the user preferences sections.

## Memory Integration

* Write the newly parsed career highlights, education, and credentials into `BOND.md` to establish the agent's baseline understanding of the owner.
* Update `INDEX.md` if this is the first time the library paths are registered.

## Wrapping Up

* Report the successful creation of the YAML libraries.
* Present a brief snippet of the structured YAML to the owner for validation.
* When complete, ask: *"Your master YAML library is created and validated. Ready to begin tailoring?"* and proceed to the tailoring step.
