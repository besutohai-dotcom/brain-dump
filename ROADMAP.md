# ブレインダンプ — Autonomous Improvement Roadmap

Managed by an autonomous Claude agent. Updated after each improvement cycle.
Last updated: 2026-05-08

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
- [x] Task notes -- expandable sub-notes field per task

## Planned (priority order)
- [x] Batch select -- checkbox mode, bulk complete/delete
- [x] Statistics view -- tasks done per day, category breakdown
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
| 2026-05-06 | Task notes (expandable sub-notes) | Deployed | OK |
| 2026-05-07 | Batch select (checkbox mode, bulk complete/delete) | Deployed | OK |
| 2026-05-08 | Statistics view (tasks done per day, category breakdown) | Deployed | OK |

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
- 2026-05-08: Statistics view -- 4-card summary (total/active/done/categories), completion rate bar, 7-day daily completions chart, category breakdown with colored bars; completedAt timestamp added to tasks
- 2026-05-07: Batch select -- Select button, checkboxes per task, bulk complete/delete, select-all, bilingual
- 2026-05-06: Task notes -- 📝 button per task, expandable textarea, auto-saved to localStorage, amber highlight when note exists

## 2026-05-06 - Task Notes (Expandable Sub-Notes)
- 📝 button added to every task card; amber color when a note exists
- Clicking the button toggles an expandable textarea below the task
- Notes are auto-saved to localStorage on every keystroke (onInput)
- Fully backward-compatible: existing tasks without notes field work unchanged
- Bilingual: "メモを追加..." / "Add a note to this task..."

## 2026-05-07 - Batch Select
- Select button in header toggles batch mode (hides clear/export/settings while active)
- Circular checkbox appears on each task card; click to toggle selection
- Swipe gestures and per-task action buttons disabled in batch mode
- Batch bar fixed at bottom: selected count, Select All, Complete N, Delete N
- Delete triggers undo toast; no schema change (backward-compatible)
- Bilingual: full Japanese/English UI strings

## 2026-05-08 - Statistics View
- Stats button in header (only visible when tasks exist, hidden in batch mode)
- Bottom sheet overlay with 4 summary cards: total / active / done / categories
- Completion rate bar (green progress bar showing % done)
- Daily completions chart: last 7 days, CSS bar chart, driven by new completedAt timestamp
- Category breakdown: color-coded horizontal bars sorted by task count, done count shown per category
- completedAt field added to tasks on toggle-done (null on undo); fully backward-compatible
- Bilingual: full Japanese/English UI strings
