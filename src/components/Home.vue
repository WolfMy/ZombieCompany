<template>
<div class="home">
    <Row>
        <Col span="24">
            <Card dis-hover style="margin:24px 0px;padding:24px 24px;">
                <h1>讨论404</h1>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
            </Card>
        </Col>
    </Row>
    <el-carousel :interval="4000" type="card" height="700px">
        <el-carousel-item>
            <Card style="text-align:left;">
                <img src="home/BatchQuery.png" slot="title" class="card-img-top">
                <h3>僵尸企业智能预测</h3>
                <p>通过人工智能、机器学习、数据挖掘技术对企业多维度建模分析，上传企业相关数据即可实现对僵尸企业的高精度预测。</p>
            </Card>
        </el-carousel-item>
        <el-carousel-item>
            <Card style="text-align:left;">
                <img src="home/BasicInformation.png" slot="title" class="card-img-top">
                <h3>数据分布可视化</h3>
                <p>通过对数据基本信息进行可视化，我们可以直观的了解到数据中各个特征的分布情况，对数据的整体情况有了一个直观了解，这将会对我们之后对数据进行预处理和建模提供重要依据。</p>
            </Card>
        </el-carousel-item>
        <el-carousel-item>
            <Card style="text-align:left;">
                <img src="home/RelevanceExplore.png" slot="title" class="card-img-top">
                <h3>数据关联性探索</h3>
                <p>关联性探索将通过数据可视化的方式，直观地去了解数据中各个特征之间的关系，其主要目的是挖掘“各个特征”与“是否是僵尸企业（flag）”这一特征之间的关系，从而挖掘和探索出对能否成为僵尸企业这一判断起到重要作用的特征。</p>
            </Card>
        </el-carousel-item>
        <el-carousel-item>
            <Card style="text-align:left;">
                <img src="home/CorporatePortraits.png" slot="title" class="card-img-top">
                <h3>僵尸企业画像</h3>
                <p>通过输入企业ID，展示当前企业基本信息。此外，我们获取了十五个与判断是否是僵尸企业起到关键作用的特征，并可视化当前企业与其他企业的数据分布情况。</p>
            </Card>
        </el-carousel-item>
        <el-carousel-item>
            <Card style="text-align:left;">
                <img src="home/ModelTraining.png" slot="title" class="card-img-top">
                <h3>模型训练可视化</h3>
                <p>模型训练可视化描述文字。。。</p>
            </Card>
        </el-carousel-item>
    </el-carousel>
    <!--Row :gutter="16">
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/BatchQuery.png" slot="title" class="card-img-top">
                <h3>僵尸企业智能预测</h3>
                <p>通过人工智能、机器学习、数据挖掘技术对企业多维度建模分析，上传企业相关数据即可实现对僵尸企业的高精度预测。</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/BasicInformation.png" slot="title" class="card-img-top">
                <h3>数据分布可视化</h3>
                <p>通过对数据基本信息进行可视化，我们可以直观的了解到数据中各个特征的分布情况，对数据的整体情况有了一个直观了解，这将会对我们之后对数据进行预处理和建模提供重要依据。</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/RelevanceExplore.png" slot="title" class="card-img-top">
                <h3>数据关联性探索</h3>
                <p>关联性探索将通过数据可视化的方式，直观地去了解数据中各个特征之间的关系，其主要目的是挖掘“各个特征”与“是否是僵尸企业（flag）”这一特征之间的关系，从而挖掘和探索出对能否成为僵尸企业这一判断起到重要作用的特征。</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/CorporatePortraits.png" slot="title" class="card-img-top">
                <h3>僵尸企业画像</h3>
                <p>通过输入企业ID，展示当前企业基本信息。此外，我们获取了十五个与判断是否是僵尸企业起到关键作用的特征，并可视化当前企业与其他企业的数据分布情况。</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/ModelTraining.png" slot="title" class="card-img-top">
                <h3>模型训练可视化</h3>
                <p>模型训练可视化描述文字。。。</p>
            </Card>
        </Col>
    </Row-->
    
</div>
</template>
<script>

export default {
    mounted(){
        
    }
}
</script>
<style scoped>
h1 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem!important;
    color: #464c5b;
}
h3 {
    margin-bottom: 0.5rem!important;
}
p {
    color: #657180;
}
.lead {
    margin-top: 0;
    margin-bottom: 1rem;
    font-size: 1.25rem;
    font-weight: 300;
}
.card-img-top {
    width: 100%;
    border-top-left-radius: calc(.25rem - 1px);
    border-top-right-radius: calc(.25rem - 1px);
}
</style>