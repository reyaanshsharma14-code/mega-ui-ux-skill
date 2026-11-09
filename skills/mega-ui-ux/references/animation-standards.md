# Ultra UI/UX Pro Max — Advanced Development, 3D, Animation & Code Standards

## 1. TypeScript-First Development Policy

**TypeScript (`.ts` and `.tsx`) MUST be the default programming language whenever the user does not explicitly specify a language.**

Follow these rules strictly:

- If the user requests a website, web application, dashboard, portfolio, landing page, or React-based interface without specifying a programming language, prefer TypeScript.
- For React projects, use `.tsx` for components and `.ts` for utilities, configuration helpers, types, hooks, and business logic.
- For Next.js projects, prefer TypeScript with the appropriate App Router or Pages Router structure based on the existing project.
- For React Three Fiber projects, use TypeScript and `.tsx` components by default.
- Define clear interfaces, types, reusable type aliases, and properly typed component props.
- Avoid `any` wherever practical. Use `unknown`, generics, type guards, and explicit interfaces when appropriate.
- Properly type event handlers, API responses, component state, function parameters, return values, configuration objects, and third-party integrations.
- Enable and respect strict TypeScript settings when compatible with the existing project.
- Use type-safe patterns without making simple code unnecessarily complicated.
- Never introduce TypeScript into a project that explicitly requires JavaScript, Python, PHP, Java, C#, or another specific language.
- If the user explicitly names a language, framework, or technology stack, follow that requirement instead of imposing TypeScript.
- If the existing project is already built using JavaScript and the user requests a feature or bug fix, preserve the existing stack unless the user explicitly requests migration.
- Never convert an entire project from JavaScript to TypeScript without permission.
- If a task is backend-only, CLI-based, game-related, or otherwise outside the usual TypeScript web stack, choose the language that best fits the explicit requirements and existing codebase.

### Language selection priority

1. **Explicit user instruction:** Use the exact language and technology the user requests.
2. **Existing project requirements:** Preserve the current architecture, framework, package manager, and language unless a change is requested.
3. **TypeScript by default:** When no language is specified and the task is a suitable web development project, use TypeScript.
4. **Best-fit exception:** For tasks where TypeScript is inappropriate, choose the most suitable technology without forcing an unsuitable stack.

Never change the requested language simply because another language is more familiar or convenient.

## 2. Advanced 3D Website Development

When the user requests a 3D website, immersive website, interactive 3D portfolio, animated 3D landing page, product visualization, or another experience where 3D meaningfully improves the result, build a genuinely interactive 3D experience rather than simulating everything with static images.

### Preferred 3D technology stack

Choose the technology according to the project:

- **Three.js:** Preferred for custom 3D experiences built with vanilla JavaScript or TypeScript.
- **React Three Fiber:** Preferred for integrating Three.js into React and TypeScript applications.
- **Drei:** Use when appropriate for reusable React Three Fiber helpers, controls, environments, loaders, and other scene utilities.
- **GSAP:** Use for sophisticated timelines, scroll-driven scenes, camera transitions, and coordinated animation sequences.
- **Framer Motion / Motion:** Use for React interface animations, layout transitions, hover interactions, and UI state changes.
- **WebGL shaders:** Use custom shaders when they offer a meaningful visual improvement, such as procedural backgrounds, animated gradients, distortion effects, or particle simulations.
- **Spline:** Consider it when a visually designed, interactive 3D scene is more appropriate than a fully custom-coded scene.

Do not install or combine every library automatically. Select the smallest appropriate toolset that delivers the requested experience.

### 3D design and interaction standards

Build polished 3D scenes with appropriate combinations of:

- Realistic or stylized lighting, shadows, materials, reflections, and depth.
- Smooth camera movement, rotation, zoom, and controlled parallax.
- Interactive 3D objects responding to pointer movement, clicks, scroll position, or user input.
- Particle systems, floating elements, procedural geometry, and animated environments when appropriate.
- Custom shaders, atmospheric effects, subtle bloom, and post-processing only when useful and performant.
- Seamless integration between the 3D scene and the HTML/CSS interface.
- Thoughtful transitions between sections, camera positions, and scene states.
- Carefully designed loading, error, and fallback states for 3D assets.

Do not add 3D effects just to make a website look complicated. Every scene must support the website's purpose, brand, visual hierarchy, or storytelling.

### 3D performance and compatibility

A visually impressive website is not successful if it runs poorly.

- Optimize 3D models, polygon counts, texture sizes, materials, and draw calls.
- Prefer compressed and appropriately sized assets.
- Lazy-load large models and nonessential scene components.
- Avoid creating excessive lights, particles, post-processing passes, or continuously running animation loops.
- Reduce rendering quality, particle counts, or visual effects on weaker devices when necessary.
- Pause or reduce unnecessary rendering when a scene is not visible or the page is inactive.
- Respect `prefers-reduced-motion` and provide an appropriate reduced-motion experience.
- Support responsive layouts, touch interactions, and mobile viewport sizes.
- Avoid blocking the main thread with expensive calculations.
- Provide a useful fallback if WebGL is unavailable or a model fails to load.
- Prevent layout shifts while 3D content loads.
- Never sacrifice text readability, navigation usability, accessibility, or core functionality for visual effects.

For React Three Fiber, use the appropriate Canvas configuration, event handling, asset-loading strategy, and rendering optimization for the scene. Avoid unnecessary React state updates on every animation frame.

## 3. Premium Animation and Motion Design

Animations must feel intentional, smooth, and professionally art-directed. Do not rely on basic fade-ins and default hover effects for every section.

### Animation capabilities

Use appropriate combinations of:

- Entrance and exit animations.
- Scroll-triggered reveals and staggered element sequences.
- Smooth page and section transitions.
- Interactive hover, focus, press, and selection states.
- Animated navigation menus and mobile drawers.
- Fluid button feedback and micro-interactions.
- Parallax backgrounds and layered depth.
- Animated typography and text reveals.
- SVG path drawing and icon transitions.
- Progress indicators, loading animations, and skeleton states.
- Interactive charts, dashboards, cards, and data visualizations.
- Timeline-based sequences and synchronized 3D animations.
- Smooth transitions between light/dark themes when the design supports them.
- Subtle ambient motion for backgrounds, particles, decorative objects, and hero sections.

Use animation to establish hierarchy, communicate feedback, explain relationships, and improve perceived quality—not simply to decorate every element.

### Motion technology selection

- Use CSS transitions and keyframes for straightforward interactions and lightweight animations.
- Use GSAP for complex timelines, synchronized sequences, and scroll-driven animation.
- Use Motion or Framer Motion for React component transitions and interactive UI states.
- Use Three.js or React Three Fiber animation mechanisms for 3D objects, cameras, and scenes.
- Use SVG animations when they are the most suitable option for vector-based illustrations or icons.

Avoid unnecessary dependencies when native CSS can accomplish the task cleanly.

### Animation quality requirements

- Maintain smooth movement and consistent easing.
- Use purposeful durations and avoid excessive delays that make interfaces feel slow.
- Prevent animations from causing layout shifts or interfering with interactions.
- Avoid excessive bounce, rotation, blur, zoom, and overshooting effects.
- Make interactions feel responsive rather than forcing users to wait for animations.
- Ensure animations do not obscure text, buttons, forms, or important information.
- Support keyboard focus and touch interactions alongside pointer interactions.
- Respect reduced-motion settings by removing or simplifying nonessential movement.
- Avoid running expensive animations indefinitely in the background.
- Use consistent motion principles across the entire website.

The final result should feel cohesive, responsive, and premium rather than like a collection of unrelated animation effects.

## 4. Strict SVG-Only Icon Policy — No Static Emojis

**Never use static emojis as interface icons. Always use SVG-based icons.**

This rule applies to every website, web application, dashboard, portfolio, navigation bar, button, menu, feature card, status indicator, empty state, and other interface component.

### Approved icon approaches

Prefer:

1. **Lucide** for clean, consistent interface icons.
2. **Custom SVG icons** when a specific visual identity or icon shape is required.
3. **Other suitable SVG-based icon libraries** when the project has an established design system that should be preserved.
4. **Inline SVG illustrations** for custom decorative graphics and interface-specific visuals.

Choose an icon library that fits the existing framework and project architecture.

### Strict requirements

- Never substitute emojis such as rockets, stars, fire, hearts, check marks, warning symbols, or smiley faces for interface icons.
- Never use emoji characters as decorative replacements for navigation icons, action buttons, feature illustrations, status indicators, or social icons.
- Use consistent icon sizes, stroke weights, alignment, and spacing.
- Prefer SVG icons that inherit the appropriate color from the design system.
- Use accessible labels for icon-only buttons.
- Mark purely decorative SVGs appropriately so screen readers do not announce meaningless content.
- Keep icons visually consistent throughout the website.
- Use custom SVGs when a standard icon does not fit the design.
- Do not embed an emoji inside an SVG to bypass this policy.
- Do not replace actual brand logos with generic icons when the correct logo asset is available.

This policy does not prohibit emojis that the user explicitly requests as actual content, such as text in a chat message or a social media post. It prohibits using static emojis as substitutes for designed UI icons.

## 5. Advanced Visual Design and UI/UX Quality

Every website should have a deliberate visual identity instead of looking like a generic AI-generated template.

### Design principles

- Establish a coherent design system covering colors, typography, spacing, borders, radii, shadows, surfaces, and motion.
- Use deliberate visual hierarchy and appropriate content density.
- Choose typography that matches the product's personality and maintains excellent readability.
- Use consistent spacing and alignment across sections.
- Create meaningful differences between headings, supporting text, metadata, and interactive controls.
- Design buttons, forms, cards, navigation, dialogs, and menus as parts of one cohesive system.
- Avoid repetitive layouts when the content calls for more variety.
- Avoid unnecessary gradients, glassmorphism, glowing borders, oversized headings, and decorative effects unless they suit the design direction.
- Use a consistent icon system and animation language.
- Ensure the design works in both the requested theme and responsive layouts.
- Maintain sufficient color contrast and visible focus states.
- Make empty, loading, error, success, disabled, and hover states feel intentional.

### Reference-driven design

When the user supplies a screenshot, website URL, reference image, or design inspiration:

- Study the actual reference before implementing it whenever access is available.
- Identify the layout, spacing, typography, colors, interaction patterns, animation behavior, and overall visual direction.
- Recreate the requested characteristics accurately while respecting the user's requested changes.
- Do not blindly copy unrelated branding, text, assets, or identity.
- If a requested resource or reference is unavailable, state the limitation and use the closest reasonable alternative rather than pretending to have inspected it.

## 6. Implementation and Project Integrity

Visual quality must never come at the cost of code correctness.

- Inspect the existing project structure before implementing changes.
- Preserve the requested language, framework, package manager, routing strategy, and architecture.
- Reuse existing components and dependencies when appropriate.
- Create only the files required for the requested task.
- Avoid replacing working code or restructuring unrelated parts of the project.
- Keep components modular, readable, maintainable, and appropriately typed.
- Handle errors, loading states, and missing assets gracefully.
- Avoid fake buttons, nonfunctional navigation, placeholder interactions, and controls that only look interactive.
- Verify that all interactive elements perform their intended actions.
- Check responsive behavior and accessibility.
- Run available type checks, linting, and relevant tests after implementation.
- Fix errors introduced by the changes before declaring the task complete.
- Never claim that a feature was tested successfully unless it was actually tested.

For TypeScript projects, resolve relevant TypeScript errors instead of hiding them with broad type assertions, `@ts-ignore`, or unnecessary `any` types.

## 7. Final Quality Checklist

Before considering a website complete, verify the following:

- [ ] The explicitly requested programming language and framework are respected.
- [ ] TypeScript is used by default for suitable web projects when no language is specified.
- [ ] The existing project architecture has been preserved unless a change was requested.
- [ ] 3D effects are genuinely interactive when required by the design.
- [ ] Three.js or React Three Fiber is used where appropriate.
- [ ] Animations are smooth, purposeful, accessible, and responsive.
- [ ] Static emojis are not used as interface icons.
- [ ] Interface icons use consistent SVG-based assets.
- [ ] The design looks polished on desktop, tablet, and mobile.
- [ ] Performance has been considered, particularly for 3D scenes and animation.
- [ ] Loading, error, and fallback states are handled appropriately.
- [ ] All buttons, links, menus, and controls work as intended.
- [ ] Relevant type checks, tests, and build checks have been run where available.
- [ ] No unrelated project files or features have been unnecessarily modified.

**Ultimate goal:** Deliver production-minded websites that combine strong UI/UX, TypeScript-first engineering, immersive 3D experiences, sophisticated animation, consistent SVG iconography, accessibility, responsiveness, and real functionality—while always following the user's explicit instructions and the requirements of the existing project.