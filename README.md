# PythonExerciseBook
Python script practice notebook

There is a thought in my mind that I need to practice my coding skill after this busy time. But in fact, I could not arrange a 
sequence of time to keep coding. So I creat this position to record my road in python scripy learning.
As for woking or my coding skill groth, learning python from step to step and I believe it worth it.
Keep coding!

## TodoList

- [x]  MyPath Scripy
- [ ]  Learning panda module
- [ ] csvFile process
- [ ] subprocess.call function 
- [ ] ...

> Try  use console to control git command.

```bash
git fetch
git add .
# git add [path]
git commit -m "xxx"
git push
# git push origin name

git status
git log
git reset
git stash

git clone/pull
git bransh xxx
git bransh -d xxx #删除分支
git checkout xxx
git pull -rebase xxx

# 回退1个change的写法就是git reset HEAD^，
# 2个为HEAD^^，
# 3个为HEAD~3，以此类推。

git -h

```

## Q&A

Quit bash

#### 1、git log 退出

如果commit（提交）比较多，git log 的内容就会比较多；当满屏放不下，就会显示冒号，回车（往下滚一行）、空格（往下滚一页）可以继续查看剩余内容；退出：英文状态下 按 **q** 可以退出git log 状态。



#### 2、git commit 

当该命令没有带-m参数时，会跳出commit change log （COMMIT_EDITMSG）界面（如下所示），这个是vi编辑器（也有可能是vim编辑器），和linux的使用时一样的，因为涉及到是否要保存编辑内容，所以退出命令有多种。

2.1 保存并退出：
（1）按 Esc 键退出编辑模式，英文模式下输入 :wq ，然后回车(write and quit)。

（2）按 Esc 键退出编辑模式，大写英文模式下输入 ZZ ，然后回车。

2.2 不保存退出：
按 Esc 键退出编辑模式，英文模式下输入 :q! ，然后回车。

按 Esc 键退出编辑模式，英文模式下输入 :qa! ，然后回车。


miaochaofeng
2021.11.12
