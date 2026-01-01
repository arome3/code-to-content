# Complete Video Script Example

**Source Project:** lottie-react (React library for Lottie animations)
**Audience:** Beginner-intermediate React developers
**Format:** YouTube tutorial script (8-10 minutes)
**Generated Following:** 5-Phase Process with all gates passed

---

## Generated Output

---

### Video Metadata

**Title:** Add Smooth Animations to React in 5 Minutes (No CSS Required)

**Description:**
Learn how to add professional Lottie animations to your React app using lottie-react. We'll cover installation, the component API, the hook API, and interactive scroll-based animations—all in under 10 minutes.

**Thumbnail Text:** "Lottie + React = Magic"

**Tags:** react, lottie, animation, frontend, web development, tutorial

---

### Script

---

#### INTRO (0:00 - 0:45)

**[ON SCREEN: Boring static UI, then transforms with smooth animations]**

**NARRATION:**
"Your React app works. But it looks... static. Generic. Like every other app out there.

What if you could add professional-grade animations—the kind you see in apps like Airbnb and Spotify—without learning complex CSS or animation libraries?

That's exactly what we're doing today.

I'm going to show you how to add Lottie animations to React in about 5 minutes. By the end, you'll have interactive, scroll-triggered animations that make your app feel alive.

Let's go."

---

#### SECTION 1: What is Lottie? (0:45 - 1:30)

**[ON SCREEN: Lottie animation examples, After Effects → JSON diagram]**

**NARRATION:**
"Quick context: Lottie animations are vector-based, lightweight, and originally created in After Effects. But here's the key—they export as JSON files.

That means they're:
- Tiny (like 5-20KB)
- Infinitely scalable
- Easy to control with code

The problem? The core library, lottie-web, was built for vanilla JavaScript. React's component model doesn't play nice with it out of the box.

That's where lottie-react comes in."

---

#### SECTION 2: Installation (1:30 - 2:15)

**[ON SCREEN: Terminal with commands]**

**NARRATION:**
"Let's install it. Open your terminal in your React project."

**[TYPE ON SCREEN]:**
```bash
npm install lottie-react
```

**NARRATION:**
"That's it. One package. No peer dependencies to worry about—lottie-web is included automatically.

Now let's grab an animation. Head to lottiefiles.com—pause if you need to—and download any free animation as a JSON file. I'm using this rocket animation."

**[ON SCREEN: LottieFiles website, downloading JSON]**

---

#### SECTION 3: Basic Usage - Component API (2:15 - 4:00)

**[ON SCREEN: VS Code with React component]**

**NARRATION:**
"The simplest way to use lottie-react is the component API. Watch how easy this is."

**[TYPE ON SCREEN]:**
```jsx
import Lottie from "lottie-react";
import rocketAnimation from "./rocket.json";

function App() {
  return <Lottie animationData={rocketAnimation} loop={true} />;
}
```

**NARRATION:**
"Three lines of actual code. Import the component, import your JSON, render it.

Let's see it in action."

**[ON SCREEN: Browser showing animation playing]**

**NARRATION:**
"Boom. Professional animation. Zero CSS.

You can control it with props:
- `loop` for continuous playback
- `autoplay` to start automatically
- `style` for sizing and positioning

But what if you need more control? Like play/pause buttons?"

---

#### SECTION 4: Hook API for Control (4:00 - 6:00)

**[ON SCREEN: VS Code with hook implementation]**

**NARRATION:**
"That's where the hook API shines. Instead of a component, you get back controls."

**[TYPE ON SCREEN]:**
```jsx
import { useLottie } from "lottie-react";

function App() {
  const { View, play, pause, stop } = useLottie({
    animationData: rocketAnimation,
    loop: true,
  });

  return (
    <div>
      {View}
      <button onClick={play}>Play</button>
      <button onClick={pause}>Pause</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}
```

**NARRATION:**
"The hook returns:
- `View` - the animation element
- `play`, `pause`, `stop` - self-explanatory controls
- Plus `setSpeed`, `goToAndPlay`, and more

This is what I use for loading states where I need to stop the animation programmatically."

**[ON SCREEN: Demo of play/pause working]**

---

#### SECTION 5: Interactive Scroll Animation (6:00 - 8:00)

**[ON SCREEN: Website with scroll-triggered animation]**

**NARRATION:**
"Now for the cool part. What if the animation responds to scrolling?

Like this—as I scroll down, the animation progresses. Scroll up, it reverses."

**[DEMO: Scrolling with animation synced]**

**NARRATION:**
"Here's the code."

**[TYPE ON SCREEN]:**
```jsx
<Lottie
  animationData={rocketAnimation}
  interactivity={{
    mode: "scroll",
    actions: [
      { visibility: [0, 0.5], type: "seek", frames: [0, 50] },
      { visibility: [0.5, 1], type: "seek", frames: [50, 100] },
    ],
  }}
/>
```

**NARRATION:**
"The `interactivity` prop takes actions based on visibility.

When the element is 0-50% visible, play frames 0 to 50. When 50-100% visible, play frames 50 to 100.

You can also use `mode: cursor` for mouse-following effects. The docs have tons of examples."

---

#### SECTION 6: Wrap-up (8:00 - 8:45)

**[ON SCREEN: Comparison - before/after UI]**

**NARRATION:**
"Let's recap what we covered:
- Component API for simple embedding
- Hook API for programmatic control
- Scroll interactivity for that premium feel

All without writing a single keyframe of CSS.

The full code is in the description. If this helped, hit subscribe—I've got more React tutorials coming.

See you in the next one."

**[END SCREEN: Subscribe button, related video suggestions]**

---

## Metadata

**Total Duration:** ~8:45
**Sections:** 6 (optimal for retention)
**Code Snippets:** 4 (all from lottie-react API)
**B-Roll Needed:** LottieFiles website, browser demos

---

## Phase Gate Verification

| Gate | Status | Evidence |
|------|--------|----------|
| Phase 1 | ✅ | Tech stack: React, TypeScript, lottie-web |
| Phase 2 | ✅ | Audience: Beginner-intermediate, Format: Video script |
| Phase 3 | ✅ | All code from lottie-react documentation |
| Phase 4 | ✅ | Paced sections, visual cues noted |
| Phase 5 | ✅ | Conversational script, clear demonstrations |

---

## Why This Example Works

1. **Hook in first 10 seconds** — Shows transformation, states the promise
2. **Progressive complexity** — Component → Hook → Interactivity
3. **Live coding moments** — Viewer sees code being written
4. **Clear section markers** — Easy to scrub through video
5. **Practical use cases** — Loading states, scroll effects
6. **Call to action** — Subscribe at the end, code in description
