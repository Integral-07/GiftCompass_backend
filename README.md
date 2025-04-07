![](https://img.shields.io/badge/技育CAMP-2024_vol22-brown)
![](https://img.shields.io/badge/状態-デバック-red)
![](https://img.shields.io/badge/build-passing-green)

## プロジェクト名

GiftCompass（ギフトコンパス）

<!-- プロジェクトについて -->

## プロジェクトについて

プレゼントを選ぶ際の参考になるデータを、贈る相手からこっそり直接得られるアプリ（B.E.）。
    
### 背景
1. プレゼントを贈る際に、相手の好みのものをあげたいが、サプライズ要素も残しておきたい<br>
  
　これらの課題を解決するために占い・性格診断型ギフト選択補助アプリを開発した<br>

### 概要
➢ ユーザの任意の項目(設問文・回答選択肢)で、占い・性格診断のページを作成できる<br>
➢ 同じ相手に複数回適用できるように、ページのデザインを複数用意してある<br>
➢ 作成したページをプレゼントを贈りたい相手に共有し、回答してもらう<br>
➢ ユーザは回答を見ることができ、その回答内容を基にプレゼントを選択できる<br>
➢ 個人情報漏洩等の問題点を抱えている<br>

### 機能
➢ 占い・性格診断ページの作成機能（設問文の追加編集/設問文に対する回答選択肢の追加編集）<br>
➢ リンクを共有するだけでページが共有でき、一般的な占い・性格診断と同じように回答できる<br>
➢ 相手の回答をバレずに見ることができる<br>


## 使用技術一覧

<!-- シールド一覧 -->
<p style="display: inline">
  <!-- フロントエンドのフレームワーク -->
  <!-- バックエンドのフレームワーク -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- ミドルウェア -->
  <img src="https://img.shields.io/badge/-SQLite-336791.svg?logo=sqlite&style=for-the-badge">
  <!-- インフラ -->
  <img src="https://img.shields.io/badge/-Github-181717.svg?logo=github&style=for-the-badge">
</p>

## 環境

| 言語・フレームワーク    | バージョン  |
| --------------------- | ---------- |
| Python                | mcr.microsoft.com/devcontainers/python:1-3.12-bullseye     |
| Django                | 4.2.0      |
| sqlite                | 3.45.3     |

その他のパッケージのバージョンは requirements.lock を参照してください

