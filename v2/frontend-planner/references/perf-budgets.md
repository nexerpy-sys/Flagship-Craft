# Frontend Performance Budgets & Rendering Discipline

Slow UIs feel broken even when they are functionally correct. This playbook enforces measurable Core Web Vitals budgets and prevents the most common rendering bottlenecks.

---

## 1. Hard Performance Budgets

| Metric | Target (Good) | Primary Culprits | Mandatory Fix |
| --- | --- | --- | --- |
| **LCP** (Largest Contentful Paint) | `<= 2.5s` | Unoptimized hero images, `loading="lazy"` on hero, render-blocking CSS/JS | Preload hero image (`fetchpriority="high"`), inline critical CSS, never lazy-load above-the-fold media. |
| **CLS** (Cumulative Layout Shift) | `<= 0.1` | Images/embeds without dimensions, late-loading web fonts, injected banners | Always set explicit `width`/`height` or `aspect-ratio`; use `font-display: swap`; reserve skeleton height. |
| **INP** (Interaction to Next Paint) | `<= 200ms` | Synchronous heavy filtering on keystroke, rendering 1,000+ DOM nodes | Debounce/defer expensive work, virtualize lists `>100` items, avoid forced synchronous layouts. |

---

## 2. React / Component Rendering Hygiene

1. **Co-locate State**: Keep ephemeral UI state (hover, dropdown open, input draft) local to the leaf component—never lift it to a global store where every keystroke re-renders the entire page.
2. **Derive, Don't Sync**: Never store derived values (`filteredItems`, `cartTotal`) in `useState` + `useEffect`. Compute them inline during render (or `useMemo` only if profiling proves it's slow).
3. **Kill Request Waterfalls**: Fetch route-level data in parallel (`Promise.all`) at the container/route boundary, not sequentially inside nested child `useEffect`s.
4. **Bundle Discipline**: Lazy-load heavy non-initial routes, charts, and rich-text editors (`React.lazy` / dynamic `import()`).

---

## 3. Verification Checks

- **DOM Size Check**: Inspect rendered DOM node count; flag any unvirtualized list/table rendering `>100` rows.
- **Asset Check**: Verify above-the-fold images have explicit dimensions and do not use `loading="lazy"`.
- **Network Waterfall Check**: Confirm independent API calls fire in parallel, not sequentially.

---

## 4. Contrastive Anchors (Naive vs. Flagship Performance)

1. **Analytics Dashboard**:
   - *Naive*: Parent fetches user -> Child fetches org -> Grandchild fetches metrics (3-step waterfall, 1.8s delay); renders 2,500 table rows directly in the DOM.
   - *Flagship*: Route loader fetches user, org, and metrics in parallel (`Promise.all`), virtualizes the table (rendering ~25 visible rows), and reserves exact skeleton heights (`CLS = 0`).
2. **Hero Landing Page**:
   - *Naive*: Loads a 4MB unoptimized PNG hero with `loading="lazy"` and 6 Google Font weights blocking first paint.
   - *Flagship*: Serves WebP/AVIF with explicit `width`/`height`, `fetchpriority="high"`, and 2 font weights with `font-display: swap`.
