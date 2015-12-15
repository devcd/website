# devcd website pelican project

Use pelican to make a website for developer at Chengdu.
成都开发者专门站点，发布信息，活动公告，技术交流资料等

## how to write content using pelican

需要使用到  Python，最好有 virtualenv

`pip install pelican markdown ghp-import fabric livereload`

其中 fabric 是用来进行一键自动发布的，可以不装，但是建议使用。

[Pelican 的文档](http://docs.getpelican.com/)

clone 本库的代码之后，所有的markdown 和图片等在 content 目录里，写好 markdown 之后，执行 `fab build` 生成所有文件到 output 目录，`fab serve` 可以在本地 8001 端口查看页面效果，好了之后提交代码到版本库，然后执行 `fab devcd` 将库同步到github 并且发布到 devcd.github.io.git 这个专门的 github pages 库，就可以在 http://devcd.io 上看到了。


