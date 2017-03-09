#About LTP(How to make some NLP fun jobs:)
+ Language Technology Platform,a platform to DO some Natural Language Processing works.
+ It powered by HIT,a institute of Haerbin，Harbin Institute of Technology，URL:http://ir.hit.edu.cn/

#How to begin
+ 语言技术平台（Language Technology Platform，LTP）是哈工大社会计算与信息检索研究中心历时十年开发的一整套中文语言处理系统。LTP制定了基于XML的语言处理结果表示，并在此基础上提供了一整套自底向上的丰富而且高效的中文语言处理模块（包括词法、句法、语义等6项中文处理核心技术），以及基于动态链接库（Dynamic Link Library, DLL）的应用程序接口、可视化工具，并且能够以网络服务（Web Service）的形式进行使用。
+ 从2006年9月5日开始该平台对外免费共享目标代码，截止目前，已经有国内外400多家研究单位共享了LTP，也有国内外多家商业公司购买了LTP，用于实际的商业项目中。
+ 2010年12月获得中国中文信息学会颁发的行业最高奖项：“钱伟长中文信息处理科学技术奖”一等奖。
+ 2011年6月1日，为了与业界同行共同研究和开发中文信息处理核心技术，我中心正式将LTP开源。
+ 2013年9月1日，语言技术平台云端服务"语言云"正式上线。


## Docs
+ http://ltp.readthedocs.io/zh_CN/latest/

## Directions
+ 研究方向包括语言分析、信息抽取、情感分析、问答系统、社会媒体处理和用户画像6个方面
+ LTP basic works:对于中文文本进行分词、词性标注、句法分析
+ 1.针对单一自然语言处理任务，生成统计机器学习模型的工具
+ 2.针对单一自然语言处理任务，调用模型进行分析的编程接口
+ 3.使用流水线方式将各个分析工具结合起来，形成一套统一的中文自然语言处理系统
+ 4.系统可调用的，用于中文语言处理的模型文件
+ 5.针对单一自然语言处理任务，基于云端的编程接口

## Get the Project(github),and model
+ 1.Using C++:
+ clone this:https://github.com/HIT-SCIR/ltp
+ 2.Using Python:
+ for i using python,https://github.com/HIT-SCIR/pyltp
+ 使用 pip 安装
+ $ pip install pyltp
+ 或从源代码安装
+ $ git clone https://github.com/HIT-SCIR/pyltp
+ $ git submodule init
+ $ git submodule update
+ $ python setup.py install
+ http://pyltp.readthedocs.io/zh_CN/latest/
+ 3.get the model:http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569

## ps: use docker to maintance this serious tools
+ see another doc: How to use docker image to improve R&D more than 30% dev speed!


## Other
+ 半世纪以来自然语言处理 (NLP)研究取得两点重要认识和三大重要成果 ,即认识到 :(1 )对于句法分析 ,基于单一标记的短语结构规则是不充分的 ;(2 )短语结构规则在真实文本中的分布呈现严重扭曲。换言之 ,有限数目的短语结构规则不能覆盖大规模语料中的语法现象。这与原先的预期大相径庭。NLP技术的发展在很大程度上受到这两个事实的影响。从这个意义上说 ,本领域中称得上里程碑式的成果是 :(1 )复杂特征集和合一语法 ;(2 )语言学研究中的词汇主义 ;(3 )语料库方法和统计语言模型。大规模语言知识的开发和自动获取是NLP技术的瓶颈问题。因此 ,语料库建设和统计学理论将成为该领域中的关键课题


## 开源协议
+ 1.语言技术平台面向国内外大学、中科院各研究所以及个人研究者免费开放源代码，但如上述机构和个人将该平台用于商业目的（如企业合作项目等）则需要付费。
+ 除上述机构以外的企事业单位，如申请使用该平台，需付费。
+ 2.凡涉及付费问题，请发邮件到 car@ir.hit.edu.cn 洽商。
+ 3.如果您在 LTP 基础上发表论文或取得科研成果，请您在发表论文和申报成果时声明“使用了哈工大社会计算与信息检索研究中心研制的语言技术平台（LTP）”，参考文献中加入以下论文： Wanxiang Che, Zhenghua Li, Ting Liu. LTP: A Chinese Language Technology Platform. In Proceedings of the Coling 2010:Demonstrations. 2010.08, pp13-16, Beijing, China. 同时，发信给car@ir.hit.edu.cn，说明发表论文或申报成果的题目、出处等。

# 算法和模型实践
## 模型概述
+ cws.model 分词模型，单文件
+ pos.model   词性标注模型，单文件
+ ner.model   命名实体识别模型，单文件
+ parser.model    依存句法分析模型，单文件
+ srl_data/   语义角色标注模型，多文件
## Dev in python
+ ltp限制用户输入字数少于1024字，分词结果少于256词。

