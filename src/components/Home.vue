<template>
<div class="home">
    <Row>
        <Col span="24">
            <Card dis-hover style="margin:24px 0px;padding:12px 24px;background-image:url('http://cdn.zomboost.dcts.top/%E5%B0%81%E9%9D%A2%E5%9B%BE.png');background-repeat:no-repeat;background-position:center;">
                <img src="ZomBoost.png"><br>
                <img src="SubTitle.png">
                <!--h1 class="title">ZomBoost</h1>
                <h2>基于CatBoost的僵尸企业识别系统</h2>
                <br>
                <p class="lead text-muted">设计思路：<strong>智能识别</strong>与<strong>可视化分析</strong>相辅相成</p>
                <p class="lead text-muted">组件介绍：对于部分组件，提供组件<Button size="small" type="info">说明</Button>，详细介绍组件的设计理念和功能</p-->
            </Card>
        </Col>
    </Row>
    <Row :gutter="16">
        <Col :xs="24" :md="7" style="margin:0px 0px 16px 0px;">
            <Row>
                <Card style="text-align:left;">
                    <img src="http://cdn.zomboost.dcts.top/BatchQuery.png" slot="title" class="card-img-top">
                    <h3>僵尸企业智能识别</h3>
                    <p>通过人工智能、数据挖掘技术对企业多维度建模分析，上传企业相关数据即可实现对僵尸企业的高精度识别。</p>
                </Card>
            </Row>
            <Row style="margin:16px 0px;">
                <Card style="text-align:left;">
                    <img src="http://cdn.zomboost.dcts.top/BasicInformation.png" slot="title" class="card-img-top">
                    <h3>数据分布可视化</h3>
                    <p>通过对数据基本信息进行可视化，可以直观了解数据中各个特征的分布情况，从而为数据预处理和建模提供重要依据。</p>
                </Card>
            </Row>
        </Col>
        <Col :xs="24" :md="10">
            <Card style="text-align:left;">
                <img src="http://cdn.zomboost.dcts.top/RelevanceExplore.png" slot="title" class="card-img-top">
                <h3>数据关联性探索</h3>
                <p>通过数据可视化的方式，直观呈现数据中各个特征之间的关系，从而挖掘和探索与僵尸企业关联度最高的重要特征。</p>
            </Card> 
        </Col>
        <Col :xs="24" :md="7">
            <Row>
                <Card style="text-align:left;">
                    <img src="http://cdn.zomboost.dcts.top/CorporatePortraits.png" slot="title" class="card-img-top">
                    <h3>僵尸企业画像</h3>
                    <p>通过输入企业ID，展示当前企业是否为僵尸企业。对企业的基本信息及十五个用于判断是否为僵尸企业的重要特征进行可视化呈现，从而对企业进行全息画像。</p>
                </Card>
            </Row>
            <Row style="margin:16px 0px;">
                <Card style="text-align:left;">
                    <img src="http://cdn.zomboost.dcts.top/ModelTraining.png" slot="title" class="card-img-top">
                    <h3>模型训练可视化</h3>
                    <p>展示模型参数信息及与模型训练相关的数据，横向对比其他模型，多指标综合评估模型性能。</p>
                </Card>
            </Row>
        </Col>
    </Row>
    
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
    font-size: 4rem;
    color: #424949;
    font-family: Verdana;
}
h2 {
    font-size: 1.8rem;
    margin-bottom: 1.5rem!important;
    color: #424949;
}
h3 {
    margin-bottom: 0.5rem!important;
}
p {
    color: #797D7F;
}
.lead {
    margin-top: 1rem;
    margin-bottom: 0rem;
    font-size: 1.25rem;
    font-weight: 400;
}
.card-img-top {
    width: 100%;
    border-top-left-radius: calc(.25rem - 1px);
    border-top-right-radius: calc(.25rem - 1px);
}
.title {
    letter-spacing:8px;  
}
</style>