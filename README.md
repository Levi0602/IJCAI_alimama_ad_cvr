# IJCAI_alimama_ad_cvr  
A CVR's competition in Tianchi  
_1_ data preprocess and feature engineering  
_2_ merge feature and df   
_3_lgb season1  
_3_ffm season2  
ig:The ffm model in libffm file which is likely to overfitting are supposed to run in the system of Windows.  

season 2 score: top 5% (226/5204)

天池阿里妈妈搜索广告复赛方案

比赛介绍
依赖包

sklearn、lightgbm、pandas、numpy、matplotlib、pickle、h5py、tqdm、ffm
运行环境

jupyter + python3.6
运行准备

创建目录：mkdir input && mkdir cache && mkdir feats && mkdir rests
数据预处理：洗脱数据，替换nan值

添加时间维度特征合并数据后存为pkl格式。源码
特征工程：

    1、通用点击率 user源码 item源码 shop源码
    2、各维度时间加权后的点击量 源码
    3、平滑后的CVR 源码
    4、target特征处理，（均值、方差、标准差等描述性统计特征）源码
    5、item、user、shop维度下各个原始level特征（如item_price_level）的描述性统计特征 源码
    6、user最后1~2次的行为特征(shift) 源码

模型
使用了LigthGBM和ffm(非常容易过拟合，但效果拔群)，由于备战考研，精力有限，最后只用了ffm一个单模型。 具体见源码

总结
感谢组委会提供这么好的竞赛机会通大神们一起学习。虽然是自己第一次参加这类数据竞赛成绩也不是很理想，不过真实的学到了很多知识，有读了很多paper，CTR预估模型千千万（LR、GBDT、Wide&Deep、FM&FFM、DeepFM...），但是后来还是只用了简单的模型，精力太有限了。我把所有的功夫都花在了特征处理上，如果没有好的特征和数据处理喂进去，即使再牛逼的模型也是白瞎。关于特征，一开始我就用原始的特征，然后一点点加进去，看feature重要度，然后再根据重要度进行延伸，同时也考虑特征的多样性。用模型进行验证后去掉没有用的特征，不断迭代。


