# Component Systems, Forms, Tables, Dashboards & Data Visualization

Synthesizes production component decision trees from `ai-design-components`, `ui-ux-pro-max`, and `ui-ux-ultra-max`. Use this reference when designing or building data-dense interfaces, forms, tables, dashboards, search/filter flows, or notification systems.

---

## 1. Forms & Input Systems

### Input Selection Matrix

| Data Type | Options Count | Component | Why |
|---|---|---|---|
| Single choice | 2–5 options | Radio group or Segmented control | All options visible at a glance; zero extra clicks |
| Single choice | 6–15 options | Native `<select>` or accessible Combobox | Compact without hiding too little |
| Single choice | 15+ options | Searchable Combobox / Autocomplete | Scrolling a long dropdown is slow and error-prone |
| Multiple choice | 2–7 options | Checkbox group | Clear independent toggles |
| Multiple choice | 8+ options | Multi-select combobox with removable chips | Keeps layout compact and shows active selections |
| Boolean (immediate effect) | 1 | Switch (`role="switch"`) | Signals instant state change without a Save button |
| Boolean (in a submitted form) | 1 | Checkbox | Signals value is committed on form submit |
| Numeric (bounded, approximate) | Range | Slider + numeric readout | Fast exploration; pair with input if exact value matters |
| Numeric (exact: price, age, OTP, quantity) | Open | `<input type="text" inputmode="numeric">` or `type="number"` | Avoid scroll-wheel accidental changes on `type="number"` |
| Date (known: birth date, expiry) | Exact | Segmented day/month/year inputs or typed mask | Faster than clicking back 30 years in a calendar |
| Date (relative: booking, flights) | Range | Calendar picker with unavailable dates disabled | Users think spatially about weeks and weekends |

### Validation Timing ("Reward Early, Punish Late")
1. **Never validate while the user is typing into a field for the first time.** Premature red errors ("Invalid email" after typing `r@`) feel hostile.
2. **Validate on blur** (when leaving the field) or **on submit**.
3. **Once a field is in an error state, re-validate on input** so the error disappears the instant the user fixes it.
4. **Preserve user input** on error—never clear a form on failed submission.
5. **Tie every error to its input** with `aria-invalid="true"` and `aria-describedby="<error-id>"`. Put the error message directly below the field in plain language: *what went wrong + how to fix it*.

---

## 2. Data Tables & Grids

### Architecture by Data Volume

| Volume | Strategy | Recommended Stack |
|---|---|---|
| **< 100 rows** | Semantic `<table>`, client-side sort/filter | Native HTML + CSS Grid/sticky headers |
| **100 – 10,000 rows** | Client-side pagination (25–50/page) or virtual rows | TanStack Table (`@tanstack/react-table`) |
| **10,000 – 1M+ rows** | Server-side cursor pagination, sort & filter + row virtualization | TanStack Table + `@tanstack/react-virtual` or AG Grid |

### Non-Negotiable Table Craft Rules
- **Alignment:** Left-align text, status badges, and IDs. **Right-align numeric columns** (currency, counts, percentages) and their headers. Center only single icons or checkboxes.
- **Typography:** Always apply `font-variant-numeric: tabular-nums` to numeric cells, timestamps, and IDs so digits align vertically.
- **Sticky Context:** Keep `<thead>` sticky (`position: sticky; top: 0; z-index: 2`) and optionally pin the primary identifier column on wide horizontal tables.
- **Row Density:** Offer a consistent row height (40px compact / 48px standard / 56px spacious). Never let multi-line cell text jaggedly vary row heights unless explicitly expanded.
- **Responsive Mobile Strategy:** Never squish 8 columns into 360px. Either:
  1. Scroll horizontally inside a container with a subtle right-edge shadow cue and a sticky first column, or
  2. Transform each row into a structured summary row (Primary label + primary metric + status) that expands on tap.

---

## 3. Dashboards & KPI Architecture

### The 5-Second Dashboard Rule
A user opening a dashboard must answer **"Is everything okay, and what needs my attention?"** within 5 seconds:
1. **Top tier (1–4 KPI metrics):** Value + unit (`font-variant-numeric: tabular-nums`) + comparison delta (`+12.4% vs last 30d`) + mini sparkline or status threshold. Never show a raw number without context.
2. **Middle tier (1–2 primary charts):** The main time-series or breakdown answering the core question.
3. **Bottom tier (actionable table / queue):** The specific items driving the numbers above, filtered by clicking the chart or KPIs.

### Dashboard Anti-Patterns to Eliminate
- **Gauge / speedometer charts:** Waste space and show a single number poorly. Use a KPI stat with a linear progress bar or bullet chart.
- **More than 4 KPI cards in a row:** Everything shrinks and nothing is focal.
- **Unfiltered wall of 9 equal charts:** Group by question; demote secondary charts behind tabs or progressive disclosure.

---

## 4. Data Visualization Selection Matrix

| Analytical Goal | Best Chart Type | Avoid |
|---|---|---|
| **Trend over time** (continuous) | Line chart, Area chart (1–3 series max) | 3D bars, stacked area with >4 noisy series |
| **Compare categories** (ranked) | Horizontal bar chart (labels read naturally without tilting) | Pie/donut chart with >4 slices |
| **Part-to-whole** | Stacked horizontal bar, 100% bar, or Treemap | Pie charts when slices are similar in size (humans judge length far better than angle) |
| **Distribution** | Histogram, Box plot, or Strip plot | Averaging away bimodal data into a single bar |
| **Correlation (2–3 variables)** | Scatter plot with trendline | Dual-axis line charts with unrelated scales |
| **Flow / Funnel / Conversion** | Horizontal funnel bar or Sankey diagram | Disconnected percentage badges |

### Accessible Chart Rules
- **Direct labels beat legends:** Label lines at their right endpoint or bars directly whenever space allows so the eye doesn't bounce between chart and legend.
- **Colorblind-safe palette (Okabe-Ito inspired):** Pair hue differences with luminance contrast and line styles (solid vs dashed) or point markers.
- **Always include units on axes and tooltips**, and provide a screen-reader summary or tabular toggle for critical data.

---

## 5. Feedback, Toasts, Modals & Empty States

| Urgency / Scope | Pattern | Rules |
|---|---|---|
| **Low-stakes confirmation** ("Saved", "Archived") | Toast / Snackbar | Auto-dismiss in 4–6s; include an **Undo** button for destructive actions; pause timer on hover/focus |
| **Field-level problem** | Inline error below field | Never use a toast for form validation errors (it disappears before the user fixes the field) |
| **Page/system warning** (offline, quota, maintenance) | Persistent inline banner | Stays visible until resolved; includes a recovery action |
| **Contextual secondary task** (filters, item detail, quick edit) | Drawer / Bottom sheet (mobile) | Preserves background context; dismissible via Esc or backdrop |
| **High-stakes destructive or blocking decision** | Modal dialog (`<dialog>`) | Focus-trapped, Esc-dismissible, explicit verb on confirm button ("Delete project", never "Yes" or "OK") |

---

## 6. Search, Filter & Command Patterns

- **Instant vs. Debounced:** Local lists (<500 items) filter on every keystroke (`0ms`). Network searches debounce by `200–300ms`, abort stale requests (`AbortController`), and keep previous results visible with a subtle loading indicator instead of flashing a blank skeleton on every keystroke.
- **Zero-Result States:** Always show the query that returned nothing, offer 1-click filter reset ("Clear 3 active filters"), and suggest popular items or broader terms.
- **Active Filter Visibility:** Show active filters as removable chips with a count badge on mobile so users never wonder why a list looks incomplete.
