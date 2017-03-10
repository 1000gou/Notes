# Github関連メモ


### はじめに
Gitの操作の概念をGoogle画像検索で確認しましょう。  
私が探したなかでは以下の画像がわかりやすかったです(下図のindexはstageと説明されている場合もあります。)
[![Git操作の](https://illustrated-git.readthedocs.io/en/latest/_images/git-flows.svg)][1]
[1]: https://illustrated-git.readthedocs.io/en/latest/_images/git-flows.svg


### Githubのリポジットの作成
Gitのホームページ（マイページ）→『＋ボタン』→New repository

### GitHubをクローニングする  
(例)$git clone https://github.com/1000gou/github

### 編集
クローニングしたフォルダ（ローカル）のなかで、普通にファイルの追加や編集や削除を行う。

### 編集結果のアップロード  
1. ファイルの作成/変更/削除をgitのインデックスに追加    
コマンドベース：$git add　ファイル名　　もしくは　$git add .  (すべてのファイル)    
GitKraken:Stage all changesボタンを押す

1. 変更結果をローカルリポジトリにコミット  
コマンドベース：git commit  
GitKraken：コメントの入力してcommitボタンを押す  

1. ローカルリポジトリをホストへプッシュ  
コマンドベース：$git push origin master  
GitKraken：Pushボタンを押す  

### リモートの状態をローカルを最新の状態へダウンロードする
1. ローカルの修正箇所の確認  
コマンド：git diff
GitKraken：

1. ローカルの状態を確認する
コマンド：$git status  
GitKraken：

1. ワークスペースの変更を保存する場合は編集のアップロード(add,commit,push)する
1. ワークスペースの変更が必要ない場合は変更を取り消す。  
コマンドベース:$git checkout ファイル名　　もしくは  　$git checkout . (すべてのファイル)  

1. リモートの状態をローカルにコピーする  
コマンドベース：$git pull  
GitKraken：Pullボタンを押す  
