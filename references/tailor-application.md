---
name: Tailor Application
description: Ingests JDs and tailors resume bullets and cover letters to target positions.
code: TA
---

**Language:** Use {communication_language} for all content and output.

# Tailor Application

## What Success Looks Like

A highly aligned resume and cover letter that mirrors the target job description's keywords and outcomes without losing the owner's unique voice. Bullets must follow the formula: **Active Verb + Project/Context + Metric/Outcome**. 

## Your Approach

1. **Ingest & Parse**:
   - Ask the owner for the target company, target role, and path to the Job Description (JD) file (or paste the JD directly).
   - Read the master resume and cover letter YAML files from the paths defined in `BOND.md`.
2. **Gap Analysis & Critical Check**:
   - Compare the JD's core requirements against the master resume library.
   - **Trigger Interview for Missing Skills**: If the JD requires a critical skill, tool, or achievement type that is completely missing from the master resume, **do not proceed** with tailoring. Instead, halt and immediately invoke `[IM] Interview Missing Experience` to query the owner for hidden experience, drafting a new bullet point before resuming this capability.
3. **Tailoring & Rewriting**:
   - For matching experience, invoke `[RL] Rewrite Library Lines` to translate your master resume accomplishments into the specific phrasing, keywords, and action verbs preferred by the JD.
   - Structure tailored bullets to emphasize achievements that prove matching competencies.
4. **Draft Cover Letter**:
   - Write a highly tailored, non-generic cover letter highlighting the top 2-3 matching experiences from the resume that directly answer the JD's biggest pain points.
5. **Present & Review**:
   - Show a side-by-side comparison of the original master bullet points vs. the newly tailored ones.
   - Ask the user for feedback.
6. **Generate Output Artifacts**:
   - Once approved, create the application folder: `{project-root}/applications/YYYY-MM-DD-company-title/` (where `company` and `title` are slugified/lowercased, e.g. `2026-06-06-google-senior-developer`).
   - Save the raw job description text to `{project-root}/applications/YYYY-MM-DD-company-title/job-description.txt`.
   - Load `RESUME-template.md` from the sanctum root. Extract the owner's contact info, links, education, and skills list directly from the master resume YAML file. Format the final tailored resume by populating `RESUME-template.md` with these extracted details alongside the newly tailored work experiences, then save it to `{project-root}/applications/YYYY-MM-DD-company-title/resume.md`.
   - Load `COVER-LETTER-template.md` from the sanctum root. Extract the owner's contact details from the master cover letter (or resume) YAML file. Format the final cover letter by populating `COVER-LETTER-template.md` with these details, the current date, target company/role, salutation, tailored body paragraphs, and sign-off, then save it to `{project-root}/applications/YYYY-MM-DD-company-title/cover-letter.md`.
   - Proceed to `[HU] Harvest Updates` to save the new tailored variations back to the master database.

## Memory Integration

* Check `BOND.md` to see the owner's coaching and voice style preferences.
* Check `MEMORY.md` to review successful patterns from past tailoring sessions.

## Wrapping Up

* Present the tailored resume bullets and cover letter drafts in clear, readable markdown.
* Ask: *"Would you like to make any adjustments to this phrasing, or shall we merge these variations into your master database?"*
* Keep track of the target company and role in the session notes.
