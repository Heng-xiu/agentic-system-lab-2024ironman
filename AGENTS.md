# AGENTS.md

Guidelines for AI coding agents and maintainers working on this repository.

## Project context

This repository is a Traditional Chinese learning and implementation lab for building Agentic AI systems with LangGraph and related tools. It was created for the 2024 iThome Ironman series and is organized as a day-by-day set of notebooks and examples.

The primary maintenance goal is to keep the examples useful, executable, and aligned with current versions of LangGraph, LangChain, OpenAI SDKs, local model tooling, and the surrounding AI application stack.

## Repository structure

Current high-level structure:

```text
.
├── README.md
├── LICENSE
├── .gitignore
└── notebooks/
    ├── Day01_...
    ├── Day02_...
    ├── ...
    ├── Day29_.../p2_streamlit_fastapi_streaming
    └── Day30_.../p3_fullstack_langgraph_server
```

Treat `notebooks/` as the source of truth for runnable educational examples. If a notebook depends on local files, external services, API keys, model servers, or databases, document those requirements near the relevant notebook or in a local README inside that example directory.

## Language and writing style

* Use Traditional Chinese for learner-facing explanations, README updates, issue templates, and documentation.
* Keep code comments concise and practical. Use English for API names, class names, function names, package names, and framework terminology when that is the normal technical convention.
* Preserve the educational tone of the project: explain why a change matters, not only what changed.
* Do not rewrite article/book-style material unless the task explicitly asks for editorial work.
* Avoid adding marketing language. Prefer concrete claims backed by repo behavior.

## Dependency and environment policy

There is currently no single repository-wide dependency lockfile. When adding or updating examples:

1. Prefer local dependency notes per notebook or example directory.
2. If a shared dependency file is added later, keep it minimal and reproducible.
3. Pin versions only when a version range is known to break the example.
4. Note incompatible version combinations explicitly.
5. Do not silently upgrade framework APIs across many notebooks without documenting the migration.

When an example uses paid or authenticated services, use environment variables and document them clearly, for example:

```bash
OPENAI_API_KEY=...
LANGSMITH_API_KEY=...
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_SECRET_KEY=...
MONGODB_URI=...
NEO4J_URI=...
```

Never commit real API keys, tokens, credentials, database URIs, `.env` files, notebooks containing secrets in outputs, or screenshots showing secrets.

## Notebook maintenance rules

When editing notebooks:

* Keep notebooks runnable from top to bottom whenever practical.
* Prefer small, focused cells over large cells that mix setup, business logic, and display code.
* Add a short markdown note when a notebook requires external setup such as Ollama, MongoDB, Neo4j, LangFuse, FastAPI, Streamlit, or cloud API access.
* Remove stale outputs if they make diffs noisy or expose secrets.
* Do not commit large generated artifacts, model files, vector indexes, local databases, or cache directories.
* If an upstream API changed, include a brief migration note in the notebook or surrounding README.
* Preserve the original learning sequence unless the task is explicitly about restructuring the course.

For changes that affect multiple notebooks, update them in a consistent order and describe the compatibility target in the pull request.

## Coding conventions

For Python examples:

* Prefer clear educational code over overly abstract production architecture.
* Use descriptive function and variable names.
* Keep external service calls isolated so readers can replace them easily.
* Prefer explicit configuration through environment variables.
* Add lightweight error messages for missing optional dependencies or missing environment variables.
* Avoid hidden global state unless it is part of the concept being taught.

For web examples:

* Keep FastAPI and Streamlit examples simple enough for learners to run locally.
* Document the expected startup command and local URL.
* Separate server, client, and graph/workflow logic where possible.
* Do not add deployment-specific configuration unless the example is explicitly about deployment.

## Validation checklist

Before proposing a change, run the checks that are relevant to the touched files.

For documentation-only changes:

```bash
git diff --check
```

For Python files, if any are added or modified:

```bash
python -m compileall .
```

For notebooks, validate at least the touched notebook manually. If the notebook can run without paid services, secrets, local model downloads, or long-running infrastructure, prefer executing it end to end:

```bash
jupyter nbconvert --to notebook --execute path/to/notebook.ipynb --output /tmp/executed-notebook.ipynb
```

If a notebook cannot be executed automatically, explain why in the pull request. Common acceptable reasons include external API keys, local Ollama models, MongoDB/Neo4j setup, LangFuse setup, or long-running examples.

For FastAPI/Streamlit examples, include the commands used to start the services and verify that the example loads.

## Pull request expectations

A good pull request should include:

* A clear summary of the change.
* The affected day/example path.
* The framework or package versions used for validation, when relevant.
* Screenshots or short logs for UI examples.
* Notes about skipped validation, if any.
* No unrelated formatting churn.

Keep PRs narrow. Prefer one conceptual fix per PR: dependency update, notebook repair, documentation improvement, or example refactor.

## Issue triage guidance

When helping triage issues, ask for or infer the following:

* Operating system and Python version.
* Notebook or example path.
* Package versions for LangGraph, LangChain, OpenAI SDK, and related tools.
* Full error traceback.
* Whether the user is running local models, cloud APIs, or both.
* Whether required environment variables are set.

Label or group issues by topic when possible:

* `notebook`
* `documentation`
* `dependency`
* `langgraph`
* `langchain`
* `openai-sdk`
* `ollama`
* `rag`
* `graphrag`
* `fastapi`
* `streamlit`
* `good first issue`

## Security and privacy

* Never request, print, or store user secrets.
* Replace secrets in examples with placeholders.
* Avoid committing notebook outputs that include prompts, logs, traces, API responses, user data, or database contents unless they are synthetic and safe.
* If a security issue is found, avoid publishing exploit details in a public issue. Open a minimal issue asking the maintainer for a private coordination path.

## Maintainer automation ideas

AI agents may help with the following maintenance tasks:

* Update notebooks to current LangGraph and LangChain APIs.
* Add smoke-test instructions for examples.
* Normalize environment variable documentation.
* Generate issue and PR templates.
* Draft migration notes for breaking dependency changes.
* Review notebooks for leaked credentials or stale outputs.
* Improve README navigation across Day01-Day30.
* Prepare release notes and changelog entries.

Do not perform broad rewrites or dependency migrations without a focused task description.
