#Follow me
+ 1.初始化本地Docker环境
+ download https://www.docker.com/products/docker-toolbox
+ install it and setup a Docker environment ,ps, if using windows, select windows version；技术部内部mac版本联系我，丁丁发你
+ 2.配置本地环境，docker 分为客户端docker-client和服务端docker-daemon两部分，docker-daemon可以监听unix scoket，也可以在tcp socket（默认端口为4234）
+ docker-client会通过一个叫DOCKER_HOST的环境变量读取服务地址和端口，因此你应该在你的bash_profile文件里面添加一行：export DOCKER_HOST=tcp://127.0.0.1:4243
+ 3.获取镜像，下载一个ubuntu Image：docker pull ubuntu:13.10；或者使用图形化的界面下载（安装1所得）
+ 4.配置镜像，启动，测试image是否正常运行

#Docker简介
+ Docker提供了一种可移植的配置标准化机制，允许你一致性地在不同的机器上运行同一个Container;而LXC本身可能因为不同机器的不同配置而无法方便地移植运行;
+ Docker以App为中心，为应用的部署做了很多优化，而LXC的帮助脚本主要是聚焦于如何机器启动地更快和耗更少的内存;
+ Docker为App提供了一种自动化构建机制(Dockerfile)，包括打包，基础设施依赖管理和安装等等;
+ Docker提供了一种类似git的Container版本化的机制，允许你对你创建过的容器进行版本管理，依靠这种机制，你还可以下载别人创建的Container，甚至像git那样进行合并;
+ Docker Container是可重用的，依赖于版本化机制，你很容易重用别人的Container(叫Image)，作为基础版本进行扩展;
+ Docker Container是可共享的，有点类似github一样，Docker有自己的INDEX，你可以创建自己的Docker用户并上传和下载Docker Image;
+ Docker提供了很多的工具链，形成了一个生态系统;这些工具的目标是自动化、个性化和集成化，包括对PAAS平台的支持等;
+ 那么Docker有什么用呢?对于运维来说，Docker提供了一种可移植的标准化部署过程，使得规模化、自动化、异构化的部署成为可能甚至是轻松简单的事情;而对于开发者来说，Docker提供了一种开发环境的管理方法，包括映像、构建、共享等功能，而后者是本文的主题。


## 常用命令
+ 比较常用的Docker命令:
+ docker version: 查看Docker版本。
+ docker pull [image name]: 下载一个docker的镜像，类似git拉代码的命令，不过这个是拉docker镜像。
+ docker images: 列出所有的镜像。
+ docker run [image name] [command]: 运行一个镜像的某个命令，这样会产生一个container。
+ docker ps: 列出container。
+ docker start [container name]: 启动一个container。
+ docker stop [container name]: 停止一个container。
+ docker rm [container name]: 删除一个container。
+ docker rmi [image name]: 删除一个image镜像。
