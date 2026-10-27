# TA — Personal Umbrella & Website Architecture

**Status:** Recovered decision + updated interpretation, 12 October 2026.

## Source of this decision

The key prior discussion occurred on **27 September 2026**. The owner explicitly described **teodorandonov.com** as the **personal TA umbrella**, with separate portals for personal Portfolio, Notes/blog, an independent architectural/computational practice, Balkan House and future Apps/Products. They can begin inside TA and separate into distinct identities/domains when substantial enough.

In the **12 October 2026** discussion the owner selected **C — both equally** for prominence of Portfolio and Studio. The owner has now clarified that this **does not** reduce the umbrella to only two destinations. It establishes parity between two major sibling sections.

## Proposed navigation model (not final URL names)

```text
TA / Teodor Andonov — teodorandonov.com
├── Portfolio     Personal portfolio, professional projects with credits,
│                 independent experiments and archive
├── Studio        Independent commissionable practice; Method / Studio Method
│                 leading provisional name, not yet approved as permanent
├── Notes         Short notes, news, articles, research and updates
├── Apps          Tools, configurators, utilities, digital experiments
├── Projects      Distinct ventures (e.g. Balkan House), possible subsites
└── About         Personal context/contact
```

**Apps** and **Projects** may be combined or split in actual navigation; this remains a UI choice. The content types should stay distinct in structured data even when grouped visually.

## Rules

1. **TA is the author/personal parent, not the practice company brand.**
2. Portfolio and Studio are **equal siblings** in main identity/navigation. Neither subsumes the other; Notes/Apps/Projects aren't relegated to Studio.
3. **Method / Studio Method** is the leading working name for Studio as of 12 October 2026; previous name research favoured **METOD** but never conclusively selected it. Do not finalize spelling/name, imply company registration or assume a domain exists.
4. The personal Portfolio can present professional/employer work **with accurate employer, team, author/role, dates, stage, attribution and permissions**. Studio must not imply those are Method's commissioned work.
5. Studio can reference relevant credited portfolio projects as evidence of experience while distinguishing its **own** commissions.
6. **A venture begins as a TA-hosted subsite** (e.g. `/studio`, `/apps/product-name`, `/projects/balkan-house`; examples only). If the venture grows into a distinct commercial/research/product entity, migrate its full presence to an independent domain. TA keeps a summary/entry page linking out. No premature separate domain or infra needed.
7. Shared design foundations—type, grid, system tokens, graphic grammar—provide family resemblance. Ventures may develop their own more distinctive treatments and brands without fragmenting the TA parent.
8. Website JSON content/structure remains the **website repository's** source of truth. This design-system repository defines identity architecture and visual usage, not an alternative content database.
9. Avoid conflating the public website with canonical project folders or the entire private archive; publish curated, credited views.
10. Navigation must serve **real visitors**: Explore Portfolio; Discover Method Studio and how to collaborate; Read Notes; Use/Explore Apps.

## Visual implications for identity studies

Identity boards should show a **full ecosystem**, not just an agency homepage:
- TA personal landing/portal with Portfolio / Studio / Notes / Apps visible.
- Portfolio page/cards, including clear project-role/credit metadata.
- Studio Method presentation or service panel, clearly scoped as a **provisional identity**.
- Notes/short article specimen.
- App/product UI with its own name nested under TA.
- Report/publication format and a presentation slide demonstrating the shared visual language.
- Typography, neutral palette, grids, iconography, components and responsive UI.
- The *same* visual-family features across all, while protecting the different purposes.

## Explicit non-decisions

- Method vs Studio Method vs METOD final spelling and official name.
- Exact public navigation order and URL slugs.
- Whether Apps and Projects share one page or separate tabs.
- Exact identity separation between future products and the TA parent.
- Domain purchase, legal business registration, launched services or completed commissions.

**Decision history:** See [DECISIONS.md](DECISIONS.md). **Brand positioning:** See [BRAND.md](BRAND.md). **Visual comparison:** See [DIRECTIONS.md](DIRECTIONS.md).
