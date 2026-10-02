# Mason Lab Scripts

Shared Python scripts from the Mason Lab (Synthetic Biomimetic Compartments Research Group).

## Layout

```
scripts/
  <your-name>/
    <script-or-project>/
      script.py
      README.md          # what it does, inputs, outputs, example usage
      requirements.txt   # only if it needs third-party packages
```

Copy `scripts/_template/` as a starting point.

## How to contribute

1. Get added as a collaborator (ask a lab admin) and make a GitHub account if needed.
2. Create a branch: `git checkout -b yourname/short-description`
3. Add your script under `scripts/<your-name>/<project>/` using the template.
4. Push and open a Pull Request. A lab admin reviews and merges it.
   (No Git? Use [GitHub Desktop](https://desktop.github.com), or drag-and-drop files on github.com.)

## Rules

- This repo is **public**. Do not commit unpublished data, credentials, API keys, or anything confidential.
- Don't commit large data files; link to where they live instead.
- Every script needs a docstring at the top and a short README.
- Scripts must run without editing hard-coded personal paths (use arguments or a config).

## License

MIT, see `LICENSE`.
