# Job Application Tailor

An outcome-driven, memory-enabled BMad agent that acts as a warm career coach and precise professional editor to tailor resumes and cover letters. It is 100% LLM-driven and features a Python-based YAML validation gate to secure database integrity.

---

## Getting Started

### Clone the Repository

Clone this repository directly into the appropriate folder of your AI client tool:

```bash                                                                                                           
git clone https://github.com/vJourneyman/agent-job-app-tailor.git
```

## Installation & Setup

This skill is fully standalone and can be copied into the skills folder of your preferred AI client. Follow the guide below for your environment:

### Where to Copy the Files

I usually dedicate an entire directory for my job applications as a project. That's what we'll call the `{project-root}`. For example, I might put that in `~/projects/job-search-YYYY/`

Copy the entire `agent-job-app-tailor` skill folder into the appropriate directory relative to your project root:

| Client Tool | Installation Folder |
| :--- | :--- |
| **antigravity-cli** | `{project-root}/.agent/skills/agent-job-app-tailor/` |
| **gemini-cli** | `{project-root}/.gemini/skills/agent-job-app-tailor/` |
| **Claude Code** | `{project-root}/.claude/skills/agent-job-app-tailor/` |

*Tip: For local development, you can create a symlink to this folder to see changes update in real-time.*

---

## How to Instantiate (Run) the Agent

After copying the files, launch your AI client and prompt it to start the agent. Below are environment-specific instructions for each client:

### 1. antigravity-cli

* **Interactive CLI**:
  Run the command in your project root:
  ```bash
  agy
  ```
  *(or `agy` if configured as a shell alias)*
  
  Once in the interactive prompt, instantiate the agent by asking:
  > Please activate the Job Application Tailor.

* **Python SDK Programmatic Mode**:
  If you are instantiating the agent programmatically inside a Python project, configure it to load the skill directory:
  ```python
  from google.antigravity import Agent, LocalAgentConfig

  # Config to auto-load the skill
  config = LocalAgentConfig(
      skills_paths=["./.agent/skills"]
  )

  async with Agent(config) as agent:
      response = await agent.chat("Please activate the Job Application Tailor.")
      print(await response.text())
  ```

### 2. gemini-cli

* **Interactive CLI**:
  Run the command in your project root:
  ```bash
  gemini-cli
  ```
  *(or `gemini` if configured as a shell alias)*
  
  Once in the interactive prompt, instantiate the agent by asking:
  > Please activate the Job Application Tailor.

### 3. Claude Code

* **Interactive CLI**:
  Run the command in your project root:
  ```bash
  claude
  ```
  
  Once in the interactive prompt, instantiate the agent by instructing:
  > Please read the instructions in .claude/skills/agent-job-app-tailor/SKILL.md and activate the Job Application Tailor.

---

## First-Run Initialization

Once the skill folder is in place, activate the agent in your AI client session.

Because this is a **Memory Agent**, it requires a *sanctum* (memory workspace) to store its persona, targets, career details, and session history. On the very first run, the agent will detect that its sanctum is missing and will:

1. Create its sanctum directories:
   * `{project-root}/_bmad/memory/agent-job-app-tailor/` (or fallback to `{project-root}/.agent/memory/agent-job-app-tailor/` if BMad is not installed).
2. Copy the templates from `assets/` and references from `references/` into the sanctum.
3. Automatically generate a list of its registered capabilities in the sanctum's `CAPABILITIES.md`.
4. Trigger the conversational **First Breath Onboarding** setup.

---

## Onboarding Conversation

During your first session, the agent will guide you through:
* Proposing or asking for its **Name**.
* Learning your **Target Roles, Companies, and Industries**.
* Confirming the file paths to your **Resume and Cover Letter YAML Libraries**.
* *Note: If you do not have YAML files set up, the agent will offer to ingest your raw text resumes/CLs to build them.*
* Aligning on the **Coaching-vs-Editing balance** (how direct or supportive you prefer the feedback to be).

---

## Job Application Tailoring Loop (Step-by-Step)

For each new position you apply to, follow this simple workflow loop with the agent:

### Step 1: Start the Session & Activate the Agent
Launch your AI client and command it to initialize the Tailor:
> Please activate the Job Application Tailor.

### Step 2: Provide the Job Details
When prompted, provide:
1. Target **Company Name** (e.g., `Google`)
2. Target **Role Title** (e.g., `Senior Systems Engineer`)
3. The **Job Description** (copy-paste it directly or provide a local path to the text file)

### Step 3: Address Missing Experience (Gap Interview)
The agent will scan the Job Description and compare it against your master resume library:
* **No gaps found**: The agent proceeds directly to tailoring.
* **Gaps found**: The agent will pause and ask you questions, one at a time, to find similar experience in your background. It will provide **3 conventional** and **3 creative spark examples** to help jog your memory and craft a new bullet point.                                                                                                   
                                                                                                                      
### Step 4: Review and Refine the Drafts
The agent will present:
* A side-by-side comparison of your original resume bullets vs. the newly tailored ones.
* A custom, tailored cover letter draft.

Review the phrasing and reply with any adjustments you want to make (e.g., *"Make the resume summary sound a bit more technical"* or *"Change the metric in the second bullet"*).

### Step 5: Save and Output
Once you approve the drafts, the agent automatically:
1. **Creates a Job Folder**: Generates `{project-root}/applications/YYYY-MM-DD-company-role/`.
2. **Saves Final Artifacts**: Writes `job-description.txt`, `resume.md` (formatted via `RESUME-template.md`), and `cover-letter.md` (formatted via `COVER-LETTER-template.md`) into the new folder.                                   
3. **Merges with Master Database**: Appends the approved tailored variations to your master YAML library files and
  runs validation scripts to guarantee data integrity.

---

## Folder Structure

```text
agent-job-app-tailor/
├── SKILL.md                         # Bootloader (routes to First Breath or Sanctum)
├── README.txt                       # This setup guide
├── customize.toml                   # Help & registry metadata
├── references/
│   ├── first-breath.md              # Configuration setup (custom career discovery)
│   ├── memory-guidance.md           # Session close & memory update instructions
│   ├── tailor-application.md        # Tailoring engine & missing experience check
│   ├── rewrite-library-lines.md     # Line rewriting using JD language
│   ├── interview-missing-experience.md # One-at-a-time interview with 6 sparks
│   ├── onboard-library.md           # Raw text to YAML converter
│   └── harvest-updates.md           # Merge engine with YAML validation
├── assets/
│   ├── INDEX-template.md            # Sanctum structure
│   ├── PERSONA-template.md          # Persona seed (cooperative coach + editor)
│   ├── CREED-template.md            # Seeds: validation rules, standing orders, boundaries
│   ├── BOND-template.md             # Seeds: career fields, voice, file paths
│   ├── MEMORY-template.md           # Seeds: tailored logs (starts empty)
│   ├── RESUME-template.md           # Formatting template for tailored resumes
│   └── COVER-LETTER-template.md     # Formatting template for tailored cover letters
└── scripts/
    └── validate_yaml.py             # Python YAML validation script (non-negotiable gate)
```

---

## Features & Capabilities

Once initialized, the agent exposes these main workflows:
* **Tailor Application `[TA]`**: Compiles tailored resume bullets and cover letter drafts. Creates a dedicated output folder `{project-root}/applications/YYYY-MM-DD-company-title/` containing `job-description.txt`, `resume.md`, and `cover-letter.md`.
* **Rewrite Library Lines `[RL]`**: Rewrites master library resume bullets using target JD language.
* **Interview Missing Experience `[IM]`**: Conversational gap-interview featuring 3 conventional and 3 creative spark answers.
* **Onboard Library `[OL]`**: Scaffolds structured YAML libraries from raw text inputs.
* **Harvest Updates `[HU]`**: Merges edits back to libraries and runs validation.
