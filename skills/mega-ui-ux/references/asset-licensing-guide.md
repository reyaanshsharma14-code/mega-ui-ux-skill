# Ultra UI/UX Pro Max — Legal Font, Asset & Image Licensing Guide
*Authored by ScraperDev BD (https://www.scraperdevbd.fun/)*
*Ethical & Production Compliance Standards*

---

## 1. Ethical Asset Sourcing & Zero Hallucination Policy

Ultra UI/UX Pro Max maintains a strict policy regarding intellectual property, font distribution, and external asset verification:
1. **Never Redistribute Unlicensed Commercial Font Files**: Do not bundle proprietary `.woff2` or `.otf` font files in git repositories unless the license explicitly permits redistribution (such as SIL Open Font License 1.1 or Apache 2.0).
2. **Never Fabricate Font or Asset URLs**: All URLs recorded in catalog registries must point to legitimate foundries, official repositories, Google Fonts, or Fontshare.
3. **Always Document External Licensing Requirements**: If a user requests a specific font that requires a commercial license, explicitly identify the font creator/foundry, document the license requirement, and provide a verified zero-cost open-source web fallback.

---

## 2. Font License Types Decoded

### SIL Open Font License 1.1 (OFL-1.1)
- **Permissions**: Free for commercial and personal use, modification, and web embedding. Can be bundled with open-source software.
- **Restrictions**: Cannot be sold by itself. Modified versions must not use Reserved Font Names without permission.
- **Examples**: `Inter`, `Space Grotesk`, `Playfair Display`, `Dela Gothic One`, `Newsreader`.

### Apache License 2.0
- **Permissions**: Free for commercial and personal web embedding.
- **Examples**: `Roboto`, `Kosugi Maru`.

### Fontshare Font License (ITF Free License)
- **Permissions**: Free for personal and commercial projects. Free web hosting via Fontshare CDN.
- **Restrictions**: Resale or direct redistribution of font files prohibited.
- **Examples**: `Cabinet Grotesk`, `Clash Display`, `Satoshi`, `General Sans`, `Switzer`.

### Freeware / Personal Use Only
- **Permissions**: Permitted for portfolio exploration, personal practice, and non-commercial evaluation.
- **Restrictions**: Commercial websites, client projects, paid products, and public SaaS apps **MUST** purchase a commercial license from the foundry.
- **Examples**: *The Last Shuriken* (Galdino Otten), *JAPAN RAMEN* (Weknow).

### Demo License
- **Permissions**: Limited character set provided for evaluation.
- **Restrictions**: Not licensed for public production deployment.
- **Examples**: *Katsuno Japan Demo* (Megatype), *Urung Bloom Demo* (ToniStudio).

### Commercial Paid License
- **Permissions**: Licensed strictly per seat or web monthly pageviews.
- **Restrictions**: Redistribution strictly prohibited.
- **Examples**: *Cayu* (Prioritype Co.).

---

## 3. Reference Table of Requested Fonts & Legal Compliance

```text
+----------------------+--------------------+---------------------------------------+-----------------------------+
| Font Name            | Foundry / Creator  | Legal Classification                  | Recommended Open Fallback   |
+----------------------+--------------------+---------------------------------------+-----------------------------+
| The Last Shuriken    | Galdino Otten      | Freeware (Personal); Commercial Req.  | Dela Gothic One / Rampart   |
| JAPAN RAMEN          | Weknow             | Free (Personal); Commercial Req.      | Yuji Boku / Kiwi Maru       |
| Katsuno Japan Demo   | Megatype           | Demo; Commercial Req.                 | Yuji Boku / Zen Tokyo Zoo   |
| Cayu                 | Prioritype Co.     | Commercial Paid License               | Instrument Serif / Bodoni   |
| Urung Bloom Demo     | ToniStudio         | Demo; Commercial Req.                 | Fraunces / Cinzel Dec.      |
+----------------------+--------------------+---------------------------------------+-----------------------------+
```
