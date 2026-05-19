# Brain Dump Roadmap

Managed by an autonomous Claude agent. Updated after each improvement cycle.
Last updated: 2026-05-19

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
- [x] Batch select -- checkbox mode, bulk complete/delete
- [x] Statistics view -- tasks done per day, category breakdown
- [x] Browser push notifications -- remind about due tasks (while app is open)
- [x] Recurring tasks -- daily/weekly repeat option
- [x] Markdown in notes -- render bold, italic, checklists
- [x] Multiple boards -- switch between independent brain-dump contexts
- [x] Share task -- copy shareable text summary
- [x] Drag to reorder tasks
- [x] Focus mode -- show only top 3 active tasks at a time
- [x] Weekly summary -- AI-generated weekly review of completed tasks
- [x] Daily journal -- write daily entries with mood, auto-save, browse past 6 days

## Planned (priority order)

_(no items -- all roadmap features shipped!)_

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
| 2026-05-09 | Browser push notifications (due-task reminders) | Deployed | OK |
| 2026-05-10 | Recurring tasks (daily/weekly repeat) | Deployed | OK |
| 2026-05-12 | Markdown in notes (bold, italic, checklists) | Deployed | OK |
| 2026-05-14 | Multiple boards (independent task contexts) | Deployed | OK |
| 2026-05-15 | Share task (copy to clipboard) | Deployed | OK |
| 2026-05-16 | Drag to reorder tasks (HTML5 DnD, per-board manual order) | Deployed | OK |
| 2026-05-17 | Focus mode (top 3 active tasks, header toggle, banner, bilingual) | Deployed | OK |
| 2026-05-18 | Weekly summary (AI review, stats cards, task list, regenerate) | Deployed | OK |
| 2026-05-19 | Daily journal (mood, auto-save, past entries, bilingual) | Deployed | OK |

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
- 2026-05-06: Task notes -- button per task, expandable textarea, auto-saved to localStorage, amber highlight when note exists
- 2026-05-12: Markdown in notes -- edit/preview toggle per note; renders bold, italic, code, GFM checklists
- 2026-05-10: Recurring tasks -- daily/weekly repeat; recurrence badge on task cards; auto-advance due date on completion
- 2026-05-09: Browser push notifications -- toggle in Settings, Notifications API, checks every 5 min for due/overdue tasks, deduplicates across sessions, bilingual
- 2026-05-14: Multiple boards -- horizontal board bar below header; create/switch/rename/delete boards; each board has independent tasks and categories; fully backward-compatible migration from single-board storage
- 2026-05-17: Focus mode -- focus button; shows top 3 active tasks only; focus banner shows hidden task count; exit button in banner; resets on board switch; bilingual
- 2026-05-16: Drag to reorder -- drag handle on each card, HTML5 DnD, per-board manual order in localStorage; falls back to priority sort; backward-compatible
- 2026-05-15: Share task -- button on each task card; builds formatted text summary; copies to clipboard via Clipboard API with fallback; toast confirmation; bilingual
- 2026-05-18: Weekly summary -- header button; bottom-sheet overlay with 4 stat cards; task list preview; AI-generated review; regenerate support; bilingual
- 2026-05-19: Daily journal -- journal button always visible; bottom-sheet with mood selector (5 emojis), large textarea, auto-save (700ms debounce); past 6 days shown as collapsible entries; journal stored globally in localStorage (not per-board); bilingual

## 2026-05-19 - Daily Journal
- Pencil/notebook journal button always visible in header (even without tasks)
- Bottom-sheet overlay (same pattern as Stats/Weekly views)
- Today date displayed prominently with short weekday label
- Mood selector: 5 emoji buttons (sad to happy), highlighted when active; instantly saved
- Large textarea for free-form daily writing (min 140px, resizable)
- Auto-save debounced at 700ms; "Saved" confirmation fades in/out
- Past 6 days shown below: collapsible entries showing mood, date, and text snippet
- Expanding a past entry shows full text in a styled box
- First-time empty state shows an encouraging prompt
- Journal data stored at top-level `journal: {}` key in localStorage (keys = ISO date, values = {text, mood, savedAt})
- Board-independent: journal entries persist across all boards
- Fully backward-compatible: new `journal: {}` default, existing data untouched
- Bilingual: full Japanese/English UI strings for all interactions

## 2026-05-06 - Task Notes (Expandable Sub-Notes)
- Button added to every task card; amber color when a note exists
- Clicking the button toggles an expandable textarea below the task
- Notes are auto-saved to localStorage on every keystroke (onInput)
- Fully backward-compatible: existing tasks without notes field work unchanged
- Bilingual: placeholder text in Japanese and English

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

## 2026-05-09 - Browser Push Notifications
- Toggle switch in Settings panel to enable/disable notifications
- Requests Notification API permission on first enable; gracefully handles denied/unsupported
- Checks every 5 minutes (while app is open) for active tasks with dueDate <= today
- Shows one browser notification per due/overdue task per day (deduplication via localStorage)
- Old deduplication entries auto-cleared after 2 days
- notificationsEnabled field added to localStorage schema (backward-compatible, default false)
- Bilingual: full Japanese/English UI strings and notification messages

## 2026-05-10 - Recurring Tasks
- Select repeat option (None / Daily / Weekly) in edit mode for any task
- Recurrence badge displayed on task card
- Completing a recurring task advances due date by 1 day (daily) or 7 days (weekly), resets to active
- Completion counted in statistics (completedAt set) even for recurring tasks
- Toast shows next due date after recurring completion
- recurrence field added to task schema (null/"daily"/"weekly"); fully backward-compatible
- Bilingual: full Japanese/English UI strings

## 2026-05-12 - Markdown in Notes
- Edit/Preview toggle buttons appear in every expanded note panel
- Preview renders: **bold**, *italic*, `code`, headings, blockquotes, bullet/numbered lists, hyperlinks
- GFM task checklists rendered as read-only checkboxes
- Empty preview shows a localized placeholder
- `marked` v9 loaded from esm.sh with GFM + line-breaks enabled
- No schema change; fully backward-compatible
- Bilingual: JP and EN toggle labels

## 2026-05-14 - Multiple Boards
- Horizontal board bar displayed below the header at all times
- Boards are scrollable chips; active board highlighted in primary color with a manage button
- "+" chip at the end opens an Add Board modal
- Clicking manage on the active board opens a Manage Board modal: rename or delete
- Deleting the last board is blocked; deleting any board switches to the first remaining one
- Each board has its own independent tasks, categories, search state, and category filter
- Storage: new boards[], activeBoardId, and boardData{} fields in localStorage
- Backward-compatible migration: existing single-board data automatically wrapped in a default board
- persist() auto-syncs boardData for the active board on every save
- Bilingual: full Japanese/English UI strings for all board interactions

## 2026-05-15 - Share Task
- Share button added to every task card (hidden in edit mode and batch mode)
- Builds a formatted plain-text summary: title, category, priority, due date (if set), recurrence (if set), status, notes (if any), and original text
- Copies to clipboard via navigator.clipboard with execCommand fallback for older browsers
- Toast notification confirms copy success
- No schema change; fully backward-compatible
- Bilingual: full Japanese/English field labels and status strings

## 2026-05-17 - Focus Mode
- Focus button in header (visible when there are active tasks, hidden in batch mode)
- Button highlighted in primary color when focus mode is active
- Filters task list to top 3 active tasks only (done tasks hidden)
- Focus banner shows inside the task list with hidden task count
- Exit button in banner exits focus mode immediately
- Focus mode auto-resets when switching boards
- No schema change; session-only state (not persisted)
- Bilingual: full Japanese/English UI strings

## 2026-05-16 - Drag to Reorder Tasks
- Drag handle added to each task card (left side of labels row)
- HTML5 Drag and Drop API: dragstart, dragover, drop, dragend events on each task card
- Visual indicator: blue top/bottom border on drag-over target showing exact insertion point
- Dragging card shown at 45% opacity while being dragged
- Manual order stored as taskOrder[] per board in localStorage boardData
- Falls back to priority sort (high/medium/low) when no manual order exists (backward-compatible)
- Done tasks always sorted to the bottom regardless of manual order
- Bilingual: drag handle tooltip in Japanese and English

## 2026-05-18 - Weekly Summary
- Weekly button in header (visible when any task has completedAt, hidden in batch mode)
- Bottom-sheet overlay (same pattern as Statistics view)
- Four stat cards: tasks completed in last 7 days, categories covered, high-priority done, remaining active tasks
- Task preview list: up to 8 completed tasks shown with category badge and title
- "Generate AI summary" button calls Claude Haiku with completed task list
- Loading state shows spinning indicator while Claude generates the review
- Generated text displayed in a styled box with left border accent
- "Regenerate" button allows refreshing the summary at any time
- Summary text resets when switching boards
- No schema change; session-only state (not persisted to localStorage)
- Bilingual: full Japanese/English UI strings for all interactions
