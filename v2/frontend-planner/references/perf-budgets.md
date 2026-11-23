# Frontend Performance Budgets

## 1. Core Web Vitals & Rendering

- **LCP (Largest Contentful Paint)**: Preload hero image/font; never lazy-load above-the-fold hero media.
- **CLS (Cumulative Layout Shift)**: Reserve explicit `width`/`height` or `aspect-ratio` on all images, embeds, and skeletons.
- **INP (Interaction to Next Paint)**: Debounce expensive search/filter handlers; virtualize lists >100 items.

## 2. Contrastive Anchors (Naive vs. Flagship Frontend Architecture)

- **Naive**: Fetches data inside 6 nested components causing waterfalls, stores derived totals in `useState` + `useEffect`, and renders a 2,000-row table directly in the DOM.
- **Flagship**: Co-locates data fetching at the route/container boundary, derives totals inline, virtualizes large lists, and models all 5 async states explicitly.
