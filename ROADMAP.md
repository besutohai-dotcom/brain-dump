# ブレインダンプ — Autonomous Improvement Roadmap

Managed by an autonomous Claude agent. Updated after each improvement cycle.
Last updated: 2026-05-04

## ✅ Done
- [x] Core app: brain dump input → AI categorization → task list
- [x] Natural language query bar
- [x] AI next-action suggestions per task
- [x] Category filter chips with colors
- [x] Mark done / delete tasks
- [x] localStorage persistence
- [x] iPhone PWA (Add to Home Screen)
- [x] Deployed to GitHub Pages
- [x] Voice input (Safari browser mode)
- [x] Fixed CORS header for direct browser API calls
- [x] Task editing — inline ✏️ edit title and original text
- [x] Dark mode — auto-detects iOS/macOS system preference
- [x] Undo delete — toast with 4-second undo button
- [x] Priority levels — High/Medium/Low badge, clickable to cycle, tasks sorted by priority
- [x] Search bar — filter tasks by keyword
- [x] Due dates — optional date picker per task, color-coded overdue/today/future badges
- [x] Swipe to complete / swipe to delete (mobile gesture)
- [x] Export data — JSON / text download
- [x] Language toggle — Japanese / English switch

## 📋 Planned (priority order)
- [ ] Better onboarding — guided first-use flow
- [ ] Task notes — expandable sub-notes field
- [ ] Batch select — checkbox mode, bulk complete/delete
- [ ] Statistics view — tasks done per day, category breakdown
- [ ] Browser push notifications — remind about active tasks
- [ ] Recurring tasks — daily/weekly repeat option
- [ ] Markdown in notes — render bold, italic, checklists
- [ ] Multiple boards — switch between different brain-dump contexts
- [ ] Share task — copy shareable text summary
- [ ] Drag to reorder tasks

## 🧪 Test Log

| Date | Feature | Verified | Status |
|------|---------|----------|--------|
| 2026-04-21 | Initial deploy | Setup | ✅ |
| 2026-04-21 | Task editing, dark mode, undo delete | HTML output verified | ✅ |
| 2026-04-21 | Priority levels (High/Medium/Low) | Deployed | ✅ |
| 2026-05-04 | Language toggle (JP/EN) | Deployed | ✅ |

## 💡 User Ideas
- Voice input for easier navigation ✅
- Best app possible with AI + user ideas
- Autonomous improvement loop (this!)

## 📝 Change Log
- 2026-04-21: Initial deploy, voice input, CORS fix
- 2026-04-21: Task editing (✏️ inline), dark mode (prefers-color-scheme), undo delete (toast)
- 2026-04-21: Priority levels — 高/中/低 badge on each task, click to cycle, auto-sort by priority
- 2026-04-22: キーワード検索バーを追加
- 2026-04-23: 期限設定機能（日付ピッカー、色分けバッジ）
- 2026-04-24: スワイプでタスク完了 / 削除（モバイルジェスチャー）
- 2026-04-25: データエクスポート（JSON / テキスト）
- 2026-05-04: 言語切り替え（日本語 / English）— header toggle, full UI + AI prompts adapt to selected language

## 2026-05-04 - 言語切り替え機能 (Language Toggle)
- ヘッダーに「EN / JP」切り替えボタンを追加
- 全UIテキストを日本語・英語の両方で翻訳
- 言語設定はlocalStorageに保存（backward-compatible: デフォルト ja）
- AIプロンプト（分類・提案・クエリ）も選択言語に合わせて切り替え
- 音声入力言語も切り替え（ja-JP / en-US）
- 日付表示フォーマットも言語に合わせて切り替え
