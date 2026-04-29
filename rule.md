# learning-notes

個人の学習内容を教科書的にまとめたノートリポジトリ。  
プログラミング・CS・機械学習・AI・理学・工学など幅広い分野を対象とする。

> **言語**: 日本語（将来的に英語対応を検討）  
> **公開**: GitHub Pages（MkDocs）への移行を前提とした構成

---

## ディレクトリ構成

```
learning-notes/
├── README.md               # このファイル（リポジトリの顔）
├── mkdocs.yml              # MkDocs設定（将来のPages公開用）
│
└── docs/                   # コンテンツのルート
    ├── index.md            # トップページ・全体目次
    │
    ├── cs/                 # CS・プログラミング
    │   ├── index.md        # カテゴリ目次
    │   ├── python/
    │   │   ├── index.md
    │   │   ├── 10_basics.md
    │   │   ├── 20_oop.md
    │   │   └── images/
    │   ├── algorithms/
    │   │   ├── index.md
    │   │   └── 10_sorting.md
    │   └── git/
    │       └── index.md
    │
    ├── ml-ai/              # 機械学習・AI
    │   ├── index.md
    │   ├── foundations/
    │   │   ├── 10_linear_regression.md
    │   │   └── 20_neural_networks.md
    │   ├── deep-learning/
    │   │   └── index.md
    │   └── llm/
    │       └── index.md
    │
    ├── math/               # 数学・統計
    │   ├── index.md
    │   ├── linear-algebra/
    │   ├── calculus/
    │   └── statistics/
    │
    ├── science/            # 理学（物理・化学など）
    │   ├── index.md
    │   └── physics/
    │
    ├── engineering/        # 工学
    │   └── index.md
    │
    └── _templates/         # 執筆テンプレート（公開対象外）
        └── topic-template.md
```

---

## カテゴリ一覧

| ディレクトリ | 内容 |
|---|---|
| `cs/` | プログラミング言語・アルゴリズム・ツール・フレームワーク |
| `ml-ai/` | 機械学習・深層学習・LLM |
| `math/` | 線形代数・微積分・統計 |
| `science/` | 物理・化学など理学全般 |
| `engineering/` | 工学全般 |

---

## 運用ルール

### ファイル命名
- 連番は `10_, 20_, 30_` のように10刻みにする（途中挿入しやすくするため）
- ディレクトリ名・ファイル名は英数字とハイフンのみ（スペースなし）

### 画像
- 各トピックディレクトリ内の `images/` に配置する
- 記事からは相対パスで参照する（例: `./images/example.png`）

### ブランチ運用
- `main`: 公開済みコンテンツ
- `draft/*`: 執筆中のコンテンツ（例: `draft/python-oop`）

### IssueをToDo管理に使う
- 「〇〇を書く」という粒度でIssueを立てる
- 書き終えたらPRをマージしてIssueをクローズ

---

## GitHub Pages への移行について

このリポジトリは将来的に **MkDocs + Material テーマ** でPages公開することを想定している。  
そのため以下の規則を守って執筆する。

- コンテンツはすべて `docs/` 以下に置く
- 画像は相対パスで参照する
- 各記事の冒頭に frontmatter を書く（後述）

移行時は `mkdocs.yml` を編集してGitHub Actionsを設定するだけで公開できる。
