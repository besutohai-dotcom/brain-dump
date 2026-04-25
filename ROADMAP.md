# ブレインダンプ — Autonomous Improvement Roadmap

Managed by an autonomous Claude agent. Updated after each improvement cycle.
Last updated: 2026-04-23

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

## 📋 Planned (priority order)
- [ ] Swipe to complete / swipe to delete (mobile gesture)
- [ ] Language toggle — Japanese / English switch
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

## 💡 User Ideas
- Voice input for easier navigation ✅
- Best app possible with AI + user ideas
- Autonomous improvement loop (this!)

## 📝 Change Log
- 2026-04-21: Initial deploy, voice input, CORS fix
- 2026-04-21: Task editing (✏️ inline), dark mode (prefers-color-scheme), undo delete (toast)
- 2026-04-21: Priority levels — 高/中/低 badge on each task, click to cycle, auto-sort by priority

## 2026-04-22 - キーワード検索バー
- タスク一覧をキーワードでリアルタイム絞り込む検索バーを追加
- タイトル・元メモ・カテゴリ名を対象に検索
- 検索結果ゼロ時の空状態メッセージを追加

## 2026-04-23 - 期限設定機能
- タスクの編集モードに「期限」日付ピッカーを追加
- 期限バッジをタスクカードに表示（色分け：期限切れ赤・今日オレンジ・将来グレー）
- 期限なしはバッジ非表示、「× クリア」で期限を削除可能
- localStorage互換性を維持（dueDate: null でデフォルト）

## 完了した改善
- [x] Export data — JSON ・テキストでダウンロード — 2026-04-25
- [x] スワイプでタスク完了 / スワイプで削除（モバイルジェスチャー） — 2026-04-24

## 2026-04-25 - データエクスポート
- タスクを2形式でダウンロードできる「📤 出力」ボタンをヘッダーに追加
- JSON：全タスクデータをbrain-dump-YYYY-MM-DD.jsonで保存
- テキスト：カテゴリ別で読みやすいbrain-dump-YYYY-MM-DD.txtで保存
- localStorageスキーマ互換性を維持
