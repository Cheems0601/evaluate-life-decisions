# Contributing

Contributions are welcome when they make the skill more accurate, useful, or globally representative.

## Useful contributions

- Add a regional source module using the provided template.
- Improve a decision step without forcing one cultural value system.
- Add an evaluation case that exposes a real failure mode.
- Replace a weak source with a primary or methodologically stronger source.
- Improve accessibility, translation, or installation guidance.

## Regional source rules

A regional module should:

1. Link to official statistical and policy sources where possible.
2. State what each source can and cannot establish.
3. Cover current economic and labor conditions as well as historical research.
4. Avoid treating a country, culture, or generation as a single personality.
5. Avoid hard coding the current year or a current officeholder.
6. Include books as search leads only unless their text is lawfully available and verified.

## Pull request checklist

- Run `python3 scripts/validate.py`.
- Explain which failure mode or user need the change addresses.
- Add or update an evaluation case for behavior changes.
- Check every new URL and identify primary sources clearly.
- Do not include copyrighted book text, private information, or generated quotations.
- Keep `SKILL.md` concise and place detailed material in `references/`.

## Style

Write direct instructions for an agent. Prefer observable checks over broad ideals. Distinguish sourced facts, analysis, and analogy. Use inclusive, plain English in shared files; regional modules may include original language source names alongside English descriptions.
