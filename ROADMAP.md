# ブレインダンプ — Autonomous Improvement Roadmap

Managed by an autonomous Claude agent. Updated after each improvement cycle.
Last updated: 2026-05-05

## Done
- [x] Core app: brain dump input to AI categorization to task list
- [x] Natural language query bar
- [x] AI next-action suggestions per task
- [x] Category filter chips with colors
- [x] Mark done / delete tasks
- [x] localStorage persistence
- [x] iPhone PWA (Add to Home Screen)
- [x] Deployed to GitHub Pages
- [x] Voice input (Safari browser mode)
- [x] Fixed CORS header for direct browser API calls
- [x] Task editing -- inline edit title and original text
- [x] Dark mode -- auto-detects iOS/macOS system preference
- [x] Undo delete -- toast with 4-second undo button
- [x] Priority levels -- High/Medium/Low badge, clickable to cycle, tasks sorted by priority
- [x] Search bar -- filter tasks by keyword
- [x] Due dates -- optional date picker per task, color-coded overdue/today/future badges
- [x] Swipe to complete / swipe to delete (mobile gesture)
- [x] Export data -- JSON / text download
- [x] Language toggle -- Japanese / English switch
- [x] Better onboarding -- guided first-use flow with animated modal overlay

## Planned (priority order)
- [ ] Task notes -- expandable sub-notes field
- [ ] Batch select -- checkbox mode, bulk complete/delete
- [ ] Statistics view -- tasks done per day, category breakdown
- [ ] Browser push notifications -- remind about active tasks
- [ ] Recurring tasks -- daily/weekly repeat option
- [ ] Markdown in notes -- render bold, italic, checklists
- [ ] Multiple boards -- switch between different brain-dump contexts
- [ ] Share task -- copy shareable text summary
- [ ] Drag to reorder tasks

## Test Log

| Date | Feature | Verified | Status |
|------|---------|----------|--------|
| 2026-04-21 | Initial deploy | Setup | OK |
| 2026-04-21 | Task editing, dark mode, undo delete | HTML output verified | OK |
| 2026-04-21 | Priority levels (High/Medium/Low) | Deployed | OK |
| 2026-05-04 | Language toggle (JP/EN) | Deployed | OK |
| 2026-05-05 | Better onboarding overlay | Deployed | OK |

## User Ideas
- Voice input for easier navigation (done)
- Best app possible with AI + user ideas
- Autonomous improvement loop (this!)

## Change Log
- 2026-04-21: Initial deploy, voice input, CORS fix
- 2026-04-21: Task editing (inline), dark mode (prefers-color-scheme), undo delete (toast)
- 2026-04-21: Priority levels badge on each task, click to cycle, auto-sort by priority
- 2026-04-22: Keyword search bar added
- 2026-04-23: Due date feature (date picker, color-coded badges)
- 2026-04-24: Swipe to complete / delete (mobile gesture)
- 2026-04-25: Data export (JSON / text)
- 2026-05-04: Language toggle (Japanese / English) -- header toggle, full UI + AI prompts adapt
- 2026-05-05: Better onboarding -- animated modal overlay for first-time users, 3-step feature tour, persists dismissal in localStorage

## 2026-05-05 - Better Onboarding (First-Use Flow)
- Full-screen animated overlay shown only to new users (no tasks + no onboardingDone flag)
- Card slides in with smooth animation; adapts to JP/EN language toggle
- 3-step feature tour: Brain Dump input, AI auto-categorization, Next Actions suggestions
- Single "Get Started" / "はじめる" button dismisses and sets onboardingDone in localStorage
- Existing users are never interrupted
