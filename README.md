![](https://img.shields.io/badge/技育CAMP-2024_vol22-brown)
![](https://img.shields.io/badge/状態-デバック-red)
![](https://img.shields.io/badge/build-passing-green)

## プロジェクト名

GiftCompass（ギフトコンパス）

<!-- プロジェクトについて -->

## プロジェクトについて

プレゼント
    
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
 
## フロントエンド(ダミーデータ版)
- ホーム画面<br>開催されているイベントの概要が一覧できる。２つのダミーイベントが登録されている状態。「詳細を見る」から下の項目に移動する。<br><img src="https://github.com/user-attachments/assets/c951edc7-6a59-4170-b6bc-41533161b358" width="200">
- イベント詳細情報画面<br>イベントの詳細とGoogleMapで（本来は屋台の位置などをマーカで示せるが、APIの関係で暗転中...）位置を確認できる<br>また、このイベントに対する投稿を一覧できる。（adminから一件の投稿がある状態）<br><img src="https://github.com/user-attachments/assets/b8cf7b19-0ff0-417b-b4ca-03c68e411d54" width="200">
- SNS画面<br>開催中のイベント名及び日程一覧と、FeSNSのタイムラインが表示される。右下の＋ボタンから投稿ができる。<br>ハートボタンからその投稿にいいねできる。<br><img src="https://github.com/user-attachments/assets/d4c15bb1-49dc-476c-9f02-d41cd50a4b22" width="200">
- イベント登録画面<br>イベント開催側が、イベントの情報を登録できる。<br>屋台などの位置は、緯度経度で指定するのでGUIで登録できるようにしたい<br><img src="https://github.com/user-attachments/assets/6b84842b-d348-4a4a-a9e5-ebb817c8f4dd" width="200">
- ログイン画面<br><img src="https://github.com/user-attachments/assets/d315eb11-5e46-4e4c-bf68-87bd4dbe9936" width="200">



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

